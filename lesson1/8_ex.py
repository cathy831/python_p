# 1から100までfor文で繰り返し、
# 3の倍数のときは「Fizz」
# 5の倍数のときは「Buzz」
# 15の倍数のときは「FizzBuzz」
# それ以外は数値を表示するプログラムを作りましょう

for i in range(1,101):
    if i%15 == 0:
        print('FizzBuzz')
    elif i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print('Buzz')
    else:
        print(i)



# 1から100まで繰り返し、素数の数値を表示するプログラムを作成しましょう

for i in range(2, 101):
# 1~100までの数字を抽出
    for j in range(2, i):
        if i % j == 0:
        # 抽出されたそれぞれの数字iをj(2~iの1個手前の数字まで)で割り算するfor文
            break
            # 2~(i-1)で割り切れてしまったiは素数じゃないのでbreakで抜けて次のiをjで割る作業に移る
    else:
        print(i)
        # 2~(i-1)で割り切れなかったiは素数なので出力する