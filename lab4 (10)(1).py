"""
UTM: CSC108, Fall 2021

Practical Lab 4

Instructors: Michael Liut, Andrew Petersen, Andi Bergen,
             Tingting Zhu, Pooja Vashisth, and Sonya Allin

This code is provided solely for the personal and private use of
students taking the CSC108 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Michael Liut, Haocheng Hu

LAB RESTRICTIONS, PLEASE READ:
You are not allowed to use any imports, except for the ones given (if any).
You may not use any lists or list methods, for the same reasons as last week.
Please also do not use try-except statements, you should be able to anticipate
or prevent any errors from happening at all!
    >>> is_palindrome("cabcbac")
    'True'
    >>> is_palindrome("cabbac")
    'Ture'
    >>> is_palindrome("cabcba")
    'False'

"""


def is_palindrome(string: str) -> bool:
    """
    Your "is_palindrome" implementation from last week (Lab 3), which you may
    use as is or with modifications if you didn't get it right last time.
    """
    p1 = 0
    p2 = len(string) - 1

    while True:
        if p1 == p2:
            return True
        elif string[p1] == string[p2]:
            p1 += 1
            p2 -= 1
        else:
            return False


def is_palindrome_string(string: str) -> bool:
    """
    Given a string <string>, return whether this string is a palindrome string.

    For the purposes of this function, a palindrome string is any string that
    forms a palindrome if you piece together the first letter of every word in
    the string. We define a word here to be ANY CONTINUOUS SEGMENT OF
    ALPHABETICAL CHARACTERS. That means that "abc;def", has two words: "abc"
    and "def". The separating character does not have to be whitespace, and
    there could be more than one separating character between two words.

    Since you will be using your is_palindrome function from last week, the
    definition of a palindrome will remain the same as the definition from
    last week (ignore capitalization and whitespace).

    A simple example: given the string "test string test", there are three
    words, "test", "string", and "test". The first letters of each word come
    together to form the string "tst". And since "tst" is a palindrome, this
    function should return True for the input "test string test".

    Precondition: <string> will contain at least one word.

    Restrictions: you must use your "is_palindrome" function from lab 3 as a
                  helper for this function, in addition to the lab restrictions
                  defined at the start of this file. You are allowed and are
                  encouraged to fix any issues with your previous submission
                  for this function.

    >>> is_palindrome_string(" |fffff|  abc;def; ;; aacveee  [[[fwaeas]]]    ")
    'True'
    >>> is_palindrome_string("the tree tall")
    'True'
    >>> is_palindrome_string("you are big")
    'False'
    """
    ptr = len(string) - 1
    while ptr != -1:
        if not string[ptr].isalpha() or\
                (ptr != 0 and string[ptr - 1].isalpha()):
            string = string[:ptr] + string[ptr + 1:]
        ptr -= 1

    return is_palindrome(string)


def reverse_sentence(s: str) -> str:
    """
    Given a sentence <s>, we define a word within <s> to be a continuous
    sequence of characters in <s> that starts with a capital letter and
    ends before the next capital letter in the string or at the end of
    the string, whichever comes first. A word can include a mixture of
    punctuation and spaces.

    This means that in the string 'ATest string!', there are in fact only two
    words: 'A' and 'Test string!'. Again, keep in mind that words start with a
    capital letter and continue until the next capital letter or the end of the
    string, which is why we consider 'Test string!' as one word.

    This function will reverse each word found in the string, and return a new
    string with the reversed words, as illustrated in the doctest below.

    >>> reverse_sentence('ATest string!')
    'A!gnirts tseT'
    >>> reverse_sentence("Best 12312412AbcTest sadawd a!")
    '21421321 tseBcbA!a dwadas tseT'
    >>> reverse_sentence("ABeautiful tree?")
    'A?eert lufituaeB'
    >>> reverse_sentence("ATall man!")
    'A!nam llaT'

    """
    result = carrier = ""
    ptr = len(s) - 1
    while ptr != -1:
        if s[ptr].isupper():
            carrier += s[ptr]
            result = carrier + result
            carrier = ""
        else:
            carrier += s[ptr]

        ptr -= 1

    return result

print(reverse_sentence("a test string"))