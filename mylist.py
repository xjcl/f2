# updated 2013-03-13
# in templates and
### f1
class Liste:
    class Knoten:
        def __init__(self, pcontents):
            self.set_contents(pcontents)
            self.prev = None
            self.next = None
            
        def cut_it(self): #cut self.
            self.get_contents()
            
        def get_contents(self):
            return self.contents
        def set_contents(self, pcontents):
            self.contents = pcontents
            
        def get_next(self):
            return self.next
        def set_next(self, pnext):
            self.next = pnext
        
        def get_prev(self):
            return self.prev
        def set_prev(self, pprev):
            self.prev = pprev   
            
            
            
        
        
            
    def __init__(self):
            self.pre = self.Knoten(None)
            self.post = self.Knoten(None)
            self.pre.set_next(self.post)
            self.post.set_prev(self.pre)
            self.curr = self.pre
            self.total = 0
            
    def get_total(self):
        return self.total
            
    def is_empty(self):
        return self.total == 0
    
    def go_to_first(self):
        self.curr = self.pre.get_next()
    def go_to_last(self):
        self.curr = self.post.get_prev()
    
    def is_pre(self):
        return self.curr == self.pre
    def is_post(self):
        return self.curr == self.post
        
    def go_fwd(self):
        if not self.is_post():
            self.curr = self.curr.get_next()
    def go_bwd(self):
        if not self.is_pre():
            self.curr = self.curr.get_prev()
    
    def get_contents(self):
        return self.curr.get_contents()
        
    def append_next(self, pobject): # append w/o moving
        if not self.is_post():
            lKnoten = self.Knoten(pobject)
            self.curr.get_next().set_prev(lKnoten)
            lKnoten.set_next(self.curr.get_next())
            self.curr.set_next(lKnoten)
            lKnoten.set_prev(self.curr)
            self.total += 1
        
    def append_prev(self, pobject): # append w/o moving
        if not self.is_pre():
            lKnoten = self.Knoten(pobject)
            self.curr.get_prev().set_next(lKnoten)
            lKnoten.set_prev(self.curr.get_prev())
            self.curr.set_prev(lKnoten)
            lKnoten.set_next(self.curr)
            self.total += 1
    
    def pop_curr(self): # throws you out after the deleted element
        if self.curr: #"None - x - None" works. "None - None" doesn't
            self.curr.get_prev().set_next(self.curr.get_next())
            self.curr.get_next().set_prev(self.curr.get_prev())
            self.curr = self.curr.get_next()
            self.total -= 1
