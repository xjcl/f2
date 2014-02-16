class Tree(object):
    def __init__(self, pdata, pid):
        self.follower = [] # insert Trees here
        self.data = pdata # while we're at it, let's make this a general purpose tree.
        self.id = pid
        
    def get_follower(self):
        return self.follower
    
    def get_id(self):
        return self.id
        
    def get_data(self):
        return self.data
        
    def add_node(self, pdata):
        llist = self.id[:] # copy list to local variable
        llist.append(len(self.follower))
        lTree = Tree(pdata, llist)
        self.follower.append(lTree)
        
    def get_node(self, num):
        return self.follower[num]
    
    def write_node_to_file(self, pf, ltree):
        pf.writelines(">")
        for level in ltree.id:
            pf.writelines(" "+str(level))
        pf.writelines("\n"+ltree.get_data().to_str()+"\n") # every inserted data must have a to_str()-method!
        for a_tree in ltree.follower:
            self.write_node_to_file(pf, a_tree)
        
    def write_tree_to_file(self, filename): # condition: data is a string
        f = open(filename+'.txt', 'wt')
        #f.writelines(">\n"+self.get_data()+"\n")
        self.write_node_to_file(f, self)
        f.close()
    
    def load_tree_from_file(self, filename):
        from shlex import split
        f = open(filename+'.txt', 'r')
        #f.writelines(">\n"+self.get_data()+"\n")
        fa = f.readlines()
        fa_ids = []
        fa_data = []
        for i in range(len(fa)):
            if i%2==0:
                to_append = split(fa[i])
                to_append.pop(0)
                fa_ids.append(to_append)
                print fa_ids
            else:
                fa_data.append(fa[i])
        f.close()
        # should this even be in here?
        # maybe divide trees (1) and nodes (infinite)?
        
if __name__ == "__main__":
    from f2_tree_data import *
    a = Tree(A_str("I AM A TREE"), [])
    a.load_tree_from_file("to_load")
if 7==1:
    from f2_tree_data import *
    a = Tree(A_str("I AM A TREE"), [])
    print a.id
    a.add_node(A_str("I am subtree. 'sub tree."))
    a.add_node(A_str("I am subtree 2 (or 1)."))
    curr = a.get_node(0)
    curr.add_node(A_str("two levels down"))
    print
    print a.get_data().to_str()
    print a.get_id()
    print a.get_node(0).get_data().to_str()
    print a.get_node(0).get_id()
    print a.get_node(1).get_data().to_str()
    print a.get_node(1).get_id()
    print a.get_node(0).get_node(0).get_data().to_str()
    print a.get_node(0).get_node(0).get_id()
    print
    print a.id
    a.write_tree_to_file("this")
