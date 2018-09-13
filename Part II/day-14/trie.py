# Exercise for the course UCSanDiegoX: ALGS204x
# String Processing and Pattern Matching Algorithms
#
#  Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.


def build_trie(patterns):
    tree = dict()
    last_index = 1
    for index, pattern in enumerate(patterns):
        node = dict()
        for c in pattern:
            if pattern in node.values():
                node[index] = c
            else:
                node[last_index] = c
            last_index += 1
        tree[index] = node
    return tree