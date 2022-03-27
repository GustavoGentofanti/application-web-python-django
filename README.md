# Primeira aplicação WEB utilizando Python com Django #:computer:



### Instalando recursos que serão necessários...

Instalações via terminal Linux(Ubuntu):

- pip: É um gerenciador de pacotes para projetos Python. É com ele que instalamos, removemos e atualizamos pacotes em nossos projetos.

#### $ sudo apt install python3-pip

- django: É um framework para desenvolvimento rápido para web, escrito em Python, que utiliza o padrão model-template-view.

#### $ sudo pip3 install django



### Criando projeto Django...

- Para começar, temos que criar um diretório, que nesse caso, vai se chamar **sistema**:

#### $ django-admin startproject sistema

#### $ ls

- Dentro deste diretório foi criado um arquivo e um diretório,  **manage.py** e **sistema**, e daremos continuidade no processo com os seguinstes comandos:

#### $ cd sistema/

#### $ ls

#### $ django-admin startapp core



### Abrir o projeto em uma IDE...

- Abra a sua IDE;

- File;

- Open folder;

- Selecione o diretório **sistema**, e abra.



### Voltando ao terminal para algumas configurações...

- Para iniciar o servidor:

#### $ python3 manage.py runserver	

- Para acessar o servidor WEB:

#### CTRL+C e clicar no endereço de IP

- Para fechar o servidor:

#### CTRL+C

- Criando tabelas e banco de dados necessários para a aplicação WEB:

#### $ python3 manage.py  migrate

- Criando usuário para poder acessar o sistema:

#### $ python3 manage.py createsuperuser

- Inicializar novamente o servidor:

#### $ python3 manage.py runserver

- Entrar na WEB com o endereço de IP que foi passado através da linha de comando, na barra de pesquisa dar continuidade com **/admin**;

![](/home/gento/Downloads/image-20220327104156439.webp)

### Criando tabela de pessoas...

- Dentro da IDE, abrir a pasta 'core';

![image-20220327104359852](/home/gento/snap/typora/57/.config/Typora/typora-user-images/image-20220327104359852.png)

- Entrar em models.py
- E escrever as seguintes linhas de comando:![image-20220327104523638](/home/gento/snap/typora/57/.config/Typora/typora-user-images/image-20220327104523638.png)



- Dando continuidade, entrar em admin.py e escrever os seguintes comandos:

![image-20220327104620595](/home/gento/snap/typora/57/.config/Typora/typora-user-images/image-20220327104620595.png)



- Em sistema, entrar em settings.py, encontrar a linha de comando **INSTALLED_APPS** e adicionar o seguinte comando:

![image-20220327104818438](/home/gento/snap/typora/57/.config/Typora/typora-user-images/image-20220327104818438.png)



- Para que seja feita esta atualização, no terminal, feche o servidor e rode os seguintes comandos:

#### $ python3 manage.py makemigrations

#### $ python3 manage.py migrate

#### $ python3 manage.py runserver

- Feita a atualização, entre novamente com IP, faça seu login,  sendo assim, foi inserido, dentro da aplicação **CORE**, Pessoas.



### Para melhorar a interface gráfica do site, com recursos simples...

Encerrar o servidor, e digitar no terminal:

#### $ sudo pip3 install django-adminlte2

Após isso, entrar novamente na IDE, sistema, settings.py e adicionar comandos na linha **INSTALELED_APPS**:

![image-20220327105434667](/home/gento/snap/typora/57/.config/Typora/typora-user-images/image-20220327105434667.png)



Iniciar novamente o servidor, e as mudanças serão feitas na interface gráfica, um visual mais moderno.





































