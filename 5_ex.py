# ex1  7を消す
data_list = [1, 2, [3, 4, 5], [6, 7], 8, 9, [10, 11]]
print(data_list[3][1])


# ex2  空配列にinputで追加してソート
number_list = []

user_input_number1 = input()
user_input_number2 = input()
user_input_number3 = input()

number_list.append(user_input_number1)
number_list.append(user_input_number2)
number_list.append(user_input_number3)

number_list.sort()

print(number_list)


# ex3  空配列にinputで追加してソート(insert版)
number_list = []

user_input_number1 = input()
user_input_number2 = input()
user_input_number3 = input()

number_list.insert(0,user_input_number1)
number_list.insert(2,user_input_number2)
number_list.insert(1,user_input_number3)

number_list.sort(reverse=True)

print(number_list)


# ex4  文字列化とリスト化
user_file_text = """
hoge
fuga
taro
ziro
saburo
"""

user_file_list = user_file_text.split('\n')

del user_file_list[0]
del user_file_list[5]
print(user_file_list)

user_file_list.sort()
print(user_file_list)

new_text = '\n'.join(user_file_list)
print(new_text)