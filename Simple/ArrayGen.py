""" Generate the encoded string """

program = """
print("I'm an evil program! I can cypher myself again when you run me.")
"""

def generateArray(string):
    output = []
    for char in string:
        output.append(ord(char))
    return output

print(generateArray(program))
