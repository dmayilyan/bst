#!/usr/bin/python
# -*- coding: utf-8 -*-


class node:
    ''' One node '''
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


class bst:
    ''' Creation of the tree '''
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = node(value)
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child is None:
                cur_node.right_child = node(value)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print('Value is already in the tree.')

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left_child)
            print(cur_node.value)
            self._print_tree(cur_node.right_child)


def main():
    num_list = [113, 112, 1210, 121, 122, 1223]

    tree = bst()
    for i in num_list:
        tree.insert(i)

    tree.print_tree()

if __name__ == '__main__':
    main()
