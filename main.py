n =int(input("Введите числа: ")) 
sum = 0 
while n > 0:
    d = n % 10 
    n = n // 10 
    sum += d 
print('Сумма всх чисел =',sum)
print("добавили восьмую строчку")