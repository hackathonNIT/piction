# Piction  
  
# 機能  
画像からエッジを検出し、関数で表現します。

## インストール
```
$pip install piction
```

# 使い方

## def getPoint(image,maxPointNum=0):  
	画像をエッジ処理し、各点を取得して、連結している順番に出力する。
	maxPointNumに値を与えるとその数を上限にして点を返す。
	戻り値はx,yの1次元配列。      

## def getPointArray(image,maxPointNum=0):  
	getPoint関数の繋がりごとに分けて配列で返す。  
	戻り値はx,yの2次元配列。      

## def getSinRegression(X,Y1):
	1次元配列のx,yを与えることで回帰する。  
	戻り値はx,yの回帰後のもの。

## def getSinRegressionArray(X,Y):
	2次元配列のx,yを与えることで回帰する。  
	戻り値はx,yの回帰後のもの。

## def WriteFunc1():
	回帰を行った後の関数を文字列で出力する。  

# サンプルアプリ  
実行方法
```
$streamlit run ex_app/app.py
```

