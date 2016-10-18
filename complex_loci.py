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
                    return ''.join(eq_list[:x+1] + list(mod_to_abs(eq_list[x+1:y])) + eq_list[y:])

#TODO cant do equations of form |z-a|=|z-b|, a&b real since vertical line with infinite gradient
def parse(eq):
    eq=mod_to_abs(eq)
    eq=eq.replace('i','I').replace('z','Z')
    eq_list=list(eq)
    nums=['1','2','3','4','5','6','7','8','9','0']
    for n,ch in enumerate(eq_list):
        if (ch=='Z' or ch=='I' or ch=='A') and (eq_list[n-1] in nums):
            eq_list.insert(n,'*')
    eq=''.join(eq_list)
    eq=eq.replace('Z','(x+y*I)')
    return eq


#TODO add support for arg, use equation: 2atan((sqrt(x^2+y^2)-x)/y)

def get_lines(lhs,rhs):

    x,y=symbols('x y',real=True)
    locs={'x':x,'y':y}

    #LHS
    lhs=parse(lhs)
    lhs=sympify(lhs,locals=locs)
    print(lhs)

    #RHS
    rhs=parse(rhs)
    rhs=sympify(rhs,locals=locs)
    print(rhs)

    solns=list(solveset(lhs-rhs,locs['y']))
    if solns:
        typ='func'
    else:
        solns=list(solveset(lhs-rhs,locs['x']))
        typ='vert'
    return typ,solns



if __name__ == '__main__':
    equation="2|z-5i|=2|z-5|"
    LHS,RHS=equation.split('=')
    t1=time.time()
    lines=get_lines(LHS,RHS)
    t2=time.time()
    print(t2-t1,'ms')
    print(lines)

    #print(complexify(LHS+'-'+RHS))
