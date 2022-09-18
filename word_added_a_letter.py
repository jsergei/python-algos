# startWords = ["abc", "def", "ant"], targetWords = ["dcda", "edxf", "ant", "abd", "cant"]

# input
start_words = ["abc", "def", "ant"]
target_words = ["dcda", "edxf", "ant", "abd", "cant", "cbat"]

# solution
A_CODE = ord('a')
MAX_BIT = 25

def to_binary(word):
    n = 0
    for c in word:
        n |= 1 << (ord(c) - A_CODE)
    return n

source_words = set()
for word in start_words:
    binary = to_binary(word)
    source_words.add(binary)

answer = 0
for word in target_words:
    binary = to_binary(word)
    bit_mask = 1
    for i in range(MAX_BIT + 1):
        if binary & bit_mask:
           without_letter = binary & ~bit_mask
           if without_letter in source_words:
               answer += 1
               break
        bit_mask <<= 1

print("Answer: {0}".format(answer))
