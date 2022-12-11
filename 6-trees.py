class Node:
    '''
    Format the Node with data, content and links
    '''
    def __init__(self, account_number, balance):

        # Value to be traversed (data)
        self.account_number = account_number
        # Contentof node
        self.balance = balance
        self.left = None
        self.right = None

    # Format node for printing
    def __str__(self):
        return str(self.account_number) + ' ' + str(self.balance)

    
class SearchTree:
    def __init__(self):
        # Initialize empty tree
        self.root = None

    def insert(self, account_number, balance):

        # create a new node
        if self.root is None:
            self.root = Node(account_number, balance)
        # Start at root and create a new node
        else:
            self._insert(account_number, balance, self.root) 
    
    def _insert(self, account_number, balance, current_node):
        # Insert left
        if account_number < current_node.account_number:
            
            # Base case
            if current_node.left is None:
                current_node.left = Node(account_number, balance)
            # Recursive case down the left side
            else:
                self._insert(account_number, balance, current_node.left)
        
        # Insert right
        elif account_number > current_node.account_number:
            # Base case
            if current_node.right is None:
                current_node.right = Node(account_number, balance)
            # Recursive case doen the right side
            else:
                self._insert(account_number, balance, current_node.right)
        else:
            print('Account already exists')
    
    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)
    
    def _print_tree(self, current_node):
        # Print tree in order
        if current_node is not None:
            self._print_tree(current_node.left)
            print(current_node)
            self._print_tree(current_node.right)
    
    def search(self, account_number):
        # check if value is in tree
        if self.root is not None:
            return self._search(account_number, self.root)
        else:
            return None
    
    def _search(self, account_number, current_node):
        # Check if empty
        if account_number is None:
            return False
        # check if found
        elif account_number == current_node.account_number:
            return current_node
        # Check left, recursive case
        elif account_number < current_node.account_number and current_node.left is not None:
            return self._search(account_number, current_node.left)
        # Check right, recursive case
        elif account_number > current_node.account_number and current_node.right is not None:
            return self._search(account_number, current_node.right)

    
    def delete(self, account_number):
        if self.root is not None:
            self.root = self._delete(account_number, self.root)
    
    def _delete(self, account_number, current_node):
        
        # Traverse tree to find node
        if current_node is None:
            return current_node
        elif account_number < current_node.account_number:
            current_node.left = self._delete(account_number, current_node.left)
        elif account_number > current_node.account_number:
            current_node.right = self._delete(account_number, current_node.right)
        
        # Delete node
        else:
            # Case 1: No children
            if current_node.left is None and current_node.right is None:
                del current_node
                return None
            # Case 2: Single branch on right
            elif current_node.left is None:
                temp_node = current_node.right
                del current_node
                return temp_node
            # Case 2: Single branch on left
            elif current_node.right is None:
                temp_node = current_node.left
                del current_node
                return temp_node
            # Case 3: Left and Right
            else:
                temp_node = self.get_previous(current_node.left)
                current_node.account_number = temp_node.account_number
                current_node.balance = temp_node.balance
                current_node.left = self._delete(temp_node.account_number, current_node.left)
            
        return current_node
    
    def get_previous(self, current_node):
        if current_node.right is not None:
            return self.get_previous(current_node.right)
        return current_node
        
    def update(self, account_number, balance):
        # traverse tree to find node
        if self.root is not None:
            self._update(account_number, balance, self.root)
    
    def _update(self, account_number, balance, current_node):
        # Set new balance   
        if account_number == current_node.account_number:
            current_node.balance = balance
        # Check left, recursive case
        elif account_number < current_node.account_number and current_node.left is not None:
            self._update(account_number, balance, current_node.left)
        # Check right, recursive case
        elif account_number > current_node.account_number and current_node.right is not None:
            self._update(account_number, balance, current_node.right)

# Test 
print("________Test 1________")
tree = SearchTree()
tree.insert(9, 100)
tree.insert(2, 200)
tree.insert(3, 300)
tree.insert(5, 400)
tree.insert(4, 500)
tree.insert(6, 600)
tree.insert(7, 700)
tree.insert(8, 800)
tree.insert(1, 900)
tree.insert(10, 1000)


tree.print_tree()
print()
# Test 2
print()
print("________Test 2________")
print('Search for 5: ', tree.search(5))

# Test 3
print()
print("________Test 3________")
print('Search for 11: ', tree.search(11))

# Test 4
print()
print("________Test 4________")
tree.delete(1)
tree.delete(5)
tree.print_tree()

# Test 5
print("________Test 5________")
tree.update(6, 1000)
print()
tree.print_tree()