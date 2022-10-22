def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_
    new_lower_str_ = str_.lower()
    new_lower_sym_str_ = "".join(sym for sym in new_lower_str_ if sym.isalpha())
    sym_dictionary = {}
    for sym in new_lower_sym_str_:
        if sym in sym_dictionary:
            sym_dictionary[sym] += 1
        else:
            sym_dictionary[sym] = 1
    print(sym_dictionary)
    return
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
get_count_char(main_str)

