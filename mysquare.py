class Square:
    def __init__(self, n, i):
        self.n = n
        self.i = i
        self.x = i % 10
        self.y = i//10
        
    def get_n(self):
        return self.n
    def set_n(self, pn):
        self.n = pn
        
    def get_i(self):
        return self.i
    def set_i(self, pi):
        self.i = pi #hehe :D
        
    def get_x(self):
        return self.x
    def set_x(self, px):
        self.x = px
        
    def get_y(self):
        return self.y
    def set_y(self, py):
        self.y = py
