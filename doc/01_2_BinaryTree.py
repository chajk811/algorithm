## 이진 탐색 트리 구현
# 이진 탐색 트리(binary search tree)는 이진트리의 특수한 경우이다.
# 모든 노드에 대해 그 왼쪽 자식들의 값이 현재 노드 값보다 작거나 같으며,
# 그 오른쪽 자식들의 값이 현재 노드의 값보다 크다는 조건을 만족하는 이진 트리
# 참고 : http://ejklike.github.io/2018/01/09/traversing-a-binary-tree-1.html

## 클래스 정의
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # 이제 여기에 원소를 추가, 탐색할 수 있도록
    # insert(), delete(), find() 메서드를 추가

    '''
    삽입 메서드
    '''
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node
    
    '''
    탐색 메서드
    원하는 값의 존재 유무를 확인할 수 있도록 구현
    '''
    def find(self, key):
        return self._find_value(self.root, key)
    
    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.right, key)
        else:
            return self._find_value(root.left, key)

    '''
    삭제 메서드
    삭제할 노드의 자식이 없으면 문젝 없다.
    자식이 하나인 경우엔 자식 노드를 삭제한 노드 위치로 가져오면 된다.
    자식이 두개일 경우, 왼쪽 서브 트리와 오른쪽 서브 트리를 A, B라고 하자.
    이때, B에서 가장 왼쪽아래에 위치한 자손을 가져오면 된다.
    이 원소는 A의 모든 원소들 보다 크면서, B의 나머지 원소보다 작다.
    '''
    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
