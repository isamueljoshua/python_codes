class LS_Tst:
    def __new__(cls, n):
        ls = list(i for i in range(n))
        return ls

s = LS_Tst(4)
for n in s:
    print("N here: ", n)