#input is 552555
#output is (2,5) , (1,2), (3,5)


from itertools import groupby
for i,j in groupby(input()):

    print(len(list(j)), str(i), end = " ")
