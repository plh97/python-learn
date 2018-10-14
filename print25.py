#!/usr/bin/python
# -*- coding: UTF-8 -*-

# more and more practice


def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(" ")
    return words


def sort_words(words):
    """Sorts the words."""
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    return word



def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    return word


def sort_sentence(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    # words = sort_sentence(sentence)
    # print words
    # print_first_word(words)
    # print_last_word(words)



if __name__ == '__main__':
    print_first_and_last_sorted(break_words('hi , am this'))
