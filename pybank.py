import pandas as pd 
import csv 

datos=pd.read_csv("/Users/leoalvarado/Desktop/databootcamp/Tarea 3/Homework 3_PyBank_Resources_budget_data.csv" )
print(datos['Date']) 

date_datos = datos['Date']
profit_losses = datos['Profit/Losses']

variacion =[]
for i in range(len(profit_losses)):
    if i<len(profit_losses)-1:
        variacion.append(profit_losses[i+1]- profit_losses[i])
     

print(f' "Profit" {sum(profit_losses)}')
print(f' "Promedio" {sum(variacion)/len(variacion )}')
print(f' "Numero de meses" {len(date_datos)}')
print(f' "Mayor variacion" {date_datos[variacion.index(max(variacion))]}')
print(f' "Valor de mayor variación " {max(variacion)}')
print(f' "Menor variacion" {date_datos[variacion.index(min(variacion))]}')
print(f' "Valor de menor variación " {min(variacion)}')
#print (date_datos[variacion.index(max(variacion))])


