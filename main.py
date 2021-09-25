# import module
import random as r

ph_no = []
ph_no.append(r.randint(6, 9))

for i in range(0, 9):
    ph_no.append(r.randint(0, 9))

# printing the number
for i in ph_no:
    print(i, end="")