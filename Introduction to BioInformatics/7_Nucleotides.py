# Introduction to Bioinformatics 2019/20
# 7 - Nucleotides
from h_read import FileReader


class Nucleotides:

    def __init__(self):
        self.data = FileReader('dataset.txt')
        self.data_list = self.data.e_read()
        self.A = 0
        self.C = 0
        self.G = 0
        self.T = 0

    # counts the nucleotides and
    def count_nucleotides(self):
        try:
            for nucleotide in self.data_list[0]:  # Iterate through nucleotides
                if nucleotide == 'A':
                    self.A += 1
                elif nucleotide == 'C':
                    self.C += 1
                elif nucleotide == 'G':
                    self.G += 1
                elif nucleotide == 'T':
                    self.T += 1
            return True
        except Exception as e:
            print('Exception occurred while creating the output; ' + str(e))

    def create_output(self):
        try:
            output = [self.A, self.C, self.G, self.T]
            self.data.write_to_file_7('output_7_file.txt', output)
            return '[OK]'
        except Exception as e:
            print('Exception occurred while creating the output; ' + str(e))
            return '[ERROR]'


if __name__ == '__main__':
    nc = Nucleotides()
    nc.count_nucleotides()
    print(nc.create_output())
