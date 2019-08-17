#Pandas pode puxar dados de diversos locais. Banco de dados, CSV, exce, html...
#
import numpy as np
import pandas as pd

df = pd.read_csv('exemplo') #Lendo de arquivos CSV
df.to_csv('exemplo.csv',index=False)

pd.read_excel('Exemplo_Excel.xlsx',sheetname='Sheet1') #Lendo de excel, só importa dados. Imagens ou macros podem bugar o método
df.to_excel('Exemplo_Excel.xlsx',sheet_name='Sheet1')

df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html') # Lendo tabelas de arquivos html

