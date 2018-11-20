# A-1 文字列のリスト
users = ["Bob", "Tom", "Ken"]

# A-2 整数のリスト
int_numbers = [1, 2, 3, 4, 5]

# A-3 要素のデータが異なるリスト
kazuma_info = ["Kazuma", "Takahashi", 35]

print("--------------A-4--------------")

# A-4 要素へのアクセス
# Kazuma Makoto を出力
members = ["Kazuma", "Makoto", "Ohira"]
print(members[0])
print(members[1])

print("--------------A-5--------------")

# A-5 要素へのアクセスとフォーマット
# "Name: Takahashi Kazuma, Age: 35"と出力
kazuma_info = ["Kazuma", "Takahashi", 35]
print(f"Name: {kazuma_info[1]} {kazuma_info[0]}, Age: {kazuma_info[2]}")

print("--------------A-6--------------")

# A-6 forによるループその1
odd_numbers = [1, 3, 5, 7, 9]
for loop in odd_numbers:
    print(loop)

print("--------------A-7--------------")

# A-7 forによるループその2
even_numbers = [2, 4, 6, 8]
for loop2 in even_numbers:
    print(loop2 * 2)

print("--------------A-8--------------")

# A-8 リストを要素に持つリスト
# 以下を出力
# "Name: Kazuma, Age: 35"
# "Name: Tom, Age: 57"
# "Name: Bob, Age: 77"
users_info = [["Kazuma", 35],
              ["Tom", 57],
              ["Bob", 77]]
print(f"Name: {users_info[0][0]}, Age: {users_info[0][1]}")
print(f"Name: {users_info[1][0]}, Age: {users_info[1][1]}")
print(f"Name: {users_info[2][0]}, Age: {users_info[2][1]}")
