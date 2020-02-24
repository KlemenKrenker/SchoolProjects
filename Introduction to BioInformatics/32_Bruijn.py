# Introduction to Bioinformatics 2019/20
# 32 - Constructing a De Bruijn Graph

from h_read import FileReader
# from Bio import SeqIO
import numpy as np
import operator
import copy


class Bruijn:
    def __init__(self, dataset):
        self.sequences = []
        self.f_lst = []
        with open(dataset) as fd:
            self.sequences = fd.readlines()

        for seq_id in range(0, len(self.sequences)):
            self.sequences[seq_id] = self.sequences[seq_id].replace('\n', '')

        # print(self.sequences)

    # Reg(L, R), Comp(R, L)
    def compute_graph(self):
        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        k = len(self.sequences[0]) - 1
        for x in range(0, len(self.sequences)):
            # print(self.sequences[x])
            t_n_lst = []
            t_c_lst = []
            for a in range(0, len(self.sequences[x]) - k + 1):
                t_n_lst.append(self.sequences[x][a:a + k])
                t_c_lst.append("".join(complement.get(base, base) for base in reversed(self.sequences[x][a:a + k])))

            tmp = t_c_lst[0]
            t_c_lst[0] = t_c_lst[1]
            t_c_lst[1] = tmp

            self.f_lst.append(t_n_lst)
            self.f_lst.append(t_c_lst)

            self.f_lst = sorted(self.f_lst)

        tmp_list = []
        for x in self.f_lst:
            if x not in tmp_list:
                tmp_list.append(x)

        self.f_lst = tmp_list
        # print(self.f_lst)

        for x in range(0, len(self.f_lst)):
            row = '('
            for a in range(0, len(self.f_lst[x])):
                row += self.f_lst[x][a]
                if a == 0:
                    row += ', '
            row += ')'
            print(row)


if __name__ == '__main__':
    b = Bruijn('dataset.txt')
    b.compute_graph()
