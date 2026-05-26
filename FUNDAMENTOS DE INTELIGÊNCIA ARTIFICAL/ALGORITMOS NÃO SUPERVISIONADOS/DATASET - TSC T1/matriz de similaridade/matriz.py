#fazer uma matriz de similaridade entre os itens, onde cada linha e coluna representa um item e o valor na interseção representa a similaridade entre os itens. Quero calcular de acordo com a quantidade de itens que os usuários tem em comum. Preciso adicionar os dados via csv e exportar via csv. 

import pandas as pd
import numpy as np

df = pd.read_csv('DTST-TSC-T1.csv', index_col=0)

def calcular_matriz_similaridade(df):
    items = df.columns
    n = len(items)
    
    matriz_sim = pd.DataFrame(np.zeros((n, n)), index=items, columns=items)
    
    for i in items:
        for j in items:
            igualdade = (df[i] == df[j]).sum()
            matriz_sim.loc[i, j] = igualdade
            
    return matriz_sim

matriz_resultado = calcular_matriz_similaridade(df)

matriz_resultado.to_csv('matriz_similaridade_itens.csv')