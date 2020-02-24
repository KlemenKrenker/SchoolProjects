# Introduction to Bioinformatics 2019/20
# 12 - Finding a Motif in DNA

from h_read import FileReader
# from Bio import SeqIO


class Motif:
    def __init__(self, dna_sequence, substring):
        self.dna_sequence = dna_sequence
        self.substring = substring
        self.sub_occ = []

    # returns a list of occ
    def get_occ(self):
        for x in range(0, len(self.dna_sequence) - len(self.substring) + 1):
            if self.dna_sequence[x:x+len(self.substring)] == self.substring:
                self.sub_occ.append(x+1)
        return self.sub_occ


if __name__ == '__main__':
    data = FileReader('dataset.txt')
    data_list = data.e_read()

    mm = Motif(data_list[0], data_list[1])
    sub_occ = mm.get_occ()

    print(*sub_occ, sep=' ')
