class Node(object):
    def __init__(self, node_key, val):
        self.node_key = node_key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, max_size: int):
        self.head = Node('head', 'head')
        self.tail = Node('tail', 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.max_size = max_size
        self.curr_size = 0
        self.node_lookup = {}

    def removeNode(self, node):
        node_after = node.next
        node_before = node.prev
        node_before.next = node_after
        node_after.prev = node_before

    def moveToEnd(self, node):
        prev_node_tail = self.tail.prev
        prev_node_tail.next = node
        node.prev = prev_node_tail
        node.next = self.tail
        self.tail.prev = node

    def get(self, node_key: int) -> int:
        if node_key not in self.node_lookup:
            return -1
        node = self.node_lookup[node_key]
        node_val = node.val
        self.removeNode(node)
        self.moveToEnd(node)
        return node_val

    def put(self, node_key: int, new_val: int) -> None:
        if node_key in self.node_lookup:
            node = self.node_lookup[node_key]
            node.val = new_val
            self.removeNode(node)
            self.moveToEnd(node)
        else:
            if self.curr_size >= self.max_size:
                lru_node = self.head.next
                del self.node_lookup[lru_node.node_key]
                self.removeNode(lru_node)
                self.curr_size -= 1

            new_node = Node(node_key, new_val)
            self.node_lookup[node_key] = new_node
            self.moveToEnd(new_node)
            self.curr_size += 1
