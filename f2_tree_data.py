class Point_Data(object):
    def __init__(self, ppts, pfield):
        self.pts = ppts
        self.field = pfield
        
    def to_str(self):
        s = ""
        for pt in self.pts:
            for coord in pt:
                s += str(coord)
                s += " "
        return s
        
    def get_field(self):
        return self.field
        
        
        
        
class A_str(object):
    def __init__(self, ps):
        self.s = ps
    def to_str(self):
        return self.s
