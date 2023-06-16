class Pokemon():
    def __init__(self, name, level, kind, exp):
        self.name = name
        self.level = level
        self.kind = kind
        self.exp = exp

pikachu = Pokemon('ピカチュウ',15,'でんきねずみ',790)
print(pikachu.name)
print('Lv' + str(pikachu.level))
print(pikachu.kind + 'ポケモン')
print('経験値：' + str(pikachu.exp))

# print('\n')

achamo = Pokemon('アチャモ',3,'ひよこ',300)
print(achamo.name)
print('Lv' + str(achamo.level))
print(achamo.kind + 'ポケモン')
print('経験値：' + str(achamo.exp))