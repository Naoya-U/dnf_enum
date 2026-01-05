「論理関数の各入力パターンに対する出力」を入力として、その論理関数の非冗長積和形を列挙したものを出力します。

# 使用例
次のような4変数の論理関数fを考えます。
| a | b | c | d | f |
|---|---|---|---|---|
|0|0|0|0|1|
|0|0|0|1|0|
|0|0|1|0|0|
|0|0|1|1|1|
|0|1|0|0|1|
|0|1|0|1|1|
|0|1|1|0|1|
|0|1|1|1|1|
|1|0|0|0|1|
|1|0|0|1|1|
|1|0|1|0|1|
|1|0|1|1|1|
|1|1|0|0|0|
|1|1|0|1|1|
|1|1|1|0|1|
|1|1|1|1|0|

この時、変数の個数と出力を(a,b,c,d) = (0,0,0,0)から(1,1,1,1)まで順に並べたものを入力することでfの非冗長積和形を列挙します。
```
変数の個数を入力: 4
出力を順に入力: 1001111111110110
a'b + ac'd + acd' + b'c'd' + b'cd
a'c'd' + a'cd + ab' + bc'd + bcd'
a'b + a'c'd' + a'cd + ab' + ac'd + acd'
a'b + a'c'd' + a'cd + ab' + ac'd + bcd'
a'b + a'c'd' + a'cd + ab' + acd' + bc'd
a'b + a'c'd' + ab' + ac'd + acd' + b'cd
a'b + a'c'd' + ab' + ac'd + b'cd + bcd'
a'b + a'c'd' + ab' + acd' + b'cd + bc'd
a'b + a'c'd' + ab' + b'cd + bc'd + bcd'
a'b + a'cd + ab' + ac'd + acd' + b'c'd'
a'b + a'cd + ab' + ac'd + b'c'd' + bcd'
a'b + a'cd + ab' + acd' + b'c'd' + bc'd
a'b + a'cd + ab' + b'c'd' + bc'd + bcd'
a'b + ab' + ac'd + b'c'd' + b'cd + bcd'
a'b + ab' + acd' + b'c'd' + b'cd + bc'd
a'b + ab' + b'c'd' + b'cd + bc'd + bcd'
a'c'd' + a'cd + ac'd + acd' + b'c'd' + b'cd + bc'd + bcd'
```
