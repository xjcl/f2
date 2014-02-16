from f2 import *
import random
from f2_file_loader import *
from f2_tree_handler import *
from f2_tree_data import *

import copy # <<< why is this to be imported? this is, like, the most useful thing ever!

def compose(pt, direct):
    if direct == "c":
        return "c"
    return str(pt[1])+" "+str(pt[0])+" "+direct

def get_move(pa):
    if random.randint(0, 10000) != 1:
        p1 = random.randint(0, len(pa)-1) #randint goes from a <= n <= b
        p2 = random.randint(0, len(pa[0])-1)
        cmd = random.choice(["u", "d", "l", "r"])
        return compose([p1, p2], cmd)
    return "c"
    
def get_moves(pa):
    ret = []
    for y in range(len(pa)):
        for x in range(len(pa[0])): # checks too many but whatevs
            for wrd in ["d", "r"]:
                ret.append(str(x)+" "+str(y)+" "+wrd)
    return ret

def make_tree(ca, lTree):
    for movestr in get_moves(ca): # get all im- and possible moves
        two_pts = interpret_and_check(ca, movestr)
        if two_pts:
            #new_a = copy.deepcopy(ca)
            new_a = ca
            print lTree.get_id()
            #print lTree.get_data().get_field()
            new_a = do_pop(ca, two_pts)
            lTree.add_node(Point_Data(two_pts, copy.deepcopy(new_a)))
            if field_is_all_zeros(lTree.get_node(-1).get_data().get_field()):
                f = open('Tree_solution_000.txt', 'wt')
                f.writelines(lTree.get_node(-1).get_id())
                f.close()
                raise SystemExit # because fuck you that's why
            if len(lTree.get_id()) < 10:#260:
                #if lTree.get_id() == []:
                #    if len(lTree.follower)==5:
                #        make_tree(copy.deepcopy(new_a), lTree.get_node(-1))
                #else:
                make_tree(copy.deepcopy(new_a), lTree.get_node(-1))
    #new_a = copy.deepcopy(ca) # finally, copy once from every possible position
    new_a = ca
    new_a = do_copy(new_a)
    lTree.add_node(Point_Data("c", copy.deepcopy(new_a)))
    if len(lTree.get_id()) < 10:#260:
        make_tree(copy.deepcopy(new_a), lTree.get_node(-1))
    #del lTree
    #del new_a
    #del ca

def main():
    print
    print "Running."
    print
    a = new_field()
    the_tree = Tree(Point_Data([[], [], ""], a), []) # empty points and init field (unimportant) and id (yes important)
    make_tree(copy.deepcopy(a), the_tree)
    print a, id(a)
    print the_tree.get_data().get_field()
    the_tree.write_tree_to_file("treetest")
    #f = open('REAL_SOLUTION.txt', 'wt')
    #f.writelines(str(movelist))
    #f.close()
    print "Done."
    print
        
if __name__ == "__main__":
    main()
