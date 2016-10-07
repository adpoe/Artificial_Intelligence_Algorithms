from ast import literal_eval
import sys

##########################
###### MINI-MAX A-B ######
##########################



##########################
###### PARSE DATA ########
##########################
def parse_data_as_list(fname):
    with open(fname, "r") as f:
        data_as_string = f.read()
        print data_as_string
        data_list = literal_eval(data_as_string)
    return data_list


class GameNode:
    def __init__(self, name, value=0, parent=None):
        self.Name = name      # a char
        self.value = value    # an int
        self.parent = parent  # a node reference
        self.children = []    # a list of nodes

    def addChild(self, childNode):
        self.children.append(childNode)


# maybe make leaf and tree nodes?

class GameTree:
    def __init__(self):
        self.root = None

    def build_tree(self, data_list):
        """
        :param data_list: Take data in list format
        :return: Parse a tree from it
        """
        self.root = GameNode(data_list.pop(0))
        for elem in data_list:
            self.parse_subtree(elem, self.root)

    def parse_subtree(self, data_list, parent):
        # base case
        if type(data_list) is tuple:
            # make connections
            leaf_node = GameNode(data_list[0])
            leaf_node.parent = parent
            parent.addChild(leaf_node)
            # if we're at a leaf, set the value
            if len(data_list) == 2:
                leaf_node.value = data_list[1]
            return

        # recursive case
        tree_node = GameNode(data_list.pop(0))
        # make connections
        tree_node.parent = parent
        parent.addChild(tree_node)
        for elem in data_list:
            self.parse_subtree(elem, tree_node)

        # return from entire method if base case and recursive case both done running
        return




##########################
#### MAIN ENTRY POINT ####
##########################

def main():
    filename = sys.argv[1]
    print "hello world! " + filename
    data_list = parse_data_as_list(filename)
    #data_tree = build_game_tree(data_list)
    data_tree = GameTree()
    data_tree.build_tree(data_list)
    print "build a tree.."

if __name__ == "__main__":
    main()
