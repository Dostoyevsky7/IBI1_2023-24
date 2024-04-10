import re
#ask the user to imput a sequence
rep_seq = input('Input a repetitive sequence:')
#read and create files needed
file_name = rep_seq + '_duplicate_genes.fa'
output_f = open(r'D:/Downloadssss/IBI1_2023-24/Practical8' + '\\' + file_name, 'w')
sequence = open('duplicate_genes.fa')
#make every gene name and its corresponding sequence into one single string
with open('store.fa', 'w') as l_string:
    for line in sequence:
        if line.startswith('>'):
            l_string.write('\n'+line[:-1])
        else:
            l_string.write(line[:-1])
#search each gene if it contains target sequence
with open('store.fa', 'r') as l_read:
    for line in l_read:
        if rep_seq in line:
            time = line.count(rep_seq)
            name = re.findall(r'>.+?_mRNA', line)
            name_str = str(name)
            new_name = re.escape(name_str) + str(time)
            new_line = line.strip(name_str)
            output_f.write(new_name + '\n' + new_line)