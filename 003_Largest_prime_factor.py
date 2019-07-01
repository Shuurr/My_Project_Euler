"""Проект Эйлера.
Задача 3. Наибольший простой делитель.

Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?"""

import math

print('\nПроект Эйлера. Задача 3. Наибольший простой делитель.')
print('\nПростые делители числа 13195 - это 5, 7, 13 и 29.\
 Каков самый большой делитель числа 600851475143, являющийся простым числом?')

def isPrime(limit):
	"""Метод определения простоты числа.

	Функция получает число n и возвращает True если n - простое число.
	Определение простоты производится на основании построения решета Аткина от 2 до limit."""

	results = [2, 3, 5]
	sieve = [False] * (limit + 1) 
	factor = int(math.sqrt(limit)) + 1
	for i in range(1, factor):
		for j in range(1, factor):
			n = 4 * i ** 2 + j ** 2
			if (n <= limit) and (n % 12 == 1 or n % 12 == 5):
				sieve[n] = not sieve[n]
			n = 3 * i ** 2 + j ** 2
			if (n <= limit) and (n % 12 == 7):
				sieve[n] = not sieve[n]
			if i > j:
				n = 3 * i ** 2 - j ** 2
				if (n <= limit) and (n % 12 == 11):
					sieve[n] = not sieve[n]
	for index in range(5, factor):
		if sieve[index]:
			for jndex in range(index ** 2, limit, index ** 2):
				sieve[jndex] = False
	for index in range(7, limit + 1):
		if sieve[index]:
			results.append(index)

	if results[-1] == limit:
		return True
	else:
		return False

N = int(input()) # Заданный диапазон поиска простых чисел
k = 2 # Коэффициент уменьшения проверочной переменной по ходу цикла
check = int(N // k) # Проверочная переменная
ans = False # Переменная наличия ответа задачи

print('\nЗаданное число N =', N)

while not ans:
	if N % check == 0:
		print('check =', check)
		print('N / check =', N / check)
		if isPrime(check):
			print('Наибольший простой делитель числа N составлет', check)
			ans = True
			break
	k += 1
	check = int(N // k)
	if k == N:
		print('Число N - простое число. Решений нет.')
		break
