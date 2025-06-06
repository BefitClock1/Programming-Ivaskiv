import os
import heapq
from collections import defaultdict

def read_words(file_path):
    with open(file_path) as f:
        n = int(f.readline())
        return [f.readline().strip() for _ in range(n)]

def heap_sort(words):
    heap = [(-len(w), w) for w in words]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(len(heap))]

def find_longest_chain(words):
    word_set = set(words)
    words = heap_sort(words)

    dp = defaultdict(lambda: 1) 
    parent = {} 
    max_chain = 1
    max_word = ''

    for word in words:
        for subword in [word[:i] + word[i+1:] for i in range(len(word))]:
            if subword in word_set and dp[subword] < dp[word] + 1:
                dp[subword] = dp[word] + 1
                parent[subword] = word
                if dp[subword] > max_chain:
                    max_chain = dp[subword]
                    max_word = subword

    chain = []
    current = max_word
    while current in parent:
        chain.append(current)
        current = parent[current]
    if current:
        chain.append(current)
    chain.reverse()

    return max_chain, chain

def main():
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, 'wchain.txt')
    out_path = os.path.join(base_path, 'wchain.out')

    words = read_words(file_path)
    max_chain, chain = find_longest_chain(words)

    with open(out_path, 'w') as f:
        f.write(str(max_chain) + '\n')

    print(f"Макс ланцюг: {max_chain}")

if __name__ == "__main__":
    main()
