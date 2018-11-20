print("--------------A-11-------------")
# A-11 BMIアプリ
# 身長(m)と体重(kg)を入力として受け取りBMIを計算するアプリを実装してください
# 小数点第2位まで表示すること
height = float(input("身長を入力してください(cm)>> "))
weight = float(input("体重を入力してください(kg)>> "))
bmi = "%.2f" % (weight / (height * height / 10000))

print(f"あなたのBMIは【{bmi}】です")
