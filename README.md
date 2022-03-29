# Primeira aplicação WEB utilizando Python com Django :computer:



### :large_blue_circle: Instalando recursos que serão necessários...

Instalações via terminal Linux(Ubuntu):

Pip: É um gerenciador de pacotes para projetos Python. É com ele que instalamos, removemos e atualizamos pacotes em nossos projetos.

- #### $ sudo apt install python3-pip

Django: É um framework para desenvolvimento rápido para web, escrito em Python, que utiliza o padrão model-template-view.

- #### $ sudo pip3 install django

#

### :large_blue_circle: Criando projeto Django...

Para começar, temos que criar um diretório, que nesse caso, vai se chamar **sistema**:

- #### $ django-admin startproject sistema

- #### $ ls

Dentro deste diretório foi criado um arquivo e um diretório,  **manage.py** e **sistema**, e daremos continuidade no processo com os seguinstes comandos:

- #### $ cd sistema/

- #### $ ls

- #### $ django-admin startapp core

#

### :large_blue_circle: Abrir o projeto em uma IDE...

Abra a sua IDE;

File;

Open folder;

Selecione o diretório **sistema**, e abra.

#

### :large_blue_circle: Voltando ao terminal para algumas configurações...

Para iniciar o servidor:

- #### $ python3 manage.py runserver	

Para acessar o servidor WEB:

- #### CTRL+C e clicar no endereço de IP

Para fechar o servidor:

- #### CTRL+C

Criando tabelas e banco de dados necessários para a aplicação WEB:

- #### $ python3 manage.py  migrate

Criando usuário para poder acessar o sistema:

- #### $ python3 manage.py createsuperuser

Inicializar novamente o servidor:

- #### $ python3 manage.py runserver

Entrar na WEB com o endereço de IP que foi passado através da linha de comando, na barra de pesquisa dar continuidade com **/admin**;

![image](https://user-images.githubusercontent.com/98665008/160518323-7bd03a22-7415-4e3e-b3f9-b5bbbf0cc6b3.png)

### :large_blue_circle: Criando tabela de pessoas...

Dentro da IDE, abrir a pasta 'core';

![image](https://user-images.githubusercontent.com/98665008/160518384-1a4321c4-0e4f-4b02-9814-432cf609b352.png)

#

Entrar em models.py
E escrever as seguintes linhas de comando:

![image](https://user-images.githubusercontent.com/98665008/160518429-0f56e9df-f9d8-4bb5-a809-ef34de165884.png)

#

Dando continuidade, entrar em admin.py e escrever os seguintes comandos:

![image](https://user-images.githubusercontent.com/98665008/160518474-9dd36953-a771-4dbb-b947-6eea2aff9ef8.png)

#

Em sistema, entrar em settings.py, encontrar a linha de comando **INSTALLED_APPS** e adicionar o seguinte comando:

![image](https://user-images.githubusercontent.com/98665008/160518570-18ea3c08-5c07-4932-845e-cebd209342a9.png)

#

Para que seja feita esta atualização, no terminal, feche o servidor e rode os seguintes comandos:

- #### $ python3 manage.py makemigrations

- #### $ python3 manage.py migrate

- #### $ python3 manage.py runserver

Feita a atualização, entre novamente com IP, faça seu login,  sendo assim, foi inserido, dentro da aplicação **CORE**, Pessoas.

#

### :large_blue_circle: Para melhorar a interface gráfica do site, com recursos simples...

Encerrar o servidor, e digitar no terminal:

- #### $ sudo pip3 install django-adminlte2

Após isso, entrar novamente na IDE, sistema, settings.py e adicionar comandos na linha **INSTALELED_APPS**:

![image](https://user-images.githubusercontent.com/98665008/160518629-cffccc3e-9c7b-46c6-a1ac-3924d3f53b78.png)



Iniciar novamente o servidor, e as mudanças serão feitas na interface gráfica, um visual mais moderno.
