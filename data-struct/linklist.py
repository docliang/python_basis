#定义链表节点
class _Node:
    __slots__ = '_element','_next'

    def __init__(self,element,next):
        self._element = element
        self._next = next

#头插
def add_first(L,e):
    newset = _Node(e)
    newset._next = L.head
    L.head = newset
    L.size += 1
