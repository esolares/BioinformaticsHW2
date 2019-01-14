#!/usr/bin/env python3

import random

def random_kmer (length: int) -> str:
	nt = ['A', 'T', 'C', 'G']
	kmer = ''
	for i in range(length):
		kmer = kmer + random.choice(nt)
	return kmer

if __name__ == '__main__':
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
