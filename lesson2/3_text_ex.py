# 各月の売上を書いたsales.txtがあります。
# これを読み込み、
# 1. 売上の合計
# 2. 黒字(0以上)の合計
# 3. 赤字(0より下)の合計
# を求めるプログラムを作成しましょう。

# 1つのファイルの中に、全て書きましょう。

# ベタ書きする場合
# with open('lesson2/sales.txt', 'r', encoding='utf-8') as sales:
#     all_sales = 0
#     surplus = 0
#     deficit = 0
#     for line in sales:
#         all_sales += int(line)
#         if int(line) > 0:
#             surplus += int(line)
#         if int(line) < 0:
#             deficit += int(line)
#     print(all_sales, surplus, deficit)

def get_total_sales(txt):
    with open(txt, 'r', encoding='utf-8') as sales:
        total_sales = 0
        for line in sales:
            total_sales += int(line)
        return total_sales

def get_total_surplus(txt):
    with open(txt, 'r', encoding='utf-8') as sales:
        surplus = 0
        # deficit = 0
        for line in sales:
            if int(line) > 0:
                surplus += int(line)
            # if int(line) < 0:
            #     deficit += int(line)
        return surplus

def get_total_deficit(txt):
    with open(txt, 'r', encoding='utf-8') as sales:
        deficit = 0
        for line in sales:
            if int(line) < 0:
                deficit += int(line)
        return deficit

total_sales = get_total_sales('lesson2/sales.txt')
total_surplus = get_total_surplus('lesson2/sales.txt')
total_deficit = get_total_deficit('lesson2/sales.txt')
print(total_sales, total_surplus, total_deficit)

'''
複数行文字列をコメントアウト代わりに使うこともある
'''