from SearcherExeption import SearcherException

class Searcher(object):

    def  contains(self,main_string,substring):
        result = False
        startidex = -1

        if main_string == "":
            raise SearcherException("Строка пуста")
        elif substring == "":
            raise SearcherException("Подстрока пуста")
        elif len(substring) > len(main_string):
            raise SearcherException("Длина подстроки больше длины строки")
        else:
            for i in range(len(main_string)):
                if result:
                    break
                j = 0
                while (main_string[i + j] == substring[j]):
                    if j == len(substring) - 1:
                        result = True
                        startidex = i
                        break
                    elif (i + j) >= (len(main_string) - 1):
                        break
                    else:
                        j += 1
        if result:
            return "содержит на позиции " + str(startidex)
        else:
            return "не содержит"




