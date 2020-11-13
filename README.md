# ✔ Indice 

- [Sobre](#-sobre)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Como Baixar o Projeto](#-como-baixar-o-projeto)

---

## 📜 Sobre 

O projeto de diagnóstico de catarata através de imagens da retina foi desenvolvido como o projeto de TCC do curso de ciências da computação dos seguintes desenvolvedores:

- João Carlos (https://github.com/joaoroche)
- Lucas Santos
- Paulo Henrique (https://github.com/Paulohz)

Esta parte do projeto consiste na API que recebe as solicitações e retorna o diagnóstico.

Existe outro repositório com o código que irá fazer a extração das caracteristicas utilizando o algoritmo LBP (Local Binary Pattern) e ao final gerando o modelo preditivo no formato .sav. (https://github.com/Lucas-Santos-A/Cataract-Feature-Extraction)

As imagens utilizadas neste projeto foram retiradas do seguinte link: https://www.kaggle.com/jr2ngb/cataractdataset

Uma aplicação WEB para consumir API citada acima pode ser acessada através do seguinte repositório (https://github.com/Paulohz/cataract-detection)

---

## 🚀 Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias.

- Python
- Flask

---

## 📦 Como Baixar o Projeto

```bash
$ git clone https://github.com/Lucas-Santos-A/Cataract-Detection-API

# Instalar dependencias
$ pip install -r requirements.txt

# Substituir as linhas 90 até 93 do arquivo app.py pelo seguinte código 

# if __name__== '__main__':
    app.run("localhost", "9999", debug=True)

# Isto garante que o código rodará localmente

#Executar a aplicação
$ py app.py

# A aplicação possui somente o endpoint /predict. É necessário enviar uma solicitação POST contendo um MultipartForm com a imagem seguindo o formato:
# image: (upload da imagem)

```








