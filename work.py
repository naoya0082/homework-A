# A-1 文字列のリスト
users = ["Bob", "Tom", "Ken"]

# A-2 整数のリスト
int_numbers = [1, 2, 3, 4, 5]

# A-3 要素のデータが異なるリスト
kazuma_info = ["Kazuma", "Takahashi", 35]

# A-4 要素へのアクセス
# Kazuma Makoto を出力
members = ["Kazuma", "Makoto", "Ohira"]
print(members[0])
print(members[1])

# A-5 要素へのアクセスとフォーマット
# "Name: Takahashi Kazuma, Age: 35"と出力
kazuma_info = ["Kazuma", "Takahashi", 35]
print(f"Name: {kazuma_info[1]} {kazuma_info[0]}, Age: {kazuma_info[2]}")
