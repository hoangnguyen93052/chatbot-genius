import time
import random
import string

class Database:
    def __init__(self):
        self.data = {}
        self.index = {}

    def insert(self, key, value):
        self.data[key] = value
        self.index[key] = []  # Initialize empty index for the key

    def search(self, key):
        return self.data.get(key, None)

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            del self.index[key]

    def get_all_items(self):
        return self.data.items()

    def build_index(self):
        for key in self.data:
            self.index[key] = self._hash_function(key)

    def _hash_function(self, key):
        return hash(key) % 10  # Simple hash function for demonstration

    def get_index(self):
        return self.index

    def display_data(self):
        for key, value in self.data.items():
            print(f'Key: {key}, Value: {value}')

class BinaryTreeNode:
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = BinaryTreeNode(key, value)
        else:
            self._insert_recursively(self.root, key, value)

    def _insert_recursively(self, node, key, value):
        if key < node.key:
            if node.left is None:
                node.left = BinaryTreeNode(key, value)
            else:
                self._insert_recursively(node.left, key, value)
        elif key > node.key:
            if node.right is None:
                node.right = BinaryTreeNode(key, value)
            else:
                self._insert_recursively(node.right, key, value)

    def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursively(node.left, key)
        return self._search_recursively(node.right, key)

    def inorder_traversal(self):
        return self._inorder_recursively(self.root, [])

    def _inorder_recursively(self, node, acc):
        if node:
            self._inorder_recursively(node.left, acc)
            acc.append((node.key, node.value))
            self._inorder_recursively(node.right, acc)
        return acc

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key, value):
        index = self._hash_function(key)
        for tuple in self.table[index]:
            if tuple[0] == key:
                tuple[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self._hash_function(key)
        for tuple in self.table[index]:
            if tuple[0] == key:
                return tuple[1]
        return None

    def delete(self, key):
        index = self._hash_function(key)
        for i, tuple in enumerate(self.table[index]):
            if tuple[0] == key:
                del self.table[index][i]
                return

    def _hash_function(self, key):
        return hash(key) % self.size

    def display(self):
        for index, item in enumerate(self.table):
            print(f'Index {index}: {item}')

def generate_random_data(num_entries=100):
    random_data = {}
    for i in range(num_entries):
        key = ''.join(random.choices(string.ascii_letters, k=5))
        value = random.randint(1, 100)
        random_data[key] = value
    return random_data

def benchmark_indexing(database):
    start = time.time()
    for key, value in database.get_all_items():
        database.search(key)
    end = time.time()
    return end - start

def benchmark_btree(database):
    btree = BinaryTree()
    start = time.time()
    for key, value in database.get_all_items():
        btree.insert(key, value)
    for key in database.data.keys():
        btree.search(key)
    end = time.time()
    return end - start

def benchmark_hash_table(database):
    hash_table = HashTable()
    start = time.time()
    for key, value in database.get_all_items():
        hash_table.insert(key, value)
    for key in database.data.keys():
        hash_table.search(key)
    end = time.time()
    return end - start

def main():
    db = Database()
    random_data = generate_random_data(100)

    for key, value in random_data.items():
        db.insert(key, value)

    db.build_index()
    print("Database Index Built")
    db.display_data()
   
    print("Benchmarking Database Access:\n")

    db_time = benchmark_indexing(db)
    print(f'Database search time: {db_time:.5f} seconds')

    btree_time = benchmark_btree(db)
    print(f'Binary Tree search time: {btree_time:.5f} seconds')

    hash_time = benchmark_hash_table(db)
    print(f'Hash Table search time: {hash_time:.5f} seconds')

if __name__ == "__main__":
    main()