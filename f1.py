from mydoublelist import *

def main():
    q = Liste()
    
    a = 00
    b = 01
    c = 10
    d = 11
    
    q.append_next(a)
    q.append_next2(a)
    q.go_fwd()
    #N -<a>- N
    q.append_next2(b)
    q.go_fwd2()
    #N - a - N
    #   <b>
    
    print q.get_contents()

             
if __name__ == "__main__":
    main()  
