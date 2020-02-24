# Introduction to Bioinformatics 2019/20
# 27 - Compute the Probability of a Hidden Path

from h_read import FileReader
# from Bio import SeqIO


class HiddenPath:
    def __init__(self, dataset):
        with open(dataset) as fd:
            self.sequence = fd.readline()
            fd.readline()
            fd.readline()
            fd.readline()
            fd.readline()
            line = fd.readline().replace('\n', '')
            a_row = line.split('\t')
            line = fd.readline().replace('\n', '')
            b_row = line.split('\t')
            self.prob_matrix = []
            self.prob_matrix.append(a_row[1:])
            self.prob_matrix.append(b_row[1:])

    def compute_pathprobability(self):
        print(self.sequence)
        print(self.prob_matrix)
        probability = 0.5
        for x in range(0, len(self.sequence)-1):
            if self.sequence[x] == 'A':  # we are in A
                if self.sequence[x + 1] == 'A':   # next state is A
                    probability = probability * float(self.prob_matrix[0][0])
                elif self.sequence[x + 1] == 'B':  # next state is B
                    probability = probability * float(self.prob_matrix[0][1])
            elif self.sequence[x] == 'B':  # we are in B
                if self.sequence[x + 1] == 'A':   # next state is A
                    probability = probability * float(self.prob_matrix[1][0])
                elif self.sequence[x + 1] == 'B':  # next state is B
                    probability = probability * float(self.prob_matrix[1][1])
        print(probability)


if __name__ == '__main__':
    hp = HiddenPath('dataset.txt')
    hp.compute_pathprobability()