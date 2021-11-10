class FunctionalDependency:
    def __init__(self, left_attributes_set, right_attributes_set):
        self.left_attributes_set = left_attributes_set
        self.right_attributes_set = right_attributes_set

    def __str__(self):
        return f"FunctionalDependency({self.left_attributes_set}, {self.right_attributes_set})"

    __repr__ = __str__


def is_lossless_join(relation_set, fds, sub_relation_1, sub_relation_2):
    # https://www.pythontutorial.net/python-basics/python-set-union/
    # check that it is a superkey
    # refactor in to function
    # by determining if each intersection is closure
    # closure algorithm
    # given each_intersection, what can I compute with it?
    # I am checking to see if I can compute all of relation_set columns, ie len(relation_set)
    # check condition 1:
    unioned = sub_relation_1.union(sub_relation_2)
    if len(unioned) != len(relation_set):
        return False

    # condition 2
    intersection1 = sub_relation_1.intersection(sub_relation_2)

    for each_intersection in intersection1:

        result = set(each_intersection)  # functionally determines itself
        new_result = {}

        while result != new_result:
            print((result))
            if new_result != {}:
                result = new_result
            new_result = {}

            for fd in fds:

                if each_intersection in fd.left_attributes_set:
                    if len(fd.left_attributes_set) > 1:
                        return False

                    # if any of the things in result are in fd.right_attribute_set: return False
                    for each_attribute in result:
                        if each_attribute in fd.right_attributes_set and len(fd.right_attributes_set) > 1:
                            # reduce return statements
                            return False

                    new_result = result.union(fd.right_attributes_set)

                    if new_result == sub_relation_1 or new_result == sub_relation_2:
                        return True

            if new_result == sub_relation_1 or new_result == sub_relation_2:
                return True
            else:
                break

    if new_result == sub_relation_1 or new_result == sub_relation_2:
        return True

    return False


relation_set = {"A", "B", "C", "D", "E", "F"}

fds = [

    FunctionalDependency({"A", "B"}, {"C", "D"}),

    FunctionalDependency({"C"}, {"D", "E"}),

]

subrelation_1 = {"A", "B", "C", "D"}

subrelation_2 = {"C", "D", "E", "F"}

assert not is_lossless_join(relation_set, fds, subrelation_1, subrelation_2)

# Another example

subrelation_1 = {"A", "B", "C", "D", "F"}

subrelation_2 = {"C", "D", "E"}
assert is_lossless_join(relation_set, fds, subrelation_1, subrelation_2)













relation_set = {"A", "B", "C", "D", "E"}

fds = [

    FunctionalDependency({"A"}, {"B", "C"}),

    FunctionalDependency({"C", "D"}, {"E"}),

    FunctionalDependency({"B"}, {"D"}),

    FunctionalDependency({"E"}, {"A"}),

]

subrelation_1 = {"A", "B", "C"}

subrelation_2 = {"A", "D", "E"}

assert is_lossless_join(relation_set, fds, subrelation_1, subrelation_2)

# Another example

subrelation_1 = {"A", "B", "C"}

subrelation_2 = {"C", "D", "E"}

assert not is_lossless_join(relation_set, fds, subrelation_1, subrelation_2)

relation_set = {"A", "B", "C", "D", "E"}

fds = [

    FunctionalDependency({"A"}, {"B", "C"}),

    FunctionalDependency({"C", "D"}, {"E"}),

    FunctionalDependency({"B"}, {"D"}),

    FunctionalDependency({"E"}, {"A"}),

]

subrelation_1 = {"B", "C", "D", "E"}

subrelation_2 = {"A", "E"}

assert is_lossless_join(relation_set, fds, subrelation_1, subrelation_2)

# Another example

subrelation_1 = {"A", "B", "C"}

subrelation_2 = {"E"}

assert not is_lossless_join(relation_set, fds, subrelation_1, subrelation_2)