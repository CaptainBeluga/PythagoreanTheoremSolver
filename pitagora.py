import math

def ip(C,c):
    alfa=(C*C)+(c*c)
    beta=math.sqrt(alfa)
    return beta

def C(ip,c):
    alfa=(ip*ip)-(c*c)
    beta=math.sqrt(alfa)
    return beta

def c(ip,C):
    alfa=(ip*ip)-(C*C)
    beta=math.sqrt(alfa)
    return beta

#import math            //libreria
#math.sqrt(numero)      //metodo
