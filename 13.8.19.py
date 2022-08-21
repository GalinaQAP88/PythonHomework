n=int(input("Сколько билетов вы хотите приобрести? "))
ages=[]
try:
    for i in range(n):
        print("Возраст посетителя ",i+1)
        ages.append(int(input()))
        if ages[i] > 100 or ages[i] < 0:
         raise ValueError("Ошибка! Проверьте правильно ли указан возраст...")
except ValueError as error:
    print(error)
    print("Неправильный возраст")
else:
 cost=0
 discout=0.9
 for i in range(n):
     if 18<=ages[i]<25:
         cost+=990
     elif ages[i]>=25:
         cost+=1390
 if n>=3:
     cost=discout*cost
 print("Итого стоимость билетов составляет ", int(cost), "руб.")
