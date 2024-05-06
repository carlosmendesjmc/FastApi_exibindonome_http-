#  Importando FastAP
from fastapi import FastAPI 
import uvicorn    # Uvicorn é um servidor ASGI super rápido, construído sobre uvloop e httptools


# iniciando a aplicação
app = FastAPI() # aqui estamos uma instancia de clase chamada FastaPI usado para definir rotas interagirmos com app.


# Definindo uma rota - metodo get ele recupera e exibi os dados solicitados, ele nao faz alterações 
@app.get("/")  #a / é usado como uma definição de rota criada para informar ao FastAPI, trata de requisição HTPP Get para a rota / equivalente a um ex: http://localhot:8000/
def home():    #usado quando faz uma requisição GET para a rota / no navegador
    return {"José Carlos"} # obs nesta rota retorna um JSON quando a função home é chamada

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
#pip install FastAPI
#pip install uvicorn

#------para rodar a aplicação
#uvicorn app:app --reload

 #--reload: Esta é uma opção que diz ao servidor Uvicorn para iniciar em modo de recarga. Em modo de recarga, 
 # o servidor irá reiniciar automaticamente sempre que detectar uma mudança no seu código. Isso é muito útil durante o
 # desenvolvimento, pois você não precisa parar e iniciar o servidor toda vez que fizer uma alteração no seu código.