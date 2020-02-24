# Introduction to Bioinformatics 2019/20
# 5 - Strings and Lists
from h_read import FileReader
import os


def write_to_file(filename, elements):
    try:
        # writes the elements to the file
        with open(os.path.dirname(os.path.realpath(__file__)) + '\\outputs\\' + filename, 'w') as fd:
            for line in elements:
                fd.write(line)
        return '[OK]'
    except Exception as e:
        print('Exception raised when trying to write a file; ' + str(e))
        return '[ERROR]'


if __name__ == '__main__':
    data = FileReader('dataset.txt')
    data_list = data.e_5_read()

    print(write_to_file('output_5_file.txt', data_list))
