#!/usr/bin/env python3

import random

def random_kmer (length: int) -> str:
	#Generates a random string of the given length from the nucleotides A, T, C, and G
	nt = ['A', 'T', 'C', 'G']
	kmer = ''
	for i in range(length):
		kmer = kmer + random.choice(nt)
	return kmer

if __name__ == '__main__':
	#Uses the function to generate 5 random k-mers of the given length
	for i in range(5):
		print(random_kmer(2))
	for i in range(5):
		print(random_kmer(3))
	for i in range(5):
		print(random_kmer(4))
	for i in range(5):
		print(random_kmer(5))
	for i in range(5):
		print(random_kmer(6))
	for i in range(5):
		print(random_kmer(7))
	for i in range(5):
		print(random_kmer(8))
	for i in range(5):
		print(random_kmer(9))
	for i in range(5):
		print(random_kmer(10))
