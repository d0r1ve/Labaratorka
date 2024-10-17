n1= int(input("введите первое число: "))
n2= int(input("введите первое число: "))
task=input("введите желаемую операцию: ")
if task=="-":
    print(f"ответ:{n2-n1}")
elif task=="+":
    print(f"ответ:{n2+n1}")
elif task=="/":
    print(f"ответ:{n2/n1}")
elif task=="*":
    print(f"ответ:{n2*n1}")