# Introduction to Bioinformatics 2019/20
# 4 - Conditions and loops
from h_read import FileReader


def get_odd_integers(a, b):
    sum_value = 0
    while a <= b:
        if a % 2 != 0:
            sum_value += a
        a += 1
    return sum_value


if __name__ == '__main__':
    data = FileReader('dataset.txt')
    data_list = data.e_read()

    print(get_odd_integers(int(data_list[0]), int(data_list[1])))
