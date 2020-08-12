# segurocarro
#Algoritmo Naive Bayes
#Propõem que a influência dos atributos na classe, sejam avaliados de forma independente, como se um não influência-se o outro.
#Embora essa não seja a forma que isso aconteça no mundo real, normalmente existe uma depenência entre os atributos, mesmo assim o algoritmo se mostra eficaz em #problemas de classificação. Muitas vezes, tendo desempenho melhor que alguns algoritmos sofisticados.
#Alem disso, tem alto desempenho computacional, ou seja, o custo de processamento em termos de memória e tempo de processamento é baixo, comparado a alguns outros #algoritmos.

#Pode ser dividido entre treino e teste para criar o modelo, mas para fins didáticos foi utilizado todo o conjunto de dados para treino, e assim a contrução do #modelo.

#Foi calculado a probabilidade da classe com 4 possibilidades e seus percentuais
#Esse nosso modelo tem 20.000 instâncias com 27 Atributos.

#Porém foi utilizado 3 atributos para a classe (Age, RiskAversion, MakeModel)

#O projeto foi desenvolvido em Python com Django
#preparar o ambiente criando a virtual env com o comando
python3 -m venv venv

#Ativar a máquina virtual venv com o comando
#linux
source env/bin/activate

#windows
./env/Scripts/activate

#Executar a instalação das bibliotecas necesárias com o comando pip
pip install -r requirements.txt

#O projeto está usando o arquivo insurance.csv como base
#para criar o modelo é necessário executar o arquivo salvar_modelo_naivebayes.py
#isso irá criar o arquivo com o modelo treinado modelo_treinado.csv
python salvar_modelo_naivebayes.py

