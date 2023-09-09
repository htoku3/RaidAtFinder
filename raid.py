from time import sleep
import shutil
import glob
import os

Screen.showMonitors()
SCREEN_SHOT_DIR = os.environ["USERPROFILE"] + u"\\Documents\\ミストレレイド"
# Make the directory if doesn't exist.
if not os.path.exists(SCREEN_SHOT_DIR):
    os.makedirs(SCREEN_SHOT_DIR)

idx = len(glob.glob(SCREEN_SHOT_DIR + u"\\syasyo*.p*"))

def main():
    for id in range(Screen.getNumberScreens()):        
        croll_all_matches(Screen(id))


def croll_all_matches(screen):
    heads = []
    for i in range(100):
        if len(heads) > 4:
            heads.pop(0)
        match = screen.findAll(Pattern("1694230004746.png").similar(0.90))
        all_failed = True
        for item in sorted(match, key=lambda m: m.y):
            region = Region(item.x, item.y, 350, 100)
            try:
                region.click("1694230231445.png")
            except FindFailed:
                continue
            sleep(0.3)
            succeed = view_each_match(screen, heads)
            all_failed = all_failed and (not succeed)
            

        wheel(Pattern("1694230004746.png").similar(0.90), WHEEL_DOWN, 6)
        if all_failed:
            exit(0)


def view_each_match(screen, heads):
    result_bar = screen.find("1694230609372.png")
    result_region = Region(result_bar.x - 450, result_bar.y  +50, 1050, 550)
    
    # check if duplicated match
    head = read_head(result_region)
    if head in heads:
        result_region.click("1694241003643.png")
        return False
    
    # new match
    heads.append(head)
    last_strength = []
    n_failed = 0
    # scrool to end
    while True:
        if capture_card(result_region, last_strength):
            n_failed = 0
            # scroll more to reduce dups
            wheel(result_region.getCenter(), WHEEL_DOWN, 3)
        else:
            n_failed += 1
        wheel(result_region.getCenter(), WHEEL_DOWN, 2)
        edge_region = Region(result_bar.x + 300, result_bar.y + 400, 250, 250)

        # If the acquisition of a new card fails two times, it is considered to be the end of the ranking.
        if  n_failed > 2:
            break
    
    result_region.click("1694241003643.png")
    return True


def read_head(result_region):
    text = ""
    head = Region(result_region.getX(), result_region.getY(), result_region.getW(), 300)
    for match in head.findAll("1694232648278.png"):
        text += Region(match.x + 90, match.y, 120, 50).text()
    return text


def capture_card(result_region, last_strength):
    global idx
    try:
        top_edge_y = min([item.y for item in result_region.findAll("1694231701518.png")])
        btm_edge_y = min([item.y for item in result_region.findAll("1694231933333.png") if item.y > top_edge_y])
    except ValueError:
       return False
    btm_edge_y += 21
    if 200 < (btm_edge_y - top_edge_y) < 300:
        # Due to lack of OCR accuracy, "strength" was used instead of player name.
        str_list = []
        for match in result_region.findAll("1694232648278.png"):
            if top_edge_y < match.y < btm_edge_y:
                strength = Region(match.x + 90, match.y, 120, 50).text()
                if strength in last_strength:
                    continue
                str_list.append(strength)  # New player
                x0 = match.x - 244
                y0 = match.y - 50
                card = Region(x0, y0, 478, 245)
                # Fond "@"
                if not card.findAll(Pattern("1694238682080.png").similar(0.90)).hasNext():
                    continue
                print("@ was found. Capture!")
                tmpfile = capture(card)
                shutil.move(tmpfile, SCREEN_SHOT_DIR + "\syasyo_{:03}.png".format(idx))
                idx += 1
        if str_list:
            del last_strength[:]
            last_strength.extend(str_list)
            return True
        return False
    else:
        return False 


if __name__ == "__main__":
    main()