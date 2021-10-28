# healthcheck_filler

元気で怠惰な人間のためのツール。
特定の健康調査票に適当にそれっぽい数字を入れてくれる。

## 使い方
pythonはインストールされている前提です。
```
$ pip install openpyxl  # for pip
$ conda install openpyxl # for conda
```
``filer.py``とおなじ階層に``healthcheck3_202109-202112.xlsx``を置く。
(学校のホームページにある。)
```
$ python3 filer.py
>>> 平均体温を入力してください。
36.5
Done!!
```
終了