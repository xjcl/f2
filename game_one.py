from mylist import *

def main():
    q = Liste()
    print q.get_contents()
    q.append_next(11)
    print q.get_contents()
    q.go_fwd()
    print q.get_contents()
    q.append_next(3242)
    print q.get_contents()
    q.go_fwd()
    print q.get_contents()
    q.append_next(3442434322434)
    print q.get_contents()
    q.go_fwd()
    print q.get_contents()
    q.append_next(3333)
    print q.get_contents()
    q.go_fwd()
    print q.get_contents()
    q.go_fwd()
    print q.get_contents()
    
    print "-----"
    q.go_to_first()
    print q.get_contents()
    q.go_fwd()
    print q.get_contents()
    q.go_fwd()
    print q.get_contents()
    q.go_fwd()
    print q.get_contents()
    q.go_fwd()
    print q.get_total()
             
if __name__ == "__main__":
    main()
