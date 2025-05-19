## これはなに？

[RESONARK](https://sepnekoya.com/resonark/) のスコアの json から、 [RRSV(ver1.9)](https://x.com/big_pudding_vrc/status/1913402138606317662) に貼り付けられるような形式にするものです。

Python が実行できる環境で動かしてください。使い方は説明をみたりして察してください。

## 使い方

1. このディレクトリの配下に、楽曲リスト `list.tsv` を用意する (カラムは、 `楽曲名\t難易度` となるようにする)
1. このディレクトリの配下に、RESONARK から出した自分のスコアのファイルを用意する (`pt1.json`, `pt2.json`)
1. `python3 extract.py`を実行する
1. 出力された `score.tsv` の内容を `スコア,Tech-Rate` に貼り付け、 `state.tsv` の内容を `FC/AP/EX` に貼り付ける
