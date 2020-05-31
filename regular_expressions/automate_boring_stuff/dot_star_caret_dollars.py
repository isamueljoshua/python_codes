import re

# use the ^ symbol to match at the start of the word
beginsWithHelloRegex = re.compile(r'^Hello')
# output Hello
print(beginsWithHelloRegex.search('Hello there!'))

# this would return None since the pattern does not match
print(beginsWithHelloRegex.search('Hi Hello there!'))

# use the $ symbol to match the pattern at end of the word
endsWithRegex = re.compile(r'world!$')
# output world!
print(endsWithRegex.search('Hello world!'))

# this returns None since the string does not match
print(endsWithRegex.search('Hello world!sahdbhshdb'))

# the entire string must begin and end with the pattern specified
# so we use the ^ and $ at the end
allDigitsRegex = re.compile(r'^\d+$')
# output 231242362361
print(allDigitsRegex.search('231242362361'))

# this returns None since the pattern starts with number and ends with number but the
# x character in between does not match the condition which says it must be all numbers 
print(allDigitsRegex.search('23124x2362361'))

'''
Let's talk about the wild card Dot (.) character
'''
# the . matches any character except new line
atRegex = re.compile('.at')
# output of matches ['cat', 'hat', 'sat', 'lat', 'mat'] notice that flat match returns a lat which means that the . matched a single character
print(atRegex.findall('The cat in the hat sat on the flat mat'))

# now changing the compile text to match 1 or 2 characters
atRegex = re.compile('.{1,2}at')
# output of matches [' cat', ' hat', ' sat', 'flat', ' mat'] now even flat gets returned, 
# but the other strings get a space before them since it must match any character
print(atRegex.findall('The cat in the hat sat on the flat mat'))


'''
Dot-Star .* matching anything
'''
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
# output [('John', 'Doe')]
print(nameRegex.findall('First Name: John Last Name: Doe'))

'''
Now the Dot-Star is greedy mode, it will try to match as much text as possible

for Non-Greedy mode use .*?
'''
serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
# output ['To serve humans']
print(nongreedy.findall(serve))

greedy = re.compile(r'<(.*)>')
# output ['To serve humans> for dinner.']
print(greedy.findall(serve))


'''
Making the Dot Match new lines too
(with re.DOTALL)
'''
prime = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
dotStar = re.compile(r'.*')
# output Serve the public trust. since the pattern says it to match any character except the new line
print(dotStar.search(prime))

# to include the new lines as well do like the below
dotStar = re.compile(r'.*', re.DOTALL)
# output is <re.Match object; span=(0, 61), match='Serve the public trust.\nProtect the innocent.\nU>
# as you can see from above output there is only U in the last part, to solve this do like below
print(dotStar.search(prime))
# this prints all the strings
mo = dotStar.search(prime)
print(mo.group())

vowelRegex = re.compile(r'[aeiou]')
# this is case sensitive, so it matches ['o', 'o', 'u', 'i', 'e', 'a', 'o', 'i', 'i', 'o', 'u']
print(vowelRegex.findall('Al, Why do you like Lamborghinis so much?'))

# to make it case insensitive, we can do like below re.IGNORECASE or re.I as well
vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE)
print(vowelRegex.findall('Al, Why do you like Lamborghinis so much?'))