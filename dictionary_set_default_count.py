message = 'It was a cold Day in May'

count = {}

# this code without upper() would seperately give caps D and small d's count, so modifying it
for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)