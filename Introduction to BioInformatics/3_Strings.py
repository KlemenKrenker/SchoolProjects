# Introduction to Bioinformatics 2019/20
# 3 - Strings and Lists
from h_read import FileReader


def get_words(input_string, x_1_start, x_1_end, x_2_start, x_2_end):
    return input_string[x_1_start:x_1_end+1] + ' ' + input_string[x_2_start:x_2_end+1]


if __name__ == '__main__':
    data = FileReader('dataset.txt')
    data_list = data.e_read()

    sample_text = data_list[0]
    a = int(data_list[1])
    b = int(data_list[2])
    c = int(data_list[3])
    d = int(data_list[4])

    print(get_words(sample_text, a, b, c, d))
