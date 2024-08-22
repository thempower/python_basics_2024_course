#DONE #1. Napisz program ktory sprawdza czy podana przez uzytkownika liczba jest parzysta czy nie parzysta - Write a program which validating of provided number by user is a integer or not

# print("We will check or provided number  is a integer ")

# user_number= int(input("Please provide a number "))
# y = 2

# if user_number % y != 0:
#     print("Provided number not integer")
# else:
#     print("Provided number is integer")

#DONE#2. Napisz program ktory sprawdza czy podana przez uzytkownika liczba jest wieszka, mniejsza lub równa zero
# print("Program will check of provided number is > 0 or = 0 or < 0 ")
# number = int(input("Please provide a number you want to check "))

# if number > 0:
#     print("Provided number is > 0")
# elif number < 0:
#     print("Provided number is < 0")
# else: 
#     print("Provided number is = 0")


# #DONE #3. Napisz program ktory zapyta uzytkownika o wynik od wynik na egazminie i wyswietli konkretna ocene
# # 90 - 100 -> 5
# # 80 - 89 -> 4
# # 70 - 79 -> 3
# # 60 - 69 -> 2
# # ponizej 60 -> 1

# score = int(input("Please provide your score points "))

# if score <= 100 and score >= 90:
#     print("Your score a 5, great job congratulations!")
# elif score <= 89 and score >= 80:
#     print("Your score a 4, good job!")
# elif score <= 79 and score >= 70:
#     print("Your score is a 3, it's a avarage scores ")
# elif score <= 69 and score >= 60:
#     print("Your score is a 2, it's could be better ")
# elif score < 60 and score >=  1:
#     print("Unfotunately you have not passed, try again ")
# else:
#     print("error, please provide a valid value")


#DONE#4 Napisz program ktory wyswietli liczby od 0 do 100

# number = 0

# while number <= 100:
#     print(number)           
#     number += 1

#DONE#5 Napisz program ktory wyswietli wszystkie liczby pierwsze od 1 do 100

# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# for num in range(101):
#     if is_prime(num):
#         print(num)


#6 Napisz program ktory wyswietli sume wszystkich liczb parzystych z przedzialu 1 - 100

# Inicjalizacja zmiennej przechowującej sumę liczb parzystych
sum_even = 0

# Pętla iterująca przez liczby od 1 do 100
for num in range(1, 101):
    if num % 2 == 0:  # Sprawdzenie, czy liczba jest parzysta
        sum_even += num  # Dodanie liczby parzystej do sumy

# Wyświetlenie wyniku
print("Suma wszystkich liczb parzystych z przedziału 1-100 wynosi:", sum_even)
    
#jezeli jest parzysta to dodac ja do sumy


#7 Napisz program ktory policzy pole prostokata (uzytkownik mus podac dlugosci bokow)
#8 Napisz program ktory sprawdzi czy podane imie jest imieniem meskim, czy zenskim(zaloz ze imiona zenskie koncza sie na litere a)
#9 Pobierz od uzytkownika 3 liczby calkowite i uporzadku jej w kolejnosc od najmniejsze do najwiekszej
#10 Stworz gre w ktorej wylosuje liczbe z przedzialu 1-100 zapisze te liczbe w  zmiennej, a nastepnie poprosis uzytkownika o odgadniecie tej liczby. 
#po kazdej proble wyswietlaj czy podana liczba jest mnieejsza czy wieksza od wylosowanej
#Gdy uzytkownik odgadnie liczbe zakoncz gre
#Znajdz informacje w jaki sposob losowac liczby calkowite w pythonie