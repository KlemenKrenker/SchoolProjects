# Introduction to Bioinformatics 2019/20
# 13 - k-Mer Composition

# from h_read import FileReader
from Bio import SeqIO
from itertools import product


class Kmer:
    def __init__(self, filename):
        self.gc_content = []
        self.sequences = []
        self.permutations = {}
        fasta_sequences = SeqIO.parse(open(filename), 'fasta')
        for fasta in fasta_sequences:
            name, sequence = fasta.id, str(fasta.seq)
            self.sequences.append((name, sequence))

    def create_dict(self):
        for _set in product(list('ACGT'), repeat=4):
            perm = ''.join(_set)
            if perm in self.permutations:
                self.permutations.update({perm: self.permutations[perm] + 1})
            else:
                self.permutations.update({perm: 0})

    def compute_kmer(self, k):
        for x in range(0, len(self.sequences[0][1]) - k + 1, 1):
            kmer = self.sequences[0][1][x:x+k]
            if kmer in self.permutations:
                self.permutations.update({kmer: self.permutations[kmer] + 1})

        ret_list = []
        for kmer in self.permutations:
            ret_list.append(self.permutations[kmer])
        return ret_list


if __name__ == '__main__':
    # data = FileReader('dataset.txt')
    # data_list = data.e_read()

    # print(data_list)
    gc = Kmer('dataset.txt')
    gc.create_dict()
    print(*gc.compute_kmer(4), sep=' ')

