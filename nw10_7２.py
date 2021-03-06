ニューラルネットワーク　人間の脳が物事を判断する処理をまねて作られたシステム
最初の層＝入力層、継ぎ隠れそう　最後　出力層
情報の伝達するとき、ニューロンからニューロンへは入力値に対して重みが欠けられる
ニューロン＝ノード
例えば、男性が４，５，６でそれぞれの重みが２，２，２だとすると　８＋１０＋１２＝３０の力を持つと出力層の結果でわかる
重みがニューラルネットワークの精度を決める

ニューラルネットワークにははじめだけ人間が重みを与えるが、そのあとは
ネットワーク地震が学習して最適な重み付けする
最適な重みとは政界との誤差を最小とする重み
誤差逆伝播（ごさぎゃくでんぱん）
　誤差を逆方向（出力層から隠れそう）に伝播（送る）している

勾配降下法（こうばいこうかほう）
　最小誤差を求めるための方法で
　ある重みxがあるとして最小誤差はグラフ的にxの右下にある。
　そのため接点xの傾きは負のため右に動かす（重み（修正量）を増やす）
　制の時は左に動かし最小誤差に近づける
　