import numpy as np
import pandas as pd

df_xyz = pd.read_csv('CIE_DATASETS/CIE_xyz_1931_2deg.csv',names=['X','Y','Z'],index_col=0)
df_illum = pd.read_csv('CIE_DATASETS/CIE_std_illum_D65.csv',names=['D65'],index_col=0)
df_xyz = df_xyz.loc[360:780]
df_illum = df_illum.loc[360:780]
(Xw,Yw,Zw) = df_xyz.T.dot(df_illum['D65'])
(Xn,Yn,Zn)=(Xw/Yw*100,Yw/Yw*100,Zw/Yw*100)

def admittance(angle:float,n:np.ndarray,n0:np.ndarray=np.array([1.0]))->np.ndarray:
    """_summary_

    Parameters
    ----------
    angle : float
        _description_
    n : np.ndarray
        _description_
    n0 : np.ndarray, optional
        _description_, by default np.array([1.0])

    Returns
    -------
    np.ndarray
        _description_
    """    
    x = np.sqrt(np.power(n,2) - np.power(n0*np.sin(angle),2))
    return np.array([x,np.power(n,2)/x])

def matrix(angle:float,d:float,n:np.ndarray,n0:np.ndarray, M:np.ndarray=np.array([[1,0],[0,1]]))->np.ndarray:
    delta = np.array(2*np.pi*d*np.sqrt((np.power(n,2)-np.power(n0*np.sin(angle),2)))/n.index)
    sin = np.sin(delta)
    cos = np.cos(delta)
    eta = admittance(angle,n,n0)
    M = np.array([[M[0,0]*cos+M[0,1]*sin*eta*1j,M[0,0]*sin/eta*1j+M[0,1]*cos],
                  [M[1,0]*cos+M[1,1]*sin*eta*1j,M[1,0]*sin/eta*1j+M[1,1]*cos]])
    return M

def reflectance(angle:float,ns:np.ndarray,ds:list[float]=[],df:pd.DataFrame=pd.DataFrame(),n0:np.ndarray=np.array([1.0]))->np.ndarray:
    """_summary_

    Parameters
    ----------
    angle : float
        _description_
    ns : np
        _description_
    ndarray : _type_
        _description_
    ds : list[float], optional
        _description_, by default []
    df : pd.DataFrame, optional
        _description_, by default pd.DataFrame()
    n0 : np.ndarray, optional
        _description_, by default np.array([1.0])

    Returns
    -------
    np.ndarray
        _description_
    """    
    eta0 = admittance(angle,n0,n0)
    etas = admittance(angle,ns,n0)
    M = np.array([[1,0],[0,1]])
    for d,(_,n) in zip(ds,df.items()):
        M = matrix(angle,d,n,n0,M)
    B = M[0,0]+M[0,1]*etas
    C = M[1,0]+M[1,1]*etas
    r = np.power(np.abs((eta0*B-C)/(eta0*B+C)),2)
    return r

def spectrum_xyz(spec:np.ndarray)->pd.Series:
    return df_xyz.mul(df_illum['D65'],axis=0).T.dot(spec)/Yw*100

def xyz_lab(X:float,Y:float,Z:float)->tuple[float,float,float]:
    def f(t):
        return t**(1/3) if t > (6/29)**3 else 1/3*(29/6)**2*t+4/29
    fy = f(Y/Yn)
    return 116*fy-16,500*(f(X/Xn)-fy),200*(fy-f(Z/Zn))
