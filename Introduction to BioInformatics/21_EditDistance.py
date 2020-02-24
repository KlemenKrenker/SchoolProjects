# Introduction to Bioinformatics 2019/20
# 13 - k-Mer Composition

# from h_read import FileReader
from Bio import SeqIO


class EditDistance:
    sequences = []
    sequence_a = None
    sequence_b = None

    distances = None

    def __init__(self, dataset):
        fasta_sequences = SeqIO.parse(open(dataset), 'fasta')
        for fasta in fasta_sequences:
            name, sequence = fasta.id, str(fasta.seq)
            self.sequences.append(sequence)
        self.sequence_a = self.sequences[0]
        self.sequence_b = self.sequences[1]

        self.compute_distance()
        print(self.distances)
        print(self.distances[-1])

    def compute_distance(self):
        try:
            if len(self.sequence_a) > len(self.sequence_b):
                self.sequence_a, self.sequence_b = self.sequence_b, self.sequence_a

            self.distances = range(len(self.sequence_a) + 1)
            for i2, c2 in enumerate(self.sequence_b):
                h_distances = [i2 + 1]
                for i1, c1 in enumerate(self.sequence_a):
                    if c1 == c2:
                        h_distances.append(self.distances[i1])
                    else:
                        h_distances.append(1 + min((self.distances[i1], self.distances[i1 + 1], h_distances[-1])))
                self.distances = h_distances
        except Exception as e:
            print('[ERROR]: exception raised in compute_distance;', str(e))


if __name__ == '__main__':
    ed = EditDistance('dataset.txt')