from f2 import *
import random
from f2_file_loader import *

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

def main():
    print
    print "Running."
    print
    topi = 0
    movelist = []
    for topi in range(100):
        left_off = [0, 0, "r"]
        a = new_field()
        movelist.append("new")
        while not field_is_all_zeros(a):
            print "Whaddaya wanna do?"
            print_field(a)
            if len(a)>100:
                break
            the_input = get_move(a)#TODO , left_off get_move(a, left_off)
            print "--> " + the_input
            print
            if the_input == "copy" or the_input == "c":
                a = do_copy(a)
                movelist.append("copy")
            else:
                points = interpret_and_check(a, the_input)
                if points:
                    a = do_pop(a, points)
                    movelist.append(points)
                else:
                   print "You suck at input.\nIf you need instructions on how to get through the hotels,\n" + \
                   "check out the enclosed instruction TXT-file."
        if field_is_all_zeros(a):
            print movelist
            f = open('Solution_1.txt', 'wt')
            f.writelines(str(movelist))
            f.close()
            break
        
if __name__ == "__main__":
    main()
