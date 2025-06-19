# trilupet_api
API do Projeto MVP da pós-graduação Engenharia de Software da PUC-RJ.

**PASSO A PASSO PARA CONFIGURAÇÃO DO AMBIENTE DA API E PARA COLOCAR API NO AR**

1º Abrir o Terminal do Windows no modo administrador no Windows.

2º Criar o ambiente virtual: 
**python -m venv .venv**

3º Ativar o ambiente virtual (A partir de agora o SO sabe que tudo que for instalado com o pip install será colocado dentro do ambiente virtual)
**.\.venv\Scripts\activate**

4º Dentro da pasta da API digitar o comando:
**pip install -r requirements.txt**

pip -> assistente de instalação do python
Este comando instala as dependências/bibliotecas, descritas no arquivo requirements.txt.

5º Digitar o comando
**flask run --host 0.0.0.0 --port 5000 --reload**

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código fonte.

Observação:
Para executar a API basta executar:
flask run --host 0.0.0.0 --port 5000

6º Abra o [link] exibido no final no navegador para verificar o status da API em execução.


