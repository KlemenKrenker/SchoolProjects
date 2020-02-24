# Mini project #1: Where are the Genes

# Implement a gene-finding algorithm that examines open reading frames and finds subsequences that span from the
# start codon to the stop codon. Use the full genome of the Mycoplasma genitalium (NCBI ID is NC_000908) to
# find gene candidates. Notice that for this organism the stop codons are only TAA and TAG. Filter out the genes
# that are too short and contain only, say, L codons, and compare your candidate genes to the genes that are
# reported in the annotated genome. For comparison, computer recall and precision, and report on the dependence
# of these two accuracy scores  on the length L of the open reading frames. Express the length of L in codons.
from Bio import SeqIO
from Bio.Seq import Seq
from Bio import Entrez
import matplotlib.pyplot as plt
import numpy as np


class GeneFinder:
    genes = []
    protein_dict = {
        'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
        'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
        'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
        'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
        'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
        'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
        'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
        'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
        'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
        'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
        'TAA': '*', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
        'TAG': '*', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
        'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
        'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
        'TGA': 'W', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
        'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
    }

    def __init__(self, genome_id, length_l=0):
        self.length_l = length_l
        self.id = genome_id

        self.matched_genes = 0

        self.sequence = None
        self.reading_frames = []
        self.actual_genes = []
        self.found_genes = []
        self.protein_frames = []

    def parse_genome(self):
        Entrez.email = 'kk8876@student.uni-lj.si'
        with Entrez.efetch(db='nucleotide', id=self.id, rettype='fasta', retmode='text') as handle:
            data = SeqIO.read(handle, 'fasta')
            self.sequence = data.seq
            print('Sequence length:', len(self.sequence))
        with Entrez.efetch(db='nucleotide', id=self.id, rettype='gb') as handle:
            rec = SeqIO.read(handle, 'gb')
            for x in rec.features:
                if x.type == 'CDS':
                    for k, v in x.qualifiers.items():
                        if k == 'translation':
                            self.actual_genes.append(v[0])

    def compute_reading_frames(self):
        # collects all reading frames (normal with offsets and reverse_complement with offsets) - offsets: 0, 1, 2
        for rf in range(0, 3):
            self.reading_frames.append(self.sequence[rf:len(self.sequence)])

        for rf in range(0, 3):
            self.reading_frames.append(self.sequence.reverse_complement()[rf:len(self.sequence)])

        # makes sure that reading frames are divisible by 3 (1/2 last proteins are deleted to ensure divisibility by 3)
        for x in range(0, 6):
            if len(self.reading_frames[x]) % 3 == 1:
                self.reading_frames[x] = self.reading_frames[x][:-1]
            elif len(self.reading_frames[x]) % 3 == 2:
                self.reading_frames[x] = self.reading_frames[x][:-2]

    # translates (with the dictionary above) all the reading_frames and adds them to protein_frames (now containing
    # sequences of proteins)
    # CAREFUL: for TGA is not a stop !!
    def translation(self):
        for x in range(0, 6):
            protein = ''
            for i in range(0, len(self.reading_frames[x]), 3):
                protein += str(self.protein_dict[self.reading_frames[x][i:i + 3]])
            self.protein_frames.append(protein)

    def compute_genes(self):
        for x in range(0, 6):
            # iterates though protein frames
            start_codons = []

            print('Computing reading frame: ' + str(x))

            # finds all the start codons (M's) and adds them to the table
            for index in range(0, len(self.protein_frames[x])):
                if self.protein_frames[x][index] == 'M':
                    start_codons.append(index)

            print('Number of start codons: ', len(start_codons))

            # iterate though the table of start codons
            for start_index in start_codons:
                gene = ''
                # for each M, iterate through frame (starting at M-> until first * is found)

                for protein in self.protein_frames[x][start_index:]:
                    if protein == '*':
                        break
                    else:
                        gene += protein

                if start_index == 550803:
                    print(gene)

                if len(gene) < self.length_l:  # eliminates genes that are shorter than specified length
                    continue
                if gene not in self.found_genes:  # adds the gene to found_genes (does not add duplicates)
                    self.found_genes.append(gene)

        # Quick 'analysis' so check how many found_genes are actual_genes
        print('\n')
        print('found genes: ', len(self.found_genes))
        print('actual genes:', len(self.actual_genes))
        for gene in self.found_genes:
            if gene in self.actual_genes:
                self.matched_genes += 1
        print('matched genes:', self.matched_genes)

    def actual_gene_analysis(self):
        actual_gene_length = []
        for gene in self.actual_genes:
            # print(gene)
            actual_gene_length.append(len(gene))

        print('Maximum:', max(actual_gene_length))
        print('Minimum:', min(actual_gene_length))
        print('Average:', round(sum(actual_gene_length)/len(actual_gene_length), 4))

    def compute_median(self, lst):
        mid = len(lst) // 2  # Take the mid of the list
        if len(lst) % 2 == 1:  # check if the len of list is odd
            return sorted(lst)[mid]  # if true then mid will be median after sorting
        else:
            # return 0.5 * sum(sorted(xs)[mid - 1:mid + 1])
            return 0.5 * np.sum(sorted(lst)[mid - 1:mid + 1])  # if false take the avg of mid

    def run(self):
        self.parse_genome()
        self.compute_reading_frames()
        self.translation()
        self.compute_genes()
        # self.actual_gene_analysis()


if __name__ == '__main__':
    actual_genes = 0
    steps = []
    found_genes = []
    matched_genes = []

    found_genes_pc = []
    precision_pc = []

    for l in range(30, 1000, 25):
        print('Computing L =', l)
        gf = GeneFinder('NC_000908', l)
        gf.run()

        steps.append(l)  # steps
        actual_genes = len(gf.actual_genes)  # actual genes in genome (509)
        print('Median: ', gf.compute_median(gf.actual_genes))
        matched_genes.append(gf.matched_genes)  # list of matched genes
        found_genes.append(len(gf.found_genes))  # found genes (all that were 'predicted')

    for x in range(0, len(steps)):
        found_genes_pc.append(matched_genes[x]/actual_genes)  # gets % of found genes
        precision_pc.append(matched_genes[x]/found_genes[x])  # gets % of predicted genes

    plt.plot(steps, found_genes_pc, label='recall')  # plots the found genes (%)
    plt.plot(steps, precision_pc, label='precision')  # plots the precision

    plt.xlabel('L')
    plt.ylabel('Percentage')
    plt.title('Precision-Recall graph')

    plt.legend()

    plt.show()
