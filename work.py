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

# A-6 forによるループその1
odd_numbers = [1, 3, 5, 7, 9]
for loop in odd_numbers:
    print(loop)

# A-7 forによるループその2
even_numbers = [2, 4, 6, 8]
for loop2 in even_numbers:
    print(loop2 * 2)
