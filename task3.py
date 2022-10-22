def delete(list_, index=None):
    ...  # TODO реализовать функцию удаления элемента из списка по индексу
    if index == None:
        list_ = list_[: -1]
        print(list_)
    else:
        list_ = list_[: index] + list_[index + 1 :]
        print(list_)
    return

(delete([0, 0, 1, 2], index=0))  # [0, 1]
(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
