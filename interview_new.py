# EMP Table

# EMP ID, NAME, Salary ,Designation


# select Designation, Avg(Salary) from EMployee group by Designation

s = "aabbaAaaccc"
d_op = {}
l = []
final_tup = []
for char in s:
    print("Char: ", char)
    # if len(l) ==0:
    l.append(char)
    print("Lst: ", l[len(l)-2])
    if char.lower() == l[len(l)-2].lower():
        print("LS: ", l)
        if len(l) > 1:
            final_tup.append(l)
        continue
    elif char.lower() != l[len(l)-2].lower():
        # if len(l)
        l = []
        print("LS ELSE: ", l)
    

print("Lst Final: ", l)
print("FInal tpuu: ", final_tup)
