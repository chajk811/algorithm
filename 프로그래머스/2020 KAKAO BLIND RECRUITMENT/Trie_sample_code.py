# Trie(트라이) 문제
# 트리 자료 구조의 일종
# 각 Node 는 글자를 갖는 key = 한 글자, 단어의 마지막 글자인지 알려주는 flag(Terminal)로 구성

class Node(object):
    """
    A node that consists of a trie.
    """

    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        print(self.key)


# Trie 구현
# insert(string) : 트라이에 문자열 삽입
# search(string) : 주어진 단어 string 이 트라이에 존재하는지 여부 반환
# starts_with(prefix) : 주어진 prefix 로 시작하는 단어들을 BFS 로 트라이에서 찾아 리트스 형태로 반환

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    """
    트라이에 문자열을 삽입합니다.
    """
    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]

            # string 의 마지막 글자 차례이면,
            # 노드의 data 필드에 저장하려는 문자열 전체를 저장한다.
        curr_node.data = string

    
    """
    주어진 단어 string이 트라이에 존재하는지 여부를 반환합니다.
    """
    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        # string의 마지막 글자에 다달았을 때,
        # curr_node 에 data  가 있다면 string이 트라이에 존재하는 것!
        if (curr_node.data != None):
            return True
        
    """
    주어진 prefix 로 시작하는 단어들을
    트라이에서 찾아 리트스 형태로 반환합니다.
    """
    def starts_with(self, prefix):
        curr_node = self.head
        result = []
        subtrie = None

        # 트라이에서 prefix 를 찾고,
        # prefix 의 마지막 글자 노드를 subtrie 로 설정
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                subtrie = curr_node
            else:
                return None

        # bfs 로 prefix subtrie를 순환하며
        # data가 있는 노드들(=완전한 단어)를 찾는다.
        queue = list(subtrie.children.values())

        while queue:
            curr = queue.pop()
            if curr.data != None:
                result.append(curr.data)

            queue += list(curr.children.values())
        
        return result

trie = Trie()
trie.insert('abcde')
trie.insert('abcdef')
a = trie.starts_with('ab')
print(a)