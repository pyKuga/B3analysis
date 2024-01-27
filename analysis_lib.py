#BIBLIOTECA AUXILIAR DE ANALISE

import pandas as pd

#Calcula a tendência de queda ou de alta
def Tendencia(x):
    if x >= 0:
        return -1
    else:
        return 1
    
#calcula a variância com base nos preços disponíveis no dia
def Variancia(x):
    return (
        (x["PREULT"]-x["PREMED"])**2+(x["PREABE"]-x["PREMED"])**2+(x["PREMAX"]-x["PREMED"])**2+(x["PREMIN"]-x["PREMED"])**2)/4

#seleciona uma tabela do tipo especificado
def SelectType(table,tipo):
    return table[tipo]


#calcula a correlação entre os dados de uma tabela pivot
def CorrTable(tabela):
    return (tabela.T@tabela).corr()

#faz o acumulado de alguma propriade com base em um ativo
def Cumulativo(Tabela,Propriedade,Ativos,Nome):
    Acumulado = pd.DataFrame()
    for Ativo in Ativos:
        Recente = Tabela.loc[Tabela["CODNEG"] == Ativo][Propriedade].cumsum()
        pd.concat([Acumulado,Recente]);
    return Acumulado
    
#adapta o arquvio original da B3 para o pandas
def Reader(year):
    Dataset = pd.read_csv("COTAHIST_A"+str(year)+".txt")
    Dataset.drop(Dataset.tail(1).index,inplace=True)
    Dataset.rename(
        columns={Dataset.columns[0]:"data"},
        inplace=True
        )
    Dataset.reset_index()
    return Dataset

#filtra o dado inteiro por ano
def DateFilter(pack,year):
    return pack.loc[
        (pack["DATA"] >= pd.to_datetime(str(year) + '-01-01'))*(pack["DATA"] <= pd.to_datetime(str(year) + '-12-31'))]