"""
Palindrom verification
"""

def is_palindrome(word: str) -> bool:
    """
    Check is word is a palindrome --A palindrome is a word, 
    number, phrase, or other sequence of symbols that reads
    the same backwards as forwards.
    ______________________________________________________________
    args
        word (str): input string to be evaluated
    ______________________________________________________________
    output
        (bool): Return True if is palindrome 
    """
    word = word.lower()
    word_reverse = word[::-1]
    return word == word_reverse

if __name__ == "__main__":
    test_word = input('Por favor ingrese una palabra: ')
    palindrome_result = is_palindrome(test_word)
    print(f"La palabra {test_word} {'es' if palindrome_result else 'no es'} un palíndromo")