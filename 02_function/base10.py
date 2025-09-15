# リスト内包表記

numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print(squares)

result = [x if x > 0 else 0 for x in range(-2, 3)]
print(result)


# 辞書内包表記

words = ["apple", "banana", "cherry"]
word_lengths = {word: len(word) for word in words}
print("単語の長さ:", word_lengths)

scores = {"Alice": 85, "Bob": 72, "Charlie": 90}
passed = {
    name: score
    for name, score in scores.items()
    if score > 80
}
print(passed)