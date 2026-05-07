import xlwings as xw
import numpy as np

wb = xw.Book('Proyectos de inversion.xlsx')
FC = wb.sheets['Flujo de Caja']

Precio=FC.range("B19").value
CV=FC.range("B20").value
Tasa=FC.range("B23").value

VarVentas1=0.5
VarVentas2=0.55
VarVentas3=0.60
VarVentas4=0.70
VarVentas5=0.85
VarVentas6=1
VarVentas7=1
VarVentas8=1
desv=0.095
n_sim = 10000
sim_van = []
sim_rec = []
celda_van = "I46"
celda_tir = "I47"
celda_rec = "I49"
celda_vanf = "I51"
inputs = []
ventasx = []
prob=[]
precio_sim= []
CV_sim= []
flag_sim=[]

for i in range(n_sim):
    app = xw.apps.active
    app.calculation = 'manual'
    preciox = np.random.normal(5,desv)
    cvx=np.random.normal(2.2,0.05)
    inputs = [[preciox],[cvx]]
    ventas = [
        [np.clip(np.random.normal(VarVentas1, desv), 0, 1)],
        [np.clip(np.random.normal(VarVentas2, desv), 0, 1)],
        [np.clip(np.random.normal(VarVentas3, desv), 0, 1)],
        [np.clip(np.random.normal(VarVentas4, desv), 0, 1)],
        [np.clip(np.random.normal(VarVentas5, desv), 0, 1)],
        [np.clip(np.random.normal(VarVentas6, desv), 0, 1)],
        [np.clip(np.random.normal(VarVentas7, desv), 0, 1)],
        [np.clip(np.random.normal(VarVentas8, desv), 0, 1)]]
    FC.range("B31").value=ventas
    FC.range("B19").value=inputs
    app.calculation = 'automatic'
    flag = FC.range("I52").value
    van=FC.range(celda_van).value
    tir=FC.range(celda_tir).value
    rec=FC.range(celda_rec).value
    vanf=FC.range(celda_vanf).value
    if van is None:
        van=0    
    if tir is None:
        tir=0
    if rec is None:
        rec=0
    if flag == 0: 
        sim_van.append(vanf)
    else:
        sim_van.append(van)

    sim_rec.append(rec)
    prob.append(1/n_sim)
    precio_sim.append(preciox)
    CV_sim.append(cvx)
    flag_sim.append(flag)

FC.range("AA2").options(transpose=True).value = sim_van
FC.range("AB2").options(transpose=True).value = prob
FC.range("AC2").options(transpose=True).value = sim_rec
FC.range("AD2").options(transpose=True).value = precio_sim
FC.range("AE2").options(transpose=True).value = CV_sim
FC.range("AF2").options(transpose=True).value = flag_sim
