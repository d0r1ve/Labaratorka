import random
num = random.randint(1,10)
for i in range(3):
    n=int(input("введите случайное число от 1 до 10: "))
    if n==num:
        print("вы угадали!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        exit()
    print("вы не угадали")
print("попытки закончились")
