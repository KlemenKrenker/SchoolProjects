# Introduction to Bioinformatics 2019/20
# 8 - Treanscribing DNA into RNA

from h_read import FileReader


class RNA:
    def __init__(self, dna_string):
        self.dna_string = dna_string
        self.rna_string = ''

    # transcribes - replaces T with U
    def transcribe(self):
        for nucleotide in self.dna_string:
            if nucleotide == 'T':
                self.rna_string += 'U'
            else:
                self.rna_string += nucleotide
        return self.rna_string


if __name__ == '__main__':
    data = FileReader('dataset.txt')
    data_list = data.e_read()

    rna = RNA(data_list[0])
    print(rna.transcribe())
