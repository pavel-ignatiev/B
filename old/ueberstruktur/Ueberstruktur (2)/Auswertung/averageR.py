
from sys import argv
tab = open(argv[1])
open(argv[2], 'a').close()
table_save = open(argv[2], 'w')
table = tab.read()

table = table.split('\t\t7\n#\n')[1]
table = table.split()

print("zeilen %s" % int(float(len(table))/7))

tab_edit = [[0 for i in range(7) ] for j in range(int(len(table)/7))]

for y in range(len(table)):
	tab_edit[int((y-y%7)/7)][y%7] = float(table[y])
table = tab_edit
res_mean = list()

tab_temp_sum = float()
tab_R_sum = float()
divider = 0

list_temp=list()
list_R=list()
i=0
print(len(table))
count=0
while i < (len(table)-1):
   
    while count < 2 and i < len(table)-1:
        tab_R_sum += table[i][5]
        tab_temp_sum += table[i][0]
        divider += 1 
        if table[i][3]*table[i+1][3] < 0:
            if count == 1 :
                 list_R.append(tab_R_sum/divider)
                 list_temp.append(tab_temp_sum/divider)
                 tab_R_sum = 0.0
                 tab_temp_sum = 0.0
                 divider = 0
            count = count + 1
        i += 1
        #print(i)
    count=0	
	
        
#print(list_R)
for i in range(len(list_R)):
     table_save.writelines(str(list_temp[i]))
     table_save.writelines("\t")
     table_save.writelines(str(list_R[i]))
     table_save.writelines("\n")

print(tab_edit[0][0])