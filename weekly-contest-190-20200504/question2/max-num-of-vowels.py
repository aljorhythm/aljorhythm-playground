def maxVowels(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    maxCount = 0
    lastCount = -1
    lastSubstrFirstLetterIsVowel = False
    isVowel = lambda letter: letter in ['a','e','i','o','u']
    for i in range(len(s)):
        if i + k > len(s):
            break
        vowCount = 0
        if lastCount == -1:
            substr = s[i:i+k]
            vowCount = len(filter(isVowel, substr))
        else:
            vowCount = lastCount - (1 if lastSubstrFirstLetterIsVowel else 0) + isVowel(s[i+k-1])
        lastSubstrFirstLetterIsVowel = isVowel(s[i])
        maxCount = max(vowCount, maxCount)
        lastCount = vowCount

    return maxCount


inputs = [
    [
        "abciiidef", 3
    ],
    [
        "aeiou", 2
    ],
    ["leetcode", 3]
]
outputs = [
    3, 2, 2
]

results = []
for (i, o) in zip(inputs, outputs)[0:]:
    result = maxVowels(i[0], i[1])
    print(result)
    print(result == o)
    results.append((result == o, result))

print("all")
print(results)
