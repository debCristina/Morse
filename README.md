# CÓDIGO MORSE

## 🛠️🖥️ Pré-requisitos do Ambiente em sua máquina.
- Certifique-se de ter o Python instalado: [Python](https://www.python.org/downloads/).
- Para testar a utilização da API, utilize um cliente de API REST: [Insomnia](https://insomnia.rest/download) ou outro cliente que desejar.

### ⚙️🖥️ Configurando o Projeto em sua máquina
Abaixo uma lista de comandos para clonar e configurar este projeto na sua máquina local:
- Instalar git (Windows, Linux e Mac) e depois:
1. Clone este repositório em sua máquina localmente:
   ```bash
   # abra uma pasta com o ( Git bash here ) e cole o código
   
   git clone https://github.com/thiagoferreirapy/Morse.git
   
   ```
2. Abra o VS code diretamente pelo terminal do GIT:
   ```bash
   # primeiro verifique se há um arquivo ( Morse )

   ls

   # Entre no arquivo

   cd Morse

   # Em seguida abra o VS code nessa pasta
   
   code .
   
   ```
- Para Windons:
Entre na pasta do projeto (cd Morse) e rode os seguintes códigos no terminal:
    ```text
   
    python -m venv venv
    venv\Scripts\activate.bat
    python -m pip install --upgrade pip
    python -m pip install django pillow
    python manage.py migrate
    
   ```
- Para linux:
Entre na pasta do projeto (cd Morse) e rode os seguintes códigos no terminal:
    ```text
   
    python3 -m venv venv
    . venv/bin/activate
    pip install django pillow
    python manage.py migrate
    
   ```

- Para Mac:
Entre na pasta do projeto (cd Morse) e rode os seguintes códigos no terminal:
    ```text
   
    python -m venv venv
    . venv/bin/activate
    pip install django pillow
    python manage.py migrate
        
   ```
## Iniciando o projeto
1. Rode o comando para iniciar o servidor
   ```bash
   # server init 
   
   python manage.py runserver 8000
   ```

