key=56
out=[50, 72, 74, 81, 86, 76, 16, 26, 113, 31, 85, 24, 89, 24, 93, 78, 81, 84, 24, 72, 74, 87, 95, 74, 89, 85, 25, 24, 113, 24, 91, 89, 86, 24, 91, 65, 72, 80, 93, 74, 24, 85, 65, 75, 93, 84, 94, 24, 89, 95, 89, 81, 86, 24, 79, 80, 93, 86, 24, 65, 87, 77, 24, 74, 77, 86, 24, 85, 93, 22, 26, 17, 50]


import random
def generateArray(string):
    output = []
    for char in string:
        output.append(ord(char))
    return output

def arrayToString(array):
    return "[" + ", ".join([str(e) for e in array]) + "]"

def XORCypher(inputArray, key):
    output = []
    for e in inputArray:
        output.append(e ^ key)
    return output

def arrayToOutput(array):
    output = ""
    for e in array:
        output += chr(e)
    return output

def intSize(inputInt):
    size = 1
    while inputInt > 0:
        size += 1
        inputInt = inputInt // 10
    return size

# Run code here
exec(arrayToOutput(XORCypher(out, key)))

# Generate new output

oldlen = len(arrayToString(out))
oldlenKey = intSize(key)
# Uncypher the old content
out = XORCypher(out, key)
# Create a new key
key = random.randint(1, 255)
# Cypher with the new key
out = XORCypher(out, key)

# Infos - Can be removed
"""
print("New key:", key)
print("Old Key numb size:", oldlenKey)
print("New key size: ", intSize(key))
print("Old size:", oldlen)
print("New size: ", len(out))
"""

# Copy his own new cyphered content to a new file 
content = "key=" + str(key) + "\nout=" + arrayToString(out) + "\n\n" + open(__file__).read()[10 + oldlenKey + oldlen:]
open(__file__,"w").write(content)