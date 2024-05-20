seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
#count how many times of GTGTGT are there
rep_1 = 0
for i in range (len(seq)):
    if seq[i:i+6] == 'GTGTGT':
        rep_1 += 1
#count how many times of GTCTGT are there
rep_2 = 0
for j in range (len(seq)):
    if seq[j:j+6] == 'GTCTGT':
        rep_2 += 1 
print('the sequence has ', rep_1, 'times of "GTGTGT"')
print('the sequence has ', rep_2, 'times of "GTCTGT"')