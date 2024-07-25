#!/usr/bin/python3
"""
utf 8 validation
"""


def num_bytes_required(num):
    """
    returns the number of bytes required to represent the number in utf-8
    """
    if num >= 0 and num <= 127:
        return 1
    elif num <= 223:
        return 2
    elif num <= 239:
        return 3
    elif num <= 247:
        return 4
    return -1


def get_next_char_seq(sequence):
    """
    returns the next bytes in the sequence
    """
    num_bytes = num_bytes_required(sequence[0])
    if num_bytes < 0 or num_bytes > len(sequence):
        return None
    char_seq = sequence[:num_bytes]
    if any([num > 247 or num < 0 for num in char_seq]):
        return None
    return char_seq


def is_seq_valid_utf8(sequence):
    """
    returns True if the sequence is a valid utf-8 encoding
    """
    if len(sequence) == 1:
        return sequence[0] <= 127

    return all([bin(num >> 6)[2:] == "10" for num in sequence[1:]])


def validUTF8(data):
    """
    validates a given data set represents a valid utf-8 encoding
    the data set contains list of integers
    """
    if data is None:
        return False

    data = list(map(get_least_significant_8bits, data))
    while len(data) > 0:
        seq = get_next_char_seq(data)
        if seq is None or not is_seq_valid_utf8(seq):
            return False
        data = data[len(seq):]
    return True


def get_least_significant_8bits(num):
    """
    returns the 8 least significant bits of num
    """
    return num & ((1 << 8) - 1)
