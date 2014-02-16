from shlex import split

def field_is_all_zeros(pa):
    for row in pa:
        for sq in row:
            if sq != 0:
                return False
    return True
    
def is_number(n):
    try:
        n = int(n)
        return True
    except: # error message thrown later
        return False

def don_exits(pa, pt): # does it exist?
    if pt[0] < len(pa):
        if pt[0] == len(pa)-1:
            if pt[1] < len(pa[-1]):
                return True
        else:
            if pt[1] < len(pa[0]):
                return True
    return False

def find_next(pa, pt, drctn):
    if drctn == "d":
        bottommost = len(pa)-1
        if not don_exits(pa, [bottommost, pt[1]]): bottommost -= 1
        for i in range(pt[0]+1, bottommost+1): # plus one to include bottommost, duh.
            if pa[i][pt[1]] != 0:
                return [i, pt[1]]
    if drctn == "u":
        for i in range(pt[0]-1, -1, -1):
            if pa[i][pt[1]] != 0:
                return [i, pt[1]]
    if drctn == "r":
        for i in range(pt[1]+9*pt[0] + 1, 9*(len(pa)-1) + len(pa[-1])-1 + 1):
            if pa[i//9][i%9] != 0:
                return [i//9, i%9]
    if drctn == "l":
        for i in range(pt[1]+9*pt[0] - 1, -1, -1):
            if pa[i//9][i%9] != 0:
                return [i//9, i%9]
                    
def interpret_and_check(pa, ps):
    words = split(ps) # our shlex.split()
    ret = []
    if len(words) == 3:
        if is_number(words[0]) and is_number(words[1]): # x and y, in that order
            words[0], words[1] = int(words[0]), int(words[1])
            pt = [words[1], words[0]] # y and x
            if don_exits(pa, pt):
                if words[2] == "up" or words[2] == "left" or words[2] == "u" or words[2] == "l":
                    ret = [find_next(pa, pt, words[2][0]), pt] # flip x/y (internal order)
                if words[2] == "down" or words[2] == "right"or words[2] == "d" or words[2] == "r":
                # strange charm top bottom. If you don't know what a quark is ...
                    ret = [pt, find_next(pa, pt, words[2][0])]
        if ret and ret[0] and ret[1]:
            if len(ret) == 2 == len(ret[0]) == len(ret[1]):
                if (pa[ret[0][0]][ret[0][1]] == pa[ret[1][0]][ret[1][1]]) or \
                (pa[ret[0][0]][ret[0][1]] == 10 - pa[ret[1][0]][ret[1][1]]):
                    return ret
            
def new_field():
    return [[1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 1, 1, 2, 1, 3, 1, 4, 1],
            [5, 1, 6, 1, 7, 1, 8, 1, 9]]
    
def print_field(pa):
    ij = 0
    print
    print "    0 1 2 3 4 5 6 7 8"
    print "    -----------------"
    for row in pa:
        print "   ",
        for sq in row:
            if sq == 0:
                print " ",
            else:
                print str(sq),
        print "| %d" % ij
        ij += 1
    print "  "

def do_pop(aa, pts):
    pt1, pt2 = pts
    aa[pt1[0]][pt1[1]], aa[pt2[0]][pt2[1]] = 0, 0
    return aa
    
def do_copy(ba):
    la = []
    for row in ba:
        for sq in row:
            if sq != 0:
                la.append(sq)
    max_num = 9*(len(ba)-1) + len(ba[-1])-1
    for i in range(max_num+1, max_num+len(la)+1):
        if len(ba[-1]) == 9:
            ba.append([la[i-(max_num+1)]])
        else:
            ba[-1].append(la[i-(max_num+1)])
    return ba

def main():
    print
    print "Welcome."
    print
    print "Enter an x-variable, then an y-variable,\nand then either 'u', 'd', 'l' or 'r'.\n\
If you don't want to play a move,\nyou can input 'c' to copy all numbers to the end.\n\
If I already managed to bore you, type 'e'.\n"
    a = new_field()
    while not field_is_all_zeros(a):
        print "Whaddaya wanna do?"
        print_field(a)
        the_input = raw_input("--> ") # < only place where moves are in [x, y] format.
        print
        if the_input == "exit" or the_input == "eoj" or the_input == "die" or the_input == "e":
            break
        elif the_input == "copy" or the_input == "c":
            a = do_copy(a)
        else:
            points = interpret_and_check(a, the_input)
            if points:
                a = do_pop(a, points)
            else:
               print "You suck at input.\nIf you need instructions on how to get through the hotels,\n" + \
               "check out the enclosed instruction TXT-file."
        
if __name__ == "__main__":
    main()
