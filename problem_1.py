import sys


class Stack:
    '''
    implementation of a stack
    '''

    def __init__(self):
        self.store = []

    def push(self, item):
        self.store.append(item)

    def pop(self):
        return self.store.pop()

    def isempty(self):
        return not self.store


class BinaryTree:
    '''
    implementation of a Binary Tree
    '''

    def __init__(self, rootid):
        self.left = None
        self.right = None
        self.rootid = rootid

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_node_value(self, value):
        self.rootid = value

    def get_node_value(self):
        return self.rootid

    def insert_right(self, new_node):
        if self.right is None:
            self.right = BinaryTree(new_node)
        else:
            tree = BinaryTree(new_node)
            tree.left = self.right
            self.right = tree

    def insert_left(self, new_node):
        if self.left is None:
            self.left = BinaryTree(new_node)
        else:
            tree = BinaryTree(new_node)
            tree.left = self.left
            self.left = tree


class MathParser:
    def __init__(self):
        # map operators to functions
        self.operate = {
            "+": self.add,
            "-": self.sub,
            "*": self.mul,
            "/": self.div
        }
        self.priority = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2
        }

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def build_parse_tree(self, exp):
        '''
        Builds a binary tree from a mathematical expression
        :param exp:
        :return exptree:
        '''
        # parse expression by using spaces as delimiters
        fplist = exp.split()
        if fplist[0] is not '(':
           fplist = ['('] + fplist + [')']

        # initialize Stack and Tree
        pstack = Stack()
        exptree = BinaryTree('')
        pstack.push(exptree)
        current_tree = exptree

        # loop through operands and operators to generate binary parse tree
        for i in fplist:
            if i == '(':
                current_tree.insert_left('')
                pstack.push(current_tree)
                current_tree = current_tree.get_left_child()
            elif i not in ['+', '-', '*', '/', ')']:
                current_tree.set_node_value(float(i))
                parent = pstack.pop()
                current_tree = parent
            elif i in ['+', '-', '*', '/']:
                if current_tree.get_node_value() in ['+', '-', '*', '/']:
                    # simplify tree if a lower priority operator is encountered
                    if self.priority[i] < self.priority[current_tree.get_node_value()]:
                        val = self.evaluate(exptree)
                        pstack = Stack()
                        exptree = BinaryTree('')
                        pstack.push(exptree)
                        current_tree = exptree
                        current_tree.insert_left('')
                        pstack.push(current_tree)
                        current_tree = current_tree.get_left_child()
                        current_tree.set_node_value(val)
                        parent = pstack.pop()
                        current_tree = parent
                        current_tree.set_node_value(i)
                        current_tree.insert_right('')
                        pstack.push(current_tree)
                        current_tree = current_tree.get_right_child()

                    else:
                        current_tree.insert_right(i)
                        pstack.push(current_tree)
                        current_tree = current_tree.get_right_child()
                        pstack.push(current_tree)
                        current_tree.insert_right('')
                        current_tree = current_tree.get_right_child()
                else:
                    current_tree.set_node_value(i)
                    current_tree.insert_right('')
                    pstack.push(current_tree)
                    current_tree = current_tree.get_right_child()
            elif i == ')':
                current_tree = pstack.pop()
            else:
                raise ValueError
        return exptree

    def evaluate(self, parse_tree):
        '''
        Evaluates a parse tree

        :param parse_tree:
        :return:
        '''
        left_c = parse_tree.get_left_child()
        right_c = parse_tree.get_right_child()

        if left_c and right_c:
            fn = self.operate[parse_tree.get_node_value()]
            return fn(self.evaluate(left_c), self.evaluate(right_c))
        else:
            return parse_tree.get_node_value()

# unit test python problem_1.py '2 + 4 / 9' -> 2.44444444444
# unit test python problem_1.py '3 + 4 - 9 * ( 3 / 8 / ( 2 + 9 ) )'  -> -30.125
def main():
    expression = sys.argv[1]
    parser = MathParser()
    tree = parser.build_parse_tree(expression)
    print(parser.evaluate(tree))


if __name__ == '__main__':
    main()
