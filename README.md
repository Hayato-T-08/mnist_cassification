# 簡単な手書き文字識別アプリ

![スクリーンショット (30)](https://user-images.githubusercontent.com/104160005/226058503-6375408f-abe2-421f-b554-70e50192bca3.png)

簡単な手書き文字識別アプリを作りました。
0から9の数字を書くとAIがどの数字を書いたか識別してくれます。

# 必要なライブラリ

tensorflow,os,tkinter,numpy,PIL

pipでインストールしてください。

例 pip install tensorflow

# 必要なソフト

ghostscript

macはhomebrew,windowsは"https://ghostscript.com/releases/gsdnld.html"

からダウンロードした後に環境変数にパスを追加してください

## 起動の仕方

ターミナルでcd codeを実行した後python mnist_classifierを実行

mnist_classifierを実行

## 操作方法

penを押すと字が書けます。

eraserを押すと文字を消すことができます。

submitを押すと書いた文字をAIに判別してもらえます。

resetを押すと書いた文字がすべて消えます。

exitを押すとアプリが終了します。

## ファイル説明

mnist_classifier.py　アプリのソースです。

ml.py　学習用のコードです。

pred_mypic.py 画像から数字を識別するテストコードです。

mnist_weight.hdf5 重みを保存したファイルです。

## 参考文献
https://qiita.com/dolce_itf/items/be85244a31654d1d56ef

https://www.idnet.co.jp/column/page_245.html

https://www.nslabs.jp/monkey-python-02b.rhtml#s10

