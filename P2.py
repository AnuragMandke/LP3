import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def calculate_frequency(data):
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1
    return frequency

def build_huffman_tree(frequency):
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_huffman_codes(root, current_code="", codes={}):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = current_code

    generate_huffman_codes(root.left, current_code + "0", codes)
    generate_huffman_codes(root.right, current_code + "1", codes)

    return codes

def huffman_encoding(data):
    if not data:
        return "", {}

    frequency = calculate_frequency(data)
    root = build_huffman_tree(frequency)
    codes = generate_huffman_codes(root)
    encoded_data = "".join(codes[char] for char in data)

    return encoded_data, codes

def huffman_decoding(encoded_data, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    decoded_data = ""
    current_code = ""

    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codes:
            decoded_data += reverse_codes[current_code]
            current_code = ""

    return decoded_data

if __name__ == "__main__":
    data = input("Enter the data to encode: ")
    encoded_data, codes = huffman_encoding(data)
    print("Encoded Data:", encoded_data)
    print("Huffman Codes:", codes)

    decoded_data = huffman_decoding(encoded_data, codes)
    print("Decoded Data:", decoded_data)