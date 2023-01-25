# # A filter for nicer outpput
#from re import  *
import re
math_str = re.compile("[\\\\^_]")
def math_filter(s, format=""):
    """Print a GiNaC output in a more readable way"""
    if isinstance(s,type([])):
        d = '[ %s' %s[0]
        for i in range(len(s)-1):
            d = d+ " , %s" %s[i+1]
        d = d+ " ]"
    else:
        d = s
    s1 = "%s" % d
    if is_latex_on():
        if re.search(math_str, s1):
            print(format+" $ \\displaystyle %s $ " %  s1)
        else:
            print(format+" %s" %  s1)
    else: # some additional replacements if LaTeX output is not used
        s1 = re.sub("\[cliffordunit object\]", "e", s1)
        s1 = re.sub("\*\[diracone object\]", "", s1)
        s1 = re.sub("\[diracone object\]\*", "", s1)
        s1 = re.sub("\[diracone object\]", "1", s1)
        s1 = re.sub("\(e~1\*e~0\)", "E", s1)
        s1 = re.sub("\(e\.1\*e\.0\)", "E", s1)
        s1 = re.sub("\(e~0\*e~1\)", "(-E)", s1)
        s1 = re.sub("\(e\.0\*e\.1\)", "(-E)", s1)
        s1 = re.sub("\],", "],\n", s1)
        s1 = re.sub("\*\*", "^", s1)
        print(format+" %s" % re.sub("\*", " ", s1))
    print("")

def draw_net(Exp,Var,X,Y,D,L,S,N=0):
    """Draw a net. draw_net(Exp,Var,X,Y,D,L,S,N=0)\n Exp expression\n Var list of variables to substitute\n X list of the first var limits\n Y list of the second var limits\n D number of dots on a line\n L number of lines \n S picture scaling\n N string for the output"""
    def make_curve(HN,D1,D2,DN,L1,L2,LN,S):
        if HN:
            H="path[] H="
        else:
            H="path[] V="
        for j in range(LN):
            if j>0:
                H=H+"^^"
            Fj=L1+1.0*(L2-L1)*j/(LN-1)
            for i in range(DN):
                if i>0:
                    H=H+".."
                Fi=D1+1.0*(D2-D1)*i/(DN-1)
                if HN:
                    T0=Exp.subs({Var[0] : Fi,Var[1] : Fj})
                else:
                    T0=Exp.subs({Var[0] : Fj,Var[1] : Fi})
                H=H+"(%s,%s)" % (S*T0.op(0).evalf(),S*T0.op(1).evalf())
        H=H+";"
        return H
    H=make_curve(True,X[0],X[1],D,Y[0],Y[1],L,S)
    V=make_curve(False,Y[0],Y[1],D,X[0],X[1],L,S)
    A=asy()
    A.send(H)
    A.send(V)
    A.send("draw(H,red)")
    A.send("draw(V,blue)")
    A.shipout("net%s" % N)
    del(A)


# Initialize Asymptote 

#from asymptote import *
#def open_asy(size=200):
#    """Open asy stream in a way suitable for cycles"""
#    A=asy()
#    A.size(size)
#    A.send("real u=5mm;")
#    return A

# Initialize cycle library and useful constants 
from cycle import *

#from figure import *

half=numeric(1,2)

a=realsymbol("a")
b=realsymbol("b")
c=realsymbol("c")
d=realsymbol("d")
r=realsymbol("r")
r1=realsymbol("r1","r'")
r2=realsymbol("r2","{r''}")

k=realsymbol("k")
l=realsymbol("L", "{l}") # Plain text l is not easy to distinguish from I or 1
n=realsymbol("n")
m=realsymbol("m")
k1=realsymbol("k1", "{k'}")
l1=realsymbol("l1", "{l'}")
n1=realsymbol("n1", "{n'}")
m1=realsymbol("m1", "{m'}")

x=realsymbol("x")
y=realsymbol("y")
t=realsymbol("t")

u=realsymbol("u")
v=realsymbol("v")
u1=realsymbol("u1", "{u'}")
v1=realsymbol("v1", "{v'}")
u2=realsymbol("u2", "{u''}")
v2=realsymbol("v2", "{v''}")

sign=realsymbol("si", "\\sigma")
sign1=realsymbol("bs", "\\sigma_1")
sign2=realsymbol("si2", "\\sigma_2")
sign3=realsymbol("si3", "\\sigma_3")
sign4=realsymbol("si4", "\\sigma_4")

s=realsymbol("s", "s")
s1=realsymbol("s1", "s_1")
s2=realsymbol("s2", "s_2")
s3=realsymbol("s3", "s_3")

M = diag_matrix([-1,sign])
M1 = diag_matrix([-1,sign1])
M2 = diag_matrix([-1,sign2])
M3 = diag_matrix([-1,sign3])
Mj = diag_matrix([-1,jump_fnct(sign)])
M1j = diag_matrix([-1,jump_fnct(sign1)])

sign_mat = diag_matrix([1,s])
sign_mat1 = diag_matrix([1,s1])
sign_mat2 = diag_matrix([1,s2])
sign_mat3 = diag_matrix([1,s3])

