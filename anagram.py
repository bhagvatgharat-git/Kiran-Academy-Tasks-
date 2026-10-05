# Program 5: Check whether two words are Anagrams

word1 = input("Enter first word: ").lower()
word2 = input("Enter second word: ").lower()

if sorted(word1) == sorted(word2):
    print("The words are Anagrams.")
else:
    print("The words are not Anagrams.")
