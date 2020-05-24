
def isPrefixOfWord(sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        words = sentence.split(" ")
        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i + 1
        return -1




inputs = [
    [
        "hello from the other side", "they"
    ],
    [
        "i use triple pillow", "pill"
    ]
]
outputs = [
    -1, 4
]

results = []
for (i, o) in zip(inputs, outputs):
    result = isPrefixOfWord(i[0], i[1])
    print(result)
    print(result == o)
    results.append((result == o,result))

print("all")
print(results)