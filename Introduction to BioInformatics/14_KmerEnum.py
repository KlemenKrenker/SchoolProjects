# Introduction to Bioinformatics 2019/20
# 14 - Enumerating k-mers Lexicographically

from h_read import FileReader
from Bio import SeqIO
from itertools import product


class KmerEnumerator:
    def __init__(self, symbols, length):
        self.symbols = symbols.replace(' ', '')
        self.length = int(length)

    def create_enumerations(self):
        for _set in product(list(self.symbols), repeat=self.length):
            perm = ''.join(_set)
            print(perm)


if __name__ == '__main__':
    data = FileReader('dataset.txt')
    data_list = data.e_14_read()

    ke = KmerEnumerator(data_list[0], data_list[1])
    ke.create_enumerations()
