# Introduction to Bioinformatics 2019/20
# 6 - Dictionaries
from h_read import FileReader


class WordCount:

    def __init__(self):
        self.data = FileReader('dataset.txt')
        self.data_list = self.data.e_read()
        self.word_dict = {}

    def create_dictionary(self):
        try:
            for element in self.data_list:
                if element in self.word_dict:
                    self.word_dict.update({element: self.word_dict[element]+1})
                else:
                    self.word_dict.update({element: 1})
            return True
        except Exception as e:
            print('Exception occurred while creating the dictionary; ' + str(e))
            return False

    def create_output(self):
        try:
            output = []

            for element in self.word_dict:  # iterate through dictionary
                output.append(element + ' ' + str(self.word_dict[element]) + '\n')

            self.data.write_to_file('output_6_file.txt', output)
            return '[OK]'
        except Exception as e:
            print('Exception occurred while creating the output; ' + str(e))
            return '[ERROR]'


if __name__ == '__main__':
    wc = WordCount()
    wc.create_dictionary()
    print(wc.create_output())
