# trilupet_api

**TRILUPET API**

API do Trilupet que contém o Backend que se conecta com o Frontend do sistema web Trilupet.

Também é a API do Projeto MVP da pós-graduação Engenharia de Software da PUC-RJ.

A API utilizará Python com Flask. 

Em resumo Python será a linguagem de programação utilizada no desenvolvimento da API e o Flask contém o conjunto de ferramentas necessárias para esse desenvolvimento. O Flask é o framework.

**PASSO A PASSO PARA CONFIGURAÇÃO DO AMBIENTE DA API E PARA COLOCAR API NO AR**

1º Instalar o Python no seu computador.

Observação:

Se você usa Windows:

Infelizmente, no Windows, o Python 3.10 não pode ser instalado diretamente via terminal no VS Code.

Você deve baixar o instalador manualmente:

👉 https://www.python.org/downloads/release/python-3100/

Depois do download:

* Execute o instalador .exe.+++++

* Marque "Add Python 3.10 to PATH".

* Finalize a instalação.

* Após isso, no terminal do VS Code:

python --version

2º Abrir o terminal do Windows no modo administrador e navegar até a pasta do projeto trilupet_api.

3º Criar o ambiente virtual (Esse comando só é executado uma vez, ou seja, na configuração inicial do projeto trilupet-api):  
**python -m venv .venv**

4º Ativar o ambiente virtual (A partir de agora o SO sabe que tudo que for instalado com o pip install será colocado dentro do ambiente virtual)
**.\.venv\Scripts\activate**

5º Navegar pela linha de comando até a pasta da API e digitar o comando:
**pip install -r requirements.txt**

O pip é o assistente de instalação do Python. O comando acima instala as dependências/bibliotecas descritas no arquivo requirements.txt.

6º Digitar o comando
**flask run --host 0.0.0.0 --port 5000 --reload**

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código fonte.

Observação:
Para executar a API basta executar:
flask run --host 0.0.0.0 --port 5000

7º Abra o [link] exibido no final no navegador para verificar o status da API em execução.




