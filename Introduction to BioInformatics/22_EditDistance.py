# Introduction to Bioinformatics 2019/20
# 13 - k-Mer Composition

# from h_read import FileReader
from Bio import SeqIO


class EditDistance:
    sequences = []

    def __init__(self, dataset):
        self.d_mat = None
        fasta_sequences = SeqIO.parse(open(dataset), 'fasta')
        for fasta in fasta_sequences:
            name, sequence = fasta.id, str(fasta.seq)
            self.sequences.append(sequence)
        self.sequence_s = self.sequences[0]
        self.sequence_t = self.sequences[1]

        self.compute_distance()

    def display_d_mat(self):
        for x in range(0, len(self.d_mat)):
            print(self.d_mat[x])
        print('\n')

    def display_d_mat_ind(self):
        for i in range(0, len(self.d_mat)):
            line = ''
            for j in range(0, len(self.d_mat[i])):
                line += str(i) + ':' + str(j) + ' '
            print(line)
        print('\n')

    def prepare_d_mat(self):
        self.d_mat[0][0] = 0

        for i in range(1, len(self.d_mat)):
            for j in range(0, len(self.d_mat[i])):
                if j == 0:  # downward 0 line -2
                    self.d_mat[i][j] = self.d_mat[i - 1][j] - 2

        for i in range(0, len(self.d_mat)):
            for j in range(1, len(self.d_mat[i])):
                if i == 0:  # horizontal 0 line -2
                    self.d_mat[i][j] = self.d_mat[i][j - 1] - 2

    def compute_distance(self):
        try:
            len_s = len(self.sequence_s) + 1
            len_t = len(self.sequence_t) + 1

            if len_s > len_t:  # s > t, append to t
                for x in range(0, len_s - len_t):
                    self.sequence_t += '*'
            else:  # t > s, append to s
                for x in range(0, len_t - len_s):
                    self.sequence_s += '*'

            self.d_mat = []
            for i in range(0, len_t):
                m_temp = []
                for j in range(0, len_s):
                    m_temp.append(0)
                self.d_mat.append(m_temp)

            self.prepare_d_mat()
            self.display_d_mat()
            print(self.sequence_t)
            print(self.sequence_s)

            # t - downward
            # s - horizontal
            for i in range(1, len(self.d_mat)):
                for j in range(1, len(self.d_mat[i])):
                    if self.sequence_t[i-1] == self.sequence_s[j-1]:  # diagonal check, equal
                        score = 2
                    else:  # not equal
                        score = -1
                    #                       DIAGONAL                    DOWNWARD                    HORIZONTAL
                    self.d_mat[i][j] = max(self.d_mat[i-1][j-1] + score, self.d_mat[i-1][j] - 2, self.d_mat[i][j-1] - 2)

            self.display_d_mat()
            self.display_d_mat_ind()
        except Exception as e:
            print('[ERROR]: exception raised in compute_distance;', str(e))


if __name__ == '__main__':
    ed = EditDistance('dataset.txt')

# >Rosalind_43
# PRETTY
# >Rosalind_97
# PRTTEIN

# >Rosalind_43
# Saturday
# >Rosalind_97
# Sunday