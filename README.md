# BioinformaticsHW2

**The python script is in the file named "HW2.ipynb" edited by Jupyter Notebook.**

## Results

***Part 1. Using kmers from 1-10, calculate the probability any random kmer can be created. I.e. for kmer where k = 1, p = 1/4***
  
The probability any random 1-mer can be created is 0.25
The probability any random 2-mer can be created is 0.0625
The probability any random 3-mer can be created is 0.015625
The probability any random 4-mer can be created is 0.00390625
The probability any random 5-mer can be created is 0.0009765625
The probability any random 6-mer can be created is 0.000244140625
The probability any random 7-mer can be created is 6.103515625e-05
The probability any random 8-mer can be created is 1.52587890625e-05
The probability any random 9-mer can be created is 3.814697265625e-06
The probability any random 10-mer can be created is 9.5367431640625e-07
  
***Generate 5 randomly generated strings using {A,T,C,G} as an alphabet, for each kmer from k = 1 to 10***
  
5 randomly generated strings for 1-mer:
\['C', 'A', 'T', 'G', 'A']

5 randomly generated strings for 2-mer:
\['CA', 'CC', 'TG', 'GG', 'TC']

5 randomly generated strings for 3-mer:
\['GGA', 'TCG', 'CAG', 'CGC', 'GTC']

5 randomly generated strings for 4-mer:
\['CCGG', 'TCCA', 'AGAT', 'ATCA', 'TCTG']

5 randomly generated strings for 5-mer:
\['GTGGA', 'ATGGG', 'CACCA', 'ACGCG', 'CACAC']

5 randomly generated strings for 6-mer:
\['GGCACC', 'CGCTGT', 'AAAAAA', 'ACAGGG', 'TCAGTC']

5 randomly generated strings for 7-mer:
\['AGCGTTA', 'AGCTAGC', 'AGATCGT', 'AAAATAT', 'GATTGCA']

5 randomly generated strings for 8-mer:
\['GTGACACT', 'ACGAGCTT', 'TCTCGGTA', 'GTGAGACC', 'CGACTAGA']

5 randomly generated strings for 9-mer:
\['TAGAGGCGA', 'TGGATCGAC', 'TAGTAATTG', 'GCAACTGGA', 'ATCCACAAG']

5 randomly generated strings for 10-mer:
\['TACCTTTGAG', 'GACACCATTG', 'GTCCCTTGCC', 'GAAAGCGTCC', 'TATCAATGAG']
  
***Part 3. Use python to find each generated kmer in the fasta file located in ~/shared/aligners folder***
  
Indices of 5 randomly generated strings for 1-mer:
\[15, 2, 0, 1, 2]

Indices of 5 randomly generated strings for 2-mer:
\[19, 21, 0, 5, 26]

Indices of 5 randomly generated strings for 3-mer:
\[6, 269, 103, 196, 190]

Indices of 5 randomly generated strings for 4-mer:
\[209, 248, 88, 722, 191]

Indices of 5 randomly generated strings for 5-mer:
\[896, 1311, 237, -1, 672]

Indices of 5 randomly generated strings for 6-mer:
\[6326, -1, 157, 2439, -1]

Indices of 5 randomly generated strings for 7-mer:
\[-1, -1, -1, -1, -1]

Indices of 5 randomly generated strings for 8-mer:
\[-1, -1, -1, -1, -1]

Indices of 5 randomly generated strings for 9-mer:
\[-1, -1, -1, -1, 1935]

Indices of 5 randomly generated strings for 10-mer:
\[-1, -1, -1, -1, -1]
