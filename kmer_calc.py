#!/usr/bin/env python3

import sys

def sequence_length(file_path: str) -> int:
	#Opens the fasta file and determines the length of the sequence that is being checked for the k-mers
	my_file = None
	try:
		my_file = open(file_path, 'r')
		for i, line in enumerate(my_file):
			if i == 1:
				return len(line)
	finally:
		if my_file != None:
			my_file.close()


def mer1_count(file_path: str) -> list:
	#Gives counts for each nucleotide type
	myfile = None
	try:
		my_file = open(file_path, 'r')
		for i, line in enumerate(my_file):
			if i == 1:
				a_count = 0
				t_count = 0
				c_count = 0
				g_count = 0
				n_count = 0
				for nt in line:
					if nt.lower() == 'a':
						a_count += 1
					elif nt.lower() == 't':
						t_count += 1
					elif nt.lower() == 'c':
						c_count += 1
					elif nt.lower() == 'g':
						g_count += 1
					else:
						n_count += 1 	#when adding just the counts for A, T, C, and G there was one nucleotide that was not accounted for
				return [a_count, t_count, c_count, g_count, n_count]
	finally:
		if my_file != None:
			my_file.close()


def kmer_count(seq_file_path: str, mer_file_path: str, length: int) -> list:
	#From the file of randomly generated k-mers determines which are of the appropriate length and searches for them in the sequence of interest
	#Returns a tuple containing the list of the k-mers searched for and a list of how many times each of them was found
	seq_file = None
	try:
		seq_file = open(seq_file_path, 'r')
		mer_file = open(mer_file_path, 'r')
		random_kmers = []
		max_pos = 9193 - length + 1	#ensures that the sequence is only searched for whole k-mers (the end nucleotides are not counted if there is not space for a full k-mer)
		for mer_line in mer_file:
			if len(mer_line[:-1]) == length:
				random_kmers.append(mer_line[:-1])	#adds the k-mers of the length specified to a list to be checked
		for i, line in enumerate(seq_file):
			if i == 1:	#skips the header
				kmer_counts = []
				for kmer in range(len(random_kmers)):
					kmer_count = 0
					for nt in range(len(line[:-(length)])):
						if nt <= max_pos:
							kmer_agreement = []		#for each potential k-mer a list of whether the nt agree with the k-mer being tested is generated
							for knt in range(len(random_kmers[kmer])):
								if line[nt + knt].lower() == random_kmers[kmer][knt].lower():
									kmer_agreement.append('y')
								else:
									kmer_agreement.append('n')
							if 'n' not in kmer_agreement:
								kmer_count += 1
					kmer_counts.append(kmer_count)
				return random_kmers, kmer_counts
	finally:
		if seq_file != None:
			seq_file.close()
		if mer_file != None:
			mer_file.close()

if __name__ == '__main__':
	seqlen = sequence_length(sys.argv[1])
	print('Sequence Lenth =', seqlen)
	print(' ')

	mer1_seq = ['A', 'T', 'C', 'G', 'N']
	mer1_counts = mer1_count(sys.argv[1])
	print('1-mer calculations:')
	print('Random \t\t\t=', int(seqlen/4), '\t(', 1/4, ')')
	for i in range(len(mer1_seq)):
		print(mer1_seq[i], 'count \t\t=', mer1_counts[i], '\t(', mer1_counts[i]/seqlen, ')')
	print(' ')

	for i in range(2, 11):
		kmer = kmer_count(sys.argv[1], sys.argv[2], i)
		kmer_seq = kmer[0]
		kmer_counts = kmer[1]
		print(str(i) + '-mer calculations:')
		print('Random  \t\t=', int((seqlen - (i-1))*((1/4)**i)), '\t(', (1/4)*((1/4)**(i-1)), ')')
		for x in range(len(kmer_seq)):
			if i > 8:
				print(kmer_seq[x], 'count \t=', kmer_counts[x], '\t(', kmer_counts[x]/(seqlen - i), ')')
			else:
				print(kmer_seq[x], 'count \t\t=', kmer_counts[x], '\t(', kmer_counts[x]/(seqlen - i), ')')
		#the different print statement for i > 8 makes the results prettier in calculations.txt
		print(' ')
