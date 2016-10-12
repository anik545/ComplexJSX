from sympy import *
import time

def mod_to_abs(eq):
    eq_list=[str(x) for x in eq]
    if '|' not in eq:
        return eq
    for x,char in enumerate(eq_list):
        if char=='|':
            eq_list[x]='Abs('
            for y,char2 in reversed(list(enumerate(eq))):
                if char2=='|':
                    eq_list[y]=')'
                    return ''.join(eq_list[:x+1] + mod_to_abs(eq_list[x+1:y]) + eq_list[y:])


#FIXME fix recursion, |z-|5i+4|| only evaluates inner mod

def get_lines(lhs,rhs):

    x,y,z=symbols('x y z',real=True)

    #Do lhs first
    lhs=mod_to_abs(lhs)
    lhs=lhs.replace('i','I')
    lhs=sympify(lhs).subs('z',x+y*I)

    #Now rhs
    rhs=mod_to_abs(rhs)
    rhs=rhs.replace('i','I')
    rhs=sympify(rhs).subs('z',x+y*I)

    solns=list(solveset(lhs-rhs,y))
    return solns

if __name__ == '__main__':
    equation="|z-5*i|=|z-25|"
    LHS,RHS=equation.split('=')
    t1=time.time()
    lines=get_lines(LHS,RHS)
    t2=time.time()
    print(t2-t1,'ms')
    print(lines)

    #print(complexify(LHS+'-'+RHS))
