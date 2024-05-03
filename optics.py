import numpy as np
import pandas as pd

def admittance(angle,n,n0=np.array([1.0])):
    x = np.sqrt(np.power(n,2) - np.power(n0*np.sin(angle),2))
    return np.array([x,np.power(n,2)/x])

def reflectance(angle,ns,ds=[],df=pd.DataFrame(),n0=np.array([1.0])):
    eta0 = admittance(angle,n0,n0)
    etas = admittance(angle,ns,n0)
    M = np.array([[1,0],[0,1]])
    for d,(_,n) in zip(ds,df.items()):
        delta = np.array(2*np.pi*d*np.sqrt((np.power(n,2)-np.power(n0*np.sin(angle),2)))/n.index)
        sin = np.sin(delta)
        cos = np.cos(delta)
        eta = admittance(angle,n,n0)
        M = np.array([[M[0,0]*cos+M[0,1]*sin*eta*1j,M[0,0]*sin/eta*1j+M[0,1]*cos],
                      [M[1,0]*cos+M[1,1]*sin*eta*1j,M[1,0]*sin/eta*1j+M[1,1]*cos]])
        
    B = M[0,0]+M[0,1]*etas
    C = M[1,0]+M[1,1]*etas
    r = np.power(np.abs((eta0*B-C)/(eta0*B+C)),2)
    return r