num = int(input("inputnum :"))

if num % 3 == 0 and num % 7 != 0:
    print(f"{num} 은 3의 배수")
elif num % 3 != 0 and num % 7 == 0:
    print(f"{num} 은 7의 배수")
elif num % 3 == 0 and num % 7 == 0:
    print(f"{num} 은 3과 7의 배수")
else:
    print(f"{num} 은 3과 7의 배수가 아님")
