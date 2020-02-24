# Introduction to Bioinformatics 2019/20
# 2 - Variables and Some Arithmetic
from math import pow
from h_read import FileReader


# returns hypotenuse value (type: int)
def hypotenuse(a, b):
    return int(pow(a, 2) + pow(b, 2))


if __name__ == '__main__':
    data = FileReader('dataset.txt')
    data_list = data.e_read()

    print(hypotenuse(int(data_list[0]), int(data_list[1])))
