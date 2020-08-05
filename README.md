# segurocarro
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

