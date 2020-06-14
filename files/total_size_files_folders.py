import os

totalsize = 0
for filename in os.listdir('C:\\windows\\system32'):
    if not os.path.isfile(os.path.join('C:\\windows\\system32', filename)):
        continue
    totalsize = totalsize + os.path.getsize(os.path.join('C:\\windows\\system32', filename))

# output - 1250263847 bytes
print(totalsize)