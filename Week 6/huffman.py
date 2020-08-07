#!/usr/local/bin/python3
# Author: Brandon Liang

import heapq
from collections import deque

# A binary tree class for Huffman
class HuffmanNode:
    def __init__(self, freq, symbol='', left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right

    # level-order traversal helps for debugging
    def printTree(self):
        Q = deque([(self, 0)])

        while Q:
            curr, level = Q.popleft()
            print('Level {}: {}'.format(level, curr.symbol))

            if curr.left:
                Q.append((curr.left, level + 1))
            if curr.right:
                Q.append((curr.right, level + 1))

    # helper for encoding just one letter
    def encodeLetter(self, letter, mutant, path=''):
        if not self.left and not self.right:
            if self.symbol == letter:
                mutant[0] = path
        else:
            if self.left:
                self.left.encodeLetter(letter, mutant, path=path + '0')
            if self.right:
                self.right.encodeLetter(letter, mutant, path=path + '1')
    
    # encode an entire word
    def encode(self, plaintext):
        enc = list()
        for l in plaintext:
            mutant = [None]
            self.encodeLetter(l, mutant)
            enc.append(mutant[0])

        return ''.join(enc)

    # decode letter by letter, until you run out or reach a terminal node
    def decodeSegment(self, mutant):
        if (not self.left and not self.right) or not mutant[0]:
            return self.symbol
        elif mutant[0][0] == '0':
            mutant[0] = mutant[0][1:]
            return self.left.decodeSegment(mutant)
        else:
            mutant[0] = mutant[0][1:]
            return self.right.decodeSegment(mutant)

    # decode an entire word
    def decode(self, ciphertext):
        dec = ''
        segment = [ciphertext]
        while segment[0]:
            dec += self.decodeSegment(segment)

        return dec

    # needed for heap operations
    def __lt__(self, other):
        return self.freq < other.freq

# will give us our Huffman tree via greedy method
def huffman(frequencies):
    n = len(frequencies)
    Q = [HuffmanNode(frequencies[f], symbol=f) for f in frequencies]
    heapq.heapify(Q)

    for i in range(n - 1):
        x = heapq.heappop(Q)
        y = heapq.heappop(Q)
        z = HuffmanNode(x.freq + y.freq, left=x, right=y)
        heapq.heappush(Q, z)

    return heapq.heappop(Q)

frequencies1 = {'a': 0.32, 'b': 0.25, 'c': 0.2, 'd': 0.18, 'e': 0.05}
res = huffman(frequencies1)
print('Huffman tree:')
res.printTree()
print('Encoding {}: {}'.format('abcde', res.encode('abcde')))
print('Decoding {}: {}'.format(res.encode('abcde'), res.decode(res.encode('abcde'))))

frequencies2 = {'a': 0.5, 'b': 0.25, 'c': 0.125, 'd': 0.125}
res = huffman(frequencies2)
print('\nHuffman tree:')
res.printTree()
print('Encoding {}: {}'.format('abcd', res.encode('abcd')))
print('Decoding {}: {}'.format(res.encode('abcd'), res.decode(res.encode('abcd'))))