#P=matrix([[u, v]])
P=[u,v]

#P1=matrix([[u1, v1]])
P1=[u1,v1]

# The paravectorformalism with UseVectors=False is not yet compatible with the figure library
UseVectors=True
#UseVectors=False

#UseVaridx=True
UseVaridx=False

if (UseVectors):
    if (UseVaridx):
        print("Using vector formalism and varidx")
        mu=varidx(symbol("mu"),2)
        nu=varidx(symbol("nu"),2)
    else:
        print("Using vector formalism and idx")
        mu=idx(symbol("mu"),2)
        nu=idx(symbol("nu"),2)

    # Point space Clifford unit
    e=clifford_unit(mu,M)
    e0=e.subs({mu : 0})
    e1=e.subs({mu : 1})

    # Cycle space Clifford unit
    es=clifford_unit(nu,M1,1)
    es0=es.subs({nu : 0})
    es1=es.subs({nu : 1})

else:
    if (UseVaridx):
        print("Using paravector formalism and varidx")
        mu=varidx(symbol("mu"),1)
        nu=varidx(symbol("nu"),1)
    else:
        print("Using paravector formalism and idx")
        mu=idx(symbol("mu"),1)
        nu=idx(symbol("nu"),1)

    # Point space Clifford unit
    e=clifford_unit(mu,diag_matrix([sign]))
    e0=1
    e1=e.subs({mu : 0});

    # Cycle space Clifford unit
    es=clifford_unit(nu,diag_matrix([sign1]),1)
    es0=1
    es1=es.subs({nu : 0})
    
one=dirac_ONE();
ones=dirac_ONE(1);

rho=idx(symbol("rho"),2)
tau=idx(symbol("tau"),2)

# Clifford unit for focus/centre
er=clifford_unit(rho,M2,2);

# Clifford unit for transformations
et=clifford_unit(tau,M3,2);

ej=clifford_unit(varidx(symbol("eta"),2),Mj);

C=cycle2D(k,[l,n],m,e)
C1=cycle2D(k1,[l1,n1],m1,e)
Cr=cycle2D([u,v],e,r2)

# Unit circle
Cu=cycle2D(1,[0,0],1,e)
real_line=cycle2D(0,[0,1],0,e)

# Zero radius cycles
Z=cycle2D([u,v], e)
Z1=cycle2D([u1,v1], e)
Zinf=cycle2D(0,[0,0],1,e)

# Arbitrary elements of SL2
g=sl2_clifford(matrix([[a,b],[c,d]]),e)
gI=sl2_clifford(matrix([[d,-b],[-c,a]]),e)

# Initialisation of the Cayley transform

# The procedure for Cayley transform
def cayley(Cm, sigp, sigc):
    if (sigp==0): # Cayley transform in parabolic case is not similarity
        k=Cm.get_k()
        l=Cm.get_l(0)
        n=Cm.get_l(1)
        m=Cm.get_m()
        return cycle2D(k - 2*sigc*n, [l, n], m-2*n, C.get_metric())
    else:

#        return Cm.matrix_similarity(one, sign1*e1, -e1, one, e)
        Cf=cycle2D(sigp,[0,1],1,e)
        return Cm.cycle_similarity(Cf).cycle_similarity(real_line)

# Transformation of parabolic cycles under the Cayley transform
def cayley_parab(C, s=sign1):
    """Parabolic Cayley transform of cycles"""
    return cycle2D(C.get_k()-2*s*C.get_l(1),C.get_l(),C.get_m()-2*C.get_l(1),C.get_unit()) # second version with focal property

#    return cycle2D(C.get_k()-2*s*C.get_l(1),[C.get_l(0),C.get_l(1)],C.get_m()-2*C.get_l(1),C.get_unit())

def cayley_parab_I(C, s=sign1):
    """Parabolic inverse Cayley transform of cycles"""
    return cycle2D(C.get_k()+2*s*C.get_l(1),C.get_l(),C.get_m()+2*C.get_l(1),C.get_unit()) # second version with focal property

#    return cycle2D(C.get_k()+2*s*C.get_l(1),C.get_l(),C.get_m()+2*C.get_l(1),C.get_unit())

# Matrices definig the Cayley transforms 
#TC=matrix([[one,-e1],[sign1*e1,one]])
#TCI=matrix([[one,e1],[-sign1*e1,one]])
TC=matrix([[one,-e0/2],[sign1*e0/2,one]]) # second version with focal property
TCI=matrix([[one,e0/2],[-sign1*e0/2,one]]) # second version with focal property


# Infinitesimal number
epsilon=possymbol("eps", "\\epsilon")

# Definition of the sign1-infinitesimal cycle
def infinites_cycle(u, v, sign1, sign4=sign1):
    """ Definition of the sign1-infinitesimal cycle"""
    C=cycle2D(1, [u, n],  pow(u,2)+2*n*v-pow(n,2)*sign4, e)
    if (sign1==sign4):
        return cycle2D(C.subs({n : pow(epsilon,2)/2/v}))
    else:
        return cycle2D(C.subs({n : (v-sqrt(pow(v,2)-(sign4-sign1)*pow(epsilon,2)))/(sign4-sign1)}))
