# Introduction to Bioinformatics 2019/20
# 29 - Implement the Viterbi Algorithm

# from h_read import FileReader
# from Bio import SeqIO
import numpy as np
import operator
import copy


class Viterbi:
    def __init__(self, dataset):
        self.transition_prob = []
        self.em_prob = []
        self.sequence = None
        self.row_count = None
        self.column_count = None
        self.read_file(dataset)

    def read_file(self, dataset):
        with open(dataset) as fd:
            self.sequence = fd.readline().replace('\n', '')
            fd.readline()
            self.column_count = len(fd.readline().replace('\n', '').split('   '))  # xyz
            fd.readline()
            self.row_count = len(fd.readline().replace('\n', '').split('   '))  # ABC
            fd.readline()
            fd.readline()
            for x in range(0, self.row_count):
                self.transition_prob.append(fd.readline().replace('\n', '').split('\t')[1:])
            fd.readline()
            fd.readline()

            for x in range(0, self.row_count):
                self.em_prob.append(fd.readline().replace('\n', '').split('\t')[1:])

            for x in range(0, len(self.transition_prob)):
                for y in range(0, len(self.transition_prob[x])):
                    self.transition_prob[x][y] = float(self.transition_prob[x][y])

            print(self.em_prob)
            for x in range(0, len(self.em_prob)):
                for y in range(0, len(self.em_prob[x])):
                    self.em_prob[x][y] = float(self.em_prob[x][y])

        print(self.sequence)
        print(self.transition_prob)
        print(self.em_prob)
        print('\n')

    def viterbi(self):
        for x in range(0, len(self.sequence) - 1):
            print(self.sequence[x])


if __name__ == '__main__':
    v = Viterbi('dataset.txt')
    v.viterbi()
