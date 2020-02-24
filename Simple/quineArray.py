key=0
out=[10, 112, 114, 105, 110, 116, 40, 34, 73, 39, 109, 32, 97, 110, 32, 101, 118, 105, 108, 32, 112, 114, 111, 103, 114, 97, 109, 33, 32, 73, 32, 99, 97, 110, 32, 99, 121, 112, 104, 101, 114, 32, 109, 121, 115, 101, 108, 102, 32, 97, 103, 97, 105, 110, 32, 119, 104, 101, 110, 32, 121, 111, 117, 32, 114, 117, 110, 32, 109, 101, 46, 34, 41, 10]

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