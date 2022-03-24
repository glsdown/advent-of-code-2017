tower = []

with open("Day7Input.txt", "r") as f:
    for line in f:
        tower.append(line.strip().split())

# Round 2
class Tree(object):
    "Generic tree node."

    def __init__(self, name="root", weight=0, children=None):
        self.name = name
        self.weight = weight
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
            self.weight_plus_children = self.get_all_weight()
            self.balanced = (
                len(list(set([child.weight_plus_children for child in self.children])))
                == 1
            )
            if not self.balanced:
                print("Unbalanced...", self.name)
                print([child.weight_plus_children for child in self.children])
                print([child.name for child in self.children])
        else:
            self.balanced = True

    def __repr__(self):
        return self.name

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

    def get_all_weight(self):
        if self.children is None:
            return self.weight
        else:
            self.weight_plus_children = self.weight
            for child in self.children:
                print
                "child.get_all_weight()", child.get_all_weight()
                self.weight_plus_children += child.get_all_weight()

        return self.weight_plus_children


root = "ykpsek"  # "tknk"#
disc_names = [item[0] for item in tower]
dependencies = {}
disc_weights = {}

for i in range(len(tower)):
    if "->" in tower[i]:
        to_add = []
        for j in range(3, len(tower[i])):
            to_add.append(tower[i][j].split(",")[0])
        dependencies[disc_names[i]] = to_add
    else:
        dependencies[disc_names[i]] = None
    disc_weights[disc_names[i]] = int(tower[i][1][1:-1])


def create_tree(my_tree):
    if dependencies[my_tree] == None:
        return Tree(my_tree, disc_weights[my_tree], None)
    else:
        return Tree(
            my_tree,
            disc_weights[my_tree],
            [create_tree(i) for i in dependencies[my_tree]],
        )


my_tree = create_tree(root)

# Round 1
#
# top_row = []
# dependencies = {}
#
# for i in range(len(tower)):
#     if '->' in tower[i]:
#         to_add = []
#         for j in range(3, len(tower[i])):
#             to_add.append(tower[i][j].split(",")[0])
#         dependencies[disc_names[i]] = to_add
#     else:
#         top_row.append(disc_names[i])
#
# while len(dependencies.keys()) > 2:
#     new_dependencies = {}
#     new_top_row = []
#
#     for item in dependencies.keys():
#         non_top = []
#         for value in dependencies[item]:
#             if value not in top_row:
#                 non_top.append(value)
#         if len(non_top) != 0:
#             new_dependencies[item] = [i for i in non_top]
#         else:
#             new_top_row.append(item)
#     dependencies = new_dependencies
#     top_row += new_top_row
#
# print(new_dependencies.keys())
