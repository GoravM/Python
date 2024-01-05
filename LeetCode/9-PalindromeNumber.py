
def isPalindrome(x):
    word = str(x)
    # Start at last position end at 0th position and take -1 steps + 0th position letter
    # ex 1234 -> "432" + "1" -> 4321
    reversed_word = word[len(word)::-1]
    print(reversed_word)
    return word == reversed_word

x = 1221

if isPalindrome(x) == True:
    print(f"{x} is a palindrome")