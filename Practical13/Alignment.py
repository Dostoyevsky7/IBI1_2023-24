#analze gene similarity from human, mouse, and rat
import blosum as bl
matrix = bl.BLOSUM(62)
#line 2 and 3 is inspired from https://pypi.org/project/blosum/ to use BLOSUM62 in python
H = open('SLC6A4_HUMAN.fa','r')
M = open('SLC6A4_MOUSE.fa','r')
R = open('SLC6A4_RAT.fa','r')
#read the file and and store the sequences into strings
human = ''.join(H.read().splitlines()[1:])
mouse = ''.join(M.read().splitlines()[1:])
rat = ''.join(R.read().splitlines()[1:])
# compare human and mouse
human_mouse = 0 #record the BLOSUM score
hm_same = 0 #record the number of same amino acid 
for i in range(min(len(human),len(mouse))):
    h = human[i]
    m = mouse[i]
    human_mouse += matrix[h][m]
    if h == m:
        hm_same += 1
hm_percent = hm_same/min(len(human),len(mouse))*100
print('human and mouse score: ',human_mouse)
print('human and mouse indentical amino acid percentage: ', hm_percent,'%')
# compare human and rat
human_rat = 0
hr_same = 0
for j in range(min(len(human),len(rat))):
    h = human[j]
    r = rat[j]
    human_rat += matrix[h][r]
    if h == r:
        hr_same += 1
hr_percent = hr_same/min(len(human),len(rat))*100
print('human and rat score: ',human_rat)
print('human and rat indentical amino acid percentage: ', hr_percent,'%')
# compare mouse and rat
mouse_rat = 0
mr_same = 0
for k in range(min(len(mouse),len(rat))):
    m = mouse[k]
    r = rat[k]
    mouse_rat += matrix[m][r]
    if m == r:
        mr_same += 1
mr_percent = mr_same/min(len(mouse),len(rat))*100
print('mouse and rat score: ',mouse_rat)
print('mouse and rat indentical amino acid percentage: ', mr_percent,'%')
#determine which pair is the closely related
closest = max(human_mouse, human_rat, mouse_rat)
if closest == mouse_rat:
    Closest = 'mouse and rat'
elif closest == human_rat:
    Closest = 'human and rat'
else:
    Closest = 'human and mouse'
print(Closest+' are most closely related')
#determine whether mouse or rat is better model organism
if human_mouse > human_rat:
    print("mouse is a better model organism for human based on data analysed here")
elif human_rat > human_mouse:
    print("rat is a better model organism for human based on data analysed here")