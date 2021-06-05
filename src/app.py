import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def grafico_comparativo(dados_2019, dados_2020, causa, estado="BRASIL" ):

    if estado == "BRASIL":
        total_2019=dados_2019.groupby("tipo_doenca").sum()
        total_2020=dados_2020.groupby("tipo_doenca").sum()
        lista = [int(total_2019.loc[causa]), int(total_2020.loc[causa])]
        dados = pd.DataFrame({"Total": lista,
                            "Ano": [2019,2020] })
    else:

        lista_campos = ["uf","tipo_doenca"]
        total_2019=dados_2019.groupby(lista_campos).sum()
        total_2020=dados_2020.groupby(lista_campos).sum()
        lista = [int(total_2019.loc[estado, causa]), int(total_2020.loc[estado, causa])]
        dados = pd.DataFrame({"Total": lista,
                            "Ano": [2019,2020] })

    fig, ax = plt.subplots()
    ax = sns.barplot(x="Ano", y = "Total", data = dados)        
    ax.set_title(f"Óbitos {causa} = {estado}")
    return fig
    
def carrega_dados(caminho):
    dados = pd.read_csv(caminho)
    return dados

def main():
  obitos_2019 = carrega_dados("..\dados\obitos-2019.csv")
  obitos_2020 = carrega_dados("..\dados\obitos-2019.csv")

  tipo_doenca = obitos_2019["tipo_doenca"].unique()
  estado = np.append( obitos_2019["uf"].unique(), "BRASIL" )

  
  st.title( "Primeira Aplicação")
  st.text("DataFrame")
  st.markdown("ESte trabalho analisa os dados dos **óbtios 2019/2020**")

  opcao_1 = st.sidebar.selectbox( "Tipos de Doença", tipo_doenca)
  opcao_2 = st.sidebar.selectbox( "Estado", estado)

  figura = grafico_comparativo( obitos_2019, obitos_2020,
                                opcao_1, opcao_2 )

  st.pyplot(figura)
  
  st.dataframe(obitos_2019) 

if __name__ == "__main__":
  main()