class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)


    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]

        curr_node.data = string


    def start_with(self, prefix):
        curr_node = self.head
        result = []
        subtrie = None

        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                subtrie = curr_node
            elif char == '?':
                break
            else:
                return None
        
        queue = list(subtrie.children.values()) if subtrie else list(self.head.children.values()) 

        while queue:
            curr = queue.pop()
            if curr.data != None and len(curr.data) == len(prefix):
                result.append(curr.data)

            queue += list(curr.children.values())

        return result


def solution(words, queries):
    trie_start = Trie()
    trie_end = Trie()
    cnt = [0] * len(queries)

    for tmp in words:
        trie_start.insert(tmp)
        trie_end.insert(tmp[::-1])
    
    for idx, q in enumerate(queries):
        result = []
        
        if q[0] == '?' and q[-1] == '?':
            result = trie_start.start_with(q)
        elif q[0] == '?':
            result = trie_end.start_with(q[::-1])
        elif q[-1] == '?':
            result = trie_start.start_with(q)

        cnt[idx] = len(result) if result else 0
    
    return cnt
            
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))