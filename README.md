# RaidRankingCaptaure
[SikuliX](http://sikulix.com/) を使って、ミストレレイドのダメージランキングをキャプチャーするスクリプトです。

# 準備

## SikuliX のインストール

[SikuliX](http://sikulix.com) はPCの操作を自動化するツールです。
このスクリプトは「ダメージランキング画面になったらスクショを撮る」操作を自動化するものですが、それを SikuliX に読ませます。

そのため、SikuliX のインストールが必要です。 以下、[公式ドキュメントのインストール手順](http://sikulix.com/quickstart/)とだいたい同じです。

### Java 実行環境のダウンロード
64bit の Java Runtime Environment (JRE) を既にインストールしている場合は不要です。
SikuliX では [OpenJDK](https://openjdk.java.net/) のダウンロードを推奨しているようです。

[公式サイト](https://jdk.java.net/18/)から、 [Windows 64bit 版 の zip ファイル](https://download.java.net/java/GA/jdk18.0.1.1/65ae32619e2f40f3a9af3af1851d6e19/2/GPL/openjdk-18.0.1.1_windows-x64_bin.zip)　を選択してダウンロードします。
解凍すればOKです。 "jdk-18.0.1.1" というフォルダが出来ます。


### SikuliX のダウンロード
[SikuliX のダウンロードページ](https://raiman.github.io/SikuliX1/downloads.html) から [sikulixide-2.0.5-win.jar ファイル](https://launchpad.net/sikuli/sikulix/2.0.5/+download/sikulixide-2.0.5-win.jar)をダウンロードします。
インストールは不要です。

先程解凍した"jdk-18.0.1.1" のフォルダに jar ファイルを突っ込みます。


## スクリプトのダウンロード
[このリンク](https://github.com/htoku3/RaidRankingCaptaure/archive/refs/heads/main.zip) をクリックして下さい。
出来た "RaidRankingCapture-main"  というフォルダを先程と同様に "jdk-18.0.1.1"　に突っ込みます。

# 使い方

## とにかく動かしたい人
"RaidRankingCapture-main" に入って、 **exec_SikuliX.bat** をダブルクリックすると動きます。 (...動くはずです。)

終了はコマンドプロンプトを閉じればOKです。

## スクリプトを確認してから手動で実行したい人
"jdk-18.0.1.1" のフォルダを Shift キーを押しながら右クリックし「PowerShellウィンドウをここで開く」を選択し、

下記のコマンドで SikuliX IDE を実行して下さい。
```
.\bin\java.exe -jar .\sikulixide-2.0.5-win.jar
```
「ファイル」 -> 「開く」 から、 raid.py　を開いて下さい。この画面からスクリプトを編集できます。
「実行ボタン」を押せば実行します。 終了はデフォルト設定では 「Shift + Alt + C」 です。

## どこに保存されるの？

マイドキュメントに「ミストレレイド」というフォルダが作られ、そこに "syasyo000.png, syasyo001.png ..." と保存されていきます。
最大 999 枚まで保存します。

raid.py をテキストエディタで開いて **SCREEN_SHOT_DIR** を編集すれば、場所を変更できます。
