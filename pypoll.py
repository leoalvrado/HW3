import pandas as pd 
import csv 
#convertir el archivo en un dataframe
df =pd.read_csv("/Users/leoalvarado/Desktop/databootcamp/Tarea 3/Homework 3_PyPoll_Resources_election_data.csv" )
print(df) 
#me da el numero de votos totales
datos_votes_df = len(df["Voter ID"])
print(f' "votos " {df}') 

#filtrar solo la columna de candidato
new_df = df.filter(["Candidate"])
print(new_df)
#khan
poll_Khan_df = new_df['Candidate']== 'Khan'
print(poll_Khan_df)
poll_Correy_df = new_df['Candidate']== 'Correy'
print(poll_Correy_df)
poll_Li_df = new_df['Candidate']== 'Li'
print(poll_Li_df)
poll_Otooley_df = new_df['Candidate']== "O'Tooley"
print(poll_Otooley_df)
#contar e imprimir los true 
true_count1 = sum(poll_Khan_df)
votos_Khan = (int(true_count1)/int(datos_votes_df))*100
print(f' "Kahn tuvo"  {true_count1} "votos"  {votos_Khan} "%"')
true_count2 = sum(poll_Correy_df)
votos_Correy = (int(true_count2)/int(datos_votes_df))*100
print(f' "Correy tuvo"  {true_count2} "votos"  {votos_Correy} "%"')
true_count3 = sum(poll_Li_df)
votos_Li = (int(true_count3)/int(datos_votes_df))*100
print(f' "Li tuvo"  {true_count3} "votos"  {votos_Li} "%"')
true_count4 = sum(poll_Otooley_df)
votos_Otooley = (int(true_count4)/int(datos_votes_df))*100
print(f' "Otooley tuvo"  {true_count4} "votos"  {votos_Otooley} "%"') 

print('Winner : Khan')
"""
poll_Khan = []
for i in range(len(df)):
    if i == 'Khan' :
       poll_Khan.append(i+1) 
    



print(poll_Khan) 
"""
    



#poll_Khan = datos_df.append(['Candidate'])
#print(poll_Khan)

'''
poll_Khan = []

for i in range(len(datos_votes)) :
    poll_Kahn.append(i[0:i.find('Khan')])
    #profit_losses.append(int(i[i.find(',')+1:i.find('/')-1]))
print(len(poll_Khan))
'''