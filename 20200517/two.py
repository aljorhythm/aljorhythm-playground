# 5413. Rearrange Words in a Sentence
# Given a sentence text (A sentence is a string of space-separated words) in the following format:

# First letter is in upper case.
# Each word in text are separated by a single space.
# Your task is to rearrange the words in text such that all words are rearranged in an increasing order of their lengths. If two words have the same length, arrange them in their original order.

# Return the new text following the format shown above.

text =  "Leetcode is cool"
text = text.lower()
result = " ".join(sorted(text.split(),key = lambda w: len(w)))
result = result[:1].upper() + result[1:]
print("Is cool leetcode" == result)
print(result)

text = "To be or not to be"
text = text.lower()
result = " ".join(sorted(text.split(),key = lambda w: len(w)))
result = result[:1].upper() + result[1:]
print("To be or to be not" == result)
print(result)
