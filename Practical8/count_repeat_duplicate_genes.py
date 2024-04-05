import re
#ask the user to imput a sequence
rep_seq = input('Input a repetitive sequence:')
#read and create files needed
file_name = rep_seq + '_duplicate_genes.fa'
output_f = open(file_name, 'w')
input_f = open('duplicate genes.fa')
sequence = input_f.read()
#make every gene name and its corresponding sequence into one single string
l_string = ''
for line in sequence:
    if line.startswith('>'):
        l_string += '\n'+line+' '
    else:
        l_string += line
#search each gene if it contains target sequence
for line in l_string:
    if re.search(rep_seq,line):
        time = line.count(rep_seq) #count the repetition times
        name = re.findall(r'>.+?_mRNA', line)
        new_name = name + time
        new_line = re.sub(new_name, name,line)
        output_f.write(new_line + '\n')