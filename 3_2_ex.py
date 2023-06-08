# 組み込み関数input()はユーザーの入力を表示してくれる
user_input = input()
print('「こんにちは、' + user_input + '」')

# ↓ 変数に入れ込む形でもいける
# user_input = input()
# result = '「こんにちは、' + user_input + '」'
# print(result)

# 最新の書き方
# user_input = input()
# result = f'「こんにちは、{user_input}'
# print(result)

# ちょっと古い書き方
# formatで、変数を埋め込める
# 'こんにちは、{}'.format(user_input)