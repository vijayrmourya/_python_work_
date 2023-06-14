#!/usr/bin/env python
"""
The rules for two words to be considered anagrams are as follows:

1. Both words must contain the same set of characters.
2. Each character in both words must have the same frequency (number of occurrences).
3. The words should be of the same length.

In other words, if two words can be formed by rearranging the letters of each other and they have the same length and the same count of each character, then they are anagrams.

For example, let's consider the words "listen" and "silent":

1. Both words contain the same set of characters: 'l', 'i', 's', 't', 'e', 'n'.
2. Each character occurs once in both words.
3. Both words have the same length, which is 6.

Therefore, "listen" and "silent" are anagrams.

On the other hand, if two words have different sets of characters or the frequency of any character differs between the two words, they are not anagrams.
"""
__all__ = ['check_multiple_words_anagram', 'check_two_word_anagram']


def check_two_word_anagram(word_1: str, word_2: str):
    """
    To check anagrams
    :param word_1(str): input word string 1
    :param word_2(str): input word string 2
    :return(bool): True if the input is anagram else False
    """
    try:
        word_1 = ''.join(e.lower() for e in word_1 if e.isalnum())
        word_2 = ''.join(e.lower() for e in word_2 if e.isalnum())
        if sorted(word_1) == sorted(word_2):
            return True
        else:
            return False
    except TypeError as TE:
        print(f"Invalid input data type! {TE}\n{word_1}:{type(word_1)},{word_2}{type(word_2)}")
        return False
    except Exception as E:
        print("Unexpected exception!")
        return False


def check_multiple_words_anagram(*check_anagrams):
    """
    To check anagrams
    :param check_anagrams(list(str)): input words
    :return(bool): True if the input is anagram else False
    """
    try:
        if len(check_anagrams) == 1:
            print("Provide 2 words at least")
            return False
        word_array = []
        word_size = len(set(''.join(e.lower() for e in check_anagrams[0] if e.isalnum())))
        for word in check_anagrams:
            word = ''.join(e.lower() for e in word if e.isalnum())
            if word_size != len(set(''.join(e.lower() for e in word if e.isalnum()))):
                return False
            word_array.append(''.join(e.lower() for e in word if e.isalnum()))
            word_size = len(set(word))
        if len(set("".join(word_array))) != word_size:
            return False
        else:
            return True
    except TypeError as TE:
        print(f"Invalid input data type! {TE}\n{check_anagrams}:{type(check_anagrams)}")
        return False
    except Exception as E:
        print("Unexpected exception!")
        return False


if __name__ == '__main__':
    try:
        print("Welcome to Anagram check!\n")
        word_1 = input("Enter the first word:")
        word_2 = input("Enter the second word:")
        word_3 = input("Enter the second word:")
        word_4 = input("Enter the second word:")
        if check_two_word_anagram(word_1, word_2):
            print(f'"{word_1} and {word_2}" are Anagrams!')
        else:
            print(f'"{word_1} and {word_2}" are not Anagrams')
        if check_multiple_words_anagram(word_1, word_2, word_3, word_4):
            print(f'"{word_1, word_2, word_3, word_4}" are Anagrams!')
        else:
            print(f'"{word_1, word_2, word_3, word_4}" are not Anagrams')
    except Exception as E:
        print("Some Error Occured!", E)
