"""
Expected Output:

Text: this is a collection of words of nice words this is a fun thing it is
a : 2
collection : 1
fun : 1
is : 3
it : 1
nice : 1
of : 2
thing : 1
this : 2
words : 2
"""

# variables
word = {}
text = input("Text: ")
words_splitter = text.split()

# code
for i in words_splitter:
    frequency = word.get(i, 0)
    word[i] = frequency + 1
print()

# variables
words = list(word.keys())
words.sort()

# code
max_length = max((len(word) for word in words_splitter))
for j in words_splitter:
    print(f"{j:{max_length}} : {word[j]}")


thing, width, other_thing = "first", 13, "second"
print(f"{thing:{width}} = {other_thing}")
