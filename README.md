# Descrição do Projeto

Case US Bank Desenvolvimento de API para consumo de dados do Machine Learning para aumentar o UPSell de vendas de seguro de carro.

## **Status do Projeto**
Finalizado

## Funcionalidades e Demonstração da Aplicação

**Utilizaremos o método HTTP - Requisição**
- Post : /predict (alteração de parâmetros para filtro do cliente)

Exemplo:

    {        
    "Id": 4033,        
    "Age": 41,        
    "Job": 7,        
    "Marital": 1,        
    "Education": 2,        
    "Default": 0,        
    "Balance": 803,        
    "HHInsurance": 1,        
    "CarLoan": 0,        
    "Communication": 0,        
    "LastContactDay": 9,        
    "NoOfContacts": 4,        
    "DaysPassed": 316,        
    "PrevAttempts": 3,        
    "CarInsurance": 0,        
    "ConnectionTime": 592,        
    "DayPeriod": 2,        
    "LastContactMonthNum": 4    
    }

-------
## Gitflow

### Branch principais
 Main e Develop

### Branch Release:
É criado a partir da branch de desenvolvimento quando ele está pronto para ir para aprovação.Nesta branch trabalhamos com o controle de qualidade (tester/qa) corrigindo erros,fazendo melhorias e documentação.Depois de finalizado e testado é mesclado com a branch principal(master/main) e desenvolvimento, criando uma nova tag com a versão dela na branch principal e é feita a exclusão dessa branch de realese.

No caso da US Bank a API foi concluída apenas com uma versão.

### Branch Hotfix
Hotfix - Responsável pela manutenção não programada de erros críticos encontrados em produção. Neste sentido, essa branch só será criada a partir da main, com suas alterações compartilhadas somente com main e develop.

### Branch Feature

**Equipe ciência de dados**

A equipe de ciência de dados deve utilizar as branches de features ao realizar alterações no modelo utilizado para fazer as previsões na API.    

 **Equipe de desenvolvimento**  
O time de desenvolvedores também deve utilizar as branches de features durante o desenvolvimento da API e ao realizar manutenções como implementação de novos endpoits . 

## Acesso ao Projeto

- Instalar dependências: 

    pip install -r requirements.txt

## Acesso a API

src/app main.py

python main.py

**Link aplicação no Azure**
api-usbank-flask.azurewebsites.net


------------------------

## **Tecnologias utilizadas**

 - Python
   
 - Google Colaboratory    
 
 - Machine Learning: Decision Tree 
   
 - Postman    
   
 - Documentação Swagger 

 - Azure
   
 -   Gitflow

## **Pessoas Desenvolvedoras do Projeto**

Carambola - Trio Sagitário

Bianca Barros
Fernando Ascari
Valdinéia Silva
