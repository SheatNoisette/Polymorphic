""" 
A simple program to generate a simple randomized encryption / decryption
functions
"""

import random

# Ecrypt | Decrypt instuction
# /r -> Replace by a random number between 0 and 255
encryptionTable = [
    ["string = [e ^ /r for e in string]", "string = [e ^ /r for e in string]"],
    ["string = [e + /r for e in string]", "string = [e - /r for e in string]"],
    ["string = [e * /r for e in string]", "string = [e // /r for e in string]"],
    ["string = [e << 2 for e in string]", "string = [e >> 2 for e in string]"],
    ["string = [e << 1 for e in string]", "string = [e >> 1 for e in string]"]
]


# Create a new encryption/ associated decryption algorithm
def createEncryption():

    # Store the generated code
    generatedCode = ""

    # Choose how much step are required to create the encryption algorithm
    steps = random.randint(2, 16)

    # Get size of the encryption table
    encryptionTableSize = len(encryptionTable)

    # New encryption/decryption algorithm table
    ecryptionAlgo = []
    decryptionAlgo = []

    # Create algorithms
    for _ in range(steps):
        # Create a new random number shared by step
        rng = random.randint(0, 255)

        # Create algorithms
        instructionChoosen = random.randint(0, encryptionTableSize - 1)
        ecryptionAlgo.append(encryptionTable[instructionChoosen][0].replace("/r", str(rng)))
        decryptionAlgo.insert(0, encryptionTable[instructionChoosen][1].replace("/r", str(rng)))
    
    # Generate function string - These was splited for readability
    generatedCode = ""

    # Encryption
    generatedCode += "def encrypt(string):\n"

    for i in range(steps):
        generatedCode += " " * 2 + ecryptionAlgo[i] + "\n"

    generatedCode += " " * 2 + "return string\n"

    # Dencryption
    generatedCode += "def decrypt(string):\n"

    for i in range(steps):
        generatedCode += " " * 2 + decryptionAlgo[i] + "\n"
    
    generatedCode += " " * 2 + "return string\n"

    return generatedCode


def generateArray(string):
    """ Create a array containing char id """
    output = []
    for char in string:
        output.append(ord(char))
    return output

def arrayToString(array):
    return "[" + ", ".join([str(e) for e in array]) + "]"

arrayHelloWord = generateArray("Hello World!")
algorithms = createEncryption()

testCode = "array =" + arrayToString(arrayHelloWord) + "\n"
testCode += algorithms

testCode+= """
def arrayToOutput(array):
    output = ""
    for e in array:
        output += chr(e)
    return output

print("Input array: ", array)
print(arrayToOutput(array))

print("Encrypting...")
array = encrypt(array)
print(array)

print("Decrypting...")
array = decrypt(array)
print(array)
print(arrayToOutput(array))
"""

print("GENERATED CODE:\n", testCode)

print("===========================")
exec(testCode)