# Introduction to Bioinformatics 2019/20
# 10 - Computing GC Content

# from h_read import FileReader
from Bio import SeqIO


class GC:
    def __init__(self, filename):
        self.gc_content = []
        self.sequences = []
        fasta_sequences = SeqIO.parse(open(filename), 'fasta')
        for fasta in fasta_sequences:
            name, sequence = fasta.id, str(fasta.seq)
            self.sequences.append((name, sequence))

    def compute_gc(self):
        for sequence in self.sequences:
            cg_content = 0
            for nucleotide in sequence[1]:
                if nucleotide == 'C' or nucleotide == 'G':
                    cg_content += 1

            self.gc_content.append((sequence[0], round((cg_content/len(sequence[1])*100), 6)))
        return self.gc_content


if __name__ == '__main__':
    # data = FileReader('dataset.txt')
    # data_list = data.e_read()

    # print(data_list)
    gc = GC('dataset.txt')
    gc_content = gc.compute_gc()
    for sequence in gc_content:
        print(sequence[0])
        print(sequence[1])
