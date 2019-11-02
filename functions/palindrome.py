word = input("enter your word")
def isPalindrome(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        return "your input is palindrome"
    return "your input is not palindrome"
print(isPalindrome(word))