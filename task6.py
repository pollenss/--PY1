list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_element = list_numbers[0]
index = 0
for i in range(len(list_numbers)):
    if list_numbers[i] > max_element:
        max_element = list_numbers[i]
        index = i
a = list_numbers[19]
list_numbers[index] = a
list_numbers[19] = max_element
print(list_numbers)
