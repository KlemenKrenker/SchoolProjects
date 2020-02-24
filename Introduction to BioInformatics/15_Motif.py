# Introduction to Bioinformatics 2019/20
# 15 - Finding a Motif in DNA

# from h_read import FileReader
from Bio import SeqIO


class Motif:
    def __init__(self, filename):
        self.failure_array = []
        fasta_sequences = SeqIO.parse(open(filename), 'fasta')
        for fasta in fasta_sequences:
            name, self.sequence = fasta.id, str(fasta.seq)
        for x in range(0, len(self.sequence)):
            self.failure_array.append(0)

    def compute_farray(self):
        x = 0
        for i in range(2, len(self.sequence) + 1):
            while x > 0 and self.sequence[x] != self.sequence[i - 1]:
                x = self.failure_array[x - 1]
            if self.sequence[x] == self.sequence[i - 1]:
                x += 1
            self.failure_array[i - 1] = x
        print(*self.failure_array, sep=' ')


if __name__ == '__main__':
    mm = Motif('dataset.txt')
    mm.compute_farray()
