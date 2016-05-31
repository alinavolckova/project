from Searcher import Searcher

search = Searcher()

for i in range(5):
    print("Введите выражения: ")
    expression1 = input()
    expression2 = input()
    try:
        print("Результат: " + search.contains(expression1,expression2).__str__())

    except Exception as exeption:
        print("Ошибка " + exeption.__str__())


