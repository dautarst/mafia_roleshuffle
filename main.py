import random
#Игроки и роли, добавление доп ролей
amount_players = int(input("Сколько игроков за столом?: "))
amount_mafia = int(input("Сколько черных игроков?: "))
amount_role = int(input("Какие роли помимо стандартных (докто/комиссар/мафия/мирные)?: "))
#Список игроков, число берем из прошлого инпута
players = list(range(1, amount_players + 1))
random.shuffle(players)
new_role=[]
#Рандом выбор мафии
mafia = [players.pop() for x in range(amount_mafia)]
#Доктор 
doctor = players.pop()
#Коммиссар
komissar = players.pop()
#Выбор игрока с новой(ыми) ролями
for roles in range(amount_role):
    role=input("Название дополнительной роли:")
    new_role.append(role)
    if amount_players-4<len(new_role):
        print("Недопустимое количество игроков!")
print("Количество новых ролей:", len(new_role))
random.shuffle(new_role)
random.shuffle(players)
for z in range(len(new_role)):
    print("Игроком с ролью" , new_role.pop() , "является:", players.pop())
#Красные игроки
civilians = players
#Раздача стола
print("Мафией(ями) являются игроки:", *mafia)
print("Доктором является игрок:", doctor)
print("Коммиссаром является игрок:", komissar)
print("Мирные жители :", *civilians)
#таймер на ожидание инпута
time=input()