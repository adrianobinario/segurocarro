#Carregamento do classificador
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
#pickle usado para gerar o modelo treinado
import pickle

base = pd.read_csv('insurance.csv')
#base.Age.unique()
#base.RiskAversion.unique()
#base.MakeModel.unique()
#base.Accident.unique()

#Cria o classificar com base nas colunas que serão trabalhadas
#2 - Age (Idade)
#4 - RiskAversion (Versão do Risco)
#9 - MakeModel (Modelo do veículo)
X = base.iloc[:, [2, 4, 9]].values

#Classe que servirá de base para fazer as previsões
y = base.iloc[:, 8].values

#Converte os atributos de categóricos para numéricos
lb = LabelEncoder()
X[:,0] = lb.fit_transform(X[:,0])
X[:,1] = lb.fit_transform(X[:,1])
X[:,2] = lb.fit_transform(X[:,2])

#Criar o modelo usando o Gaus
modelo = GaussianNB()
#Treina o modelo no naive_bayes
modelo.fit(X, y)

#Testando na mesma base
previsoes = modelo.predict(X)
#Verifica o accuracy_score
accuracy_score(y, previsoes)

pickle.dump(modelo, open('app_pagina/naivebayes/modelo_treinado.csv', 'wb'))