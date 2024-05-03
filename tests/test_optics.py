import numpy as np
import pandas as pd
from optics import admittance,reflectance

def test_admittance():
    assert np.allclose(admittance(0,1.5,1.0), np.array([1.5,1.5]))
    assert np.allclose(admittance(np.pi/6,1.5,1.0),np.array([np.sqrt(2),1.5*1.5/np.sqrt(2)]))
    assert np.allclose(admittance(np.pi/3,1.0,1.0),np.array([0.5,2.0]))
    assert np.allclose(admittance(0,[1.5,1.5],1.0), np.array([[1.5,1.5],[1.5,1.5]]))
    assert np.allclose(admittance(np.pi/3,[1.0,1.0,1.0],1.0), np.array([[0.5,0.5,0.5],[2.0,2.0,2.0]]))
    assert np.allclose(admittance(0,1.5), np.array([1.5,1.5]))
    assert np.allclose(admittance(np.pi/3,[1.0,1.0,1.0]), np.array([[0.5,0.5,0.5],[2.0,2.0,2.0]]))

def test_reflectance():
    assert np.allclose(reflectance(0,1.5),np.array([0.04,0.04]))
    assert np.allclose(reflectance(0,[1.5,1.5]),np.array([[0.04,0.04],[0.04,0.04]]))
    assert np.allclose(reflectance(np.pi/6,1.0),np.array([0.0,0.0]))
    assert np.allclose(reflectance(0,[1.5],[100],pd.DataFrame([1.5],index=[550])),np.array([0.04,0.04]))
    assert np.allclose(reflectance(0,[1.5],[100],pd.DataFrame([1.0],index=[550])),(0.04,0.04))
    assert np.allclose(reflectance(0,[1.5],[100,100],pd.DataFrame([[1.0,1.0]],index=[550])),(0.04,0.04))
    assert np.allclose(reflectance(0,[1.5],[100,100],pd.DataFrame([[1.5,1.5]],index=[550])),(0.04,0.04))
    assert np.allclose(reflectance(0,[1.5],[100,100],pd.DataFrame([[1.0,1.5]],index=[550])),(0.04,0.04))
    assert np.allclose(reflectance(0,[1.5,1.5],[100,100],pd.DataFrame([[1.5,1.5],[1.5,1.5]],index=[550,600])),[(0.04,0.04),(0.04,0.04)])
    assert np.allclose(reflectance(np.pi/6,[1.5],[100],pd.DataFrame([1.5],index=[550])),reflectance(np.pi/6,[1.5]))
    assert np.allclose(reflectance(np.pi/3,[1.5],[100],pd.DataFrame([1.5],index=[550])),reflectance(np.pi/3,[1.5]))
    assert np.allclose(reflectance(np.pi/3,[1.5],[100],pd.DataFrame([1.0],index=[550])),reflectance(np.pi/3,[1.5]))