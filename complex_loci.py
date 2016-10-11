from sympy import *

def eval_mod(eq):
    print('call',eq)
    if '|' not in eq:
        locs={}
        locs['x'],locs['y']=symbols('x y',real=True)
        a=sympify(eq,locals=locs)
        print(a)
        print('('+str(sqrt(re(a)**2+im(a)**2))+')')
        return '('+str(sqrt(re(a)**2+im(a)**2))+')'
    for x,char in enumerate(eq):
        if char=='|':
            l=list(eq)
            l[x]='('
            eq=''.join(l)
            for y,char2 in reversed(list(enumerate(eq))):
                if char2=='|':
                    l=list(eq)
                    l[y]=')'
                    eq=''.join(l)
                    print('inner:',eq[x+1:y])
                    return eq[:x+1] + eval_mod(eq[x+1:y]) + eq[y:]

def mod_to_abs(eq):
    if '|' not in eq:
        return eq
    for x,char in enumerate(eq):
        if char=='|':
            l=list(eq)
            l[x]='Abs('
            eq=''.join(l)
            for y,char2 in reversed(list(enumerate(eq))):
                if char2=='|':
                    l=list(eq)
                    l[y]=')'
                    eq=''.join(l)
                    print('inner:',eq[x+1:y])
                    return eq[:x+1] + eval_mod(eq[x+1:y]) + eq[y:]
#FIXME fix recursion, |z-|5i+4|| only evaluates inner mod

def complexify(equation):
    equation=equation.replace('z','(x+y*I)').replace('i','I')

    equation=eval_mod(equation)

    locs={}
    locs['x'],locs['y']=symbols('x y',real=True)

    eq=sympify(equation,locals=locs)

    print(eq,type(eq))

    solns = solve(eq,locs['y'])

    x,y=symbols('x y',real=True)
    eq2=sympify(mod_to_abs(equation),locals=locs)
    print()
    print('eq2:',eq2)
    print('solveset: ',solveset(eq2,locs['y']))

    return solns

#USE SOLVESET, JUST MAKE MOD LINES DO ABS() INSTEAD

#>>> solveset(Abs(x+y*I)-5,y)
#{-sqrt(-(x - 5)*(x + 5)), sqrt(-(x - 5)*(x + 5))}


if __name__ == '__main__':
    LHS,RHS='|z-|5+i||','5'
    print(complexify(LHS+'-'+RHS))
