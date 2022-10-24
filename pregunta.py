"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re


def ingest_data():

#Se abre el archivo 
    with open('clusters_report.txt') as archivo:
        row = archivo.readlines()

#Se eliminan las primeras filas
    row=row[4:]

#Con los datos de cada clúster se hace una lista
    clusters = []
    cluster = [0, 0, 0, '']

    for r in row:
        if re.match('^ +[0-9]+ +', r):
            number, quantity, percentage, words = r.split()
      
     
            cluster[0] = int(number)
            cluster[1] = int(quantity)
            cluster[2] = float(percentage.replace(',','.')) 

      
            words.pop(0) 
            words = ' '.join(words) 
            cluster[3] += words

        elif re.match('^ +[a-z]', r):
            words = r.split()
            words = ' '.join(words) 
            cluster[3] += ' ' + words 

         elif re.match('^\n', r) or re.match('^ +$', r):
            cluster[3] = cluster[3].replace('.', '') 
            clusters.append(cluster) 
            cluster = [0, 0, 0, ''] 

    df = pd.DataFrame (clusters, columns = ['cluster', 'keywords_quantity', 'keywords_percentage', 'keywords_main'])

    return df
