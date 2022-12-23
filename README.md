# send_credit_card_history_to_line
クレジットカードの使用履歴をLineに送るシステム


## ソースコード
https://github.com/ANKM0/showcase/blob/main/remote_mitsui_sumitomo_card/remote_mitsui_sumitomo_card.py
## 設計資料
<details>
<summary>設計資料</summary>


![portfolio_ax1](https://user-images.githubusercontent.com/76755363/186085995-10cbab49-99be-4f08-8da2-35a33b8d3e3c.png)
</details>


## <やりたかったこと>
クレジットカードの使用履歴をLineで確認できるようにする

## <背景>
おばあちゃんが毎月クレジットカードの使用履歴を確認していたが<br>
サイトにたどり着くやり方がたまに分からなくなっていた<br>
そこでLineに通知するシステムを作ればその手間が省けると思い、作成した<br>
## <使った技術>
- 使用言語<br>
Python<br>

- フレームワーク<br>
Selenium<br>

- サーバー<br>
Heroku<br>

- その他<br>
Git,GitHub,VSCode,LINE Notify API
### <選んだ理由>
安定した動作を実現したかったため、<br>
動的な待機ができるSeleniumを使用した


## 苦労したところ
- LineAPIとdjango-allauthの連携<br>
APIの認証周りで苦戦した<br>
公式ドキュメントを読み込む、不明点を検索するなどして、問題を解決した<br>
- 銀行口座からのクローリング<br>
銀行口座のbot対策が固く、上手くクローリング出来なかった<br>
Moneytreeと銀行口座を連携させてそこからクローリングさせることによって問題を解決した
