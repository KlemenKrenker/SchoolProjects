# Introduction to Bioinformatics 2019/20
# 9 - Complementing a Strand of DNA

from h_read import FileReader


class DNA:
    def __init__(self, dna_string):
        self.dna_string = dna_string
        self.dna_complement = ''

    # returns the reverse complement of dna_string
    def complement(self):
        try:
            for nucleotide in reversed(self.dna_string):
                if nucleotide == 'A':
                    self.dna_complement += 'T'
                elif nucleotide == 'T':
                    self.dna_complement += 'A'
                elif nucleotide == 'C':
                    self.dna_complement += 'G'
                elif nucleotide == 'G':
                    self.dna_complement += 'C'
                else:
                    print('[ERROR]')
            return self.dna_complement
        except Exception as e:
            print('[ERROR] - exception raised in complement; ' + str(e))
            return 'ERROR'


if __name__ == '__main__':
    data = FileReader('dataset.txt')
    data_list = data.e_read()

    cmp = DNA(data_list[0])
    print(cmp.complement())
