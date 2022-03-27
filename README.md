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

![](https://lh3.googleusercontent.com/5sODyT6EfSCjcKzu7vH2bUHeJynlHRlFacLMdBYeXBGeJHotEzta8bCLCUrQ5-8yIuvjkRzwq35naj_C6F6JCiEog_E32SeD96JX_y_0b-f3fEyX9d-uKlsgmKjGxUcu9TXoUb1a52xnXeNdBCkYiOFYAXj_SnzmCPjdlI7NnfwBdM9lkdgUOa804NPCAlnFLCTYLBNja0xclb1Fjpb-Y6pnpwvvb1AKjuqcl-mqpYqN4kcFvy_eZA_FN7oF8xNlqSIuuSacdcx27xm9CCv_lmLZJV1MGveZNvVLLD9YenjgnN0he75ycIr4gNCESXR37qBv8vT9HlK9yfORNmmeo3OdxDOsw6IJGI16vdawDVCsim7wpC0XqzVA4-YP4yjM56u8WhPd37x2l6rp7DmpuECHXSN3zkwxaRDJU0A3epcNpkq4QgTv_Dg5kOrtzltxKD3SYszPF0nDQJd864Ov7i6DO87RHH88n_JvndNnmlt9yx21H8HcIjHB0PuwKX4eI0-DDjfLLd-CyS6M4GKNyKfCBKRyjj0HlPYOvB9Q_mrolg-mNukaT4km5YvniiwHDVqcdcPwm-WE7EyARwKVzkakj1trV_mKcMkhV-ddh-Uo94isms_gupL7HhTOB1lSuTwk4D5iJxmD2hShseZXja7WU8eFXCLlUwFGlARLc-xOJnWzV646mYs5xM04nEbobUbdLssWc8gEndCMia4-ZEBH7giTqTifJDUBsC1jWQd1Qpmy1aT1tEys2i0tmBj5J0ZY4oAckhO6mv4DzEozbmg2Nba_w2xjT-vN=w1108-h66-no?authuser=0)

### :large_blue_circle: Criando tabela de pessoas...

Dentro da IDE, abrir a pasta 'core';

![](https://lh3.googleusercontent.com/YUNyHcz-WH3-Gqus6SUYw9-ZM6XwPoSwh1sGsSuhFGXaG8syPMOzPLAC0TvL5HRsifKk9GOb_1uDGy3OqfvQFOaldxc81sDM1gCpQjE1ujEsOjk796sFHLaUVJsVTyAZ6b_LJlfgoYHs-IJkHA0lgok1KlA4V46jXUdcnrIp0vCmpxohfAoISkvg-wTC-qklkXgoqj7rs-BJqBFkcG8T8xfFm0X3LZxg3AOOxUxKzS2guu53mvFAFQyhDA7Uj5sMnBwgDY4A2oQIeBn7YGx9yXX_tHfB8WNUnBSTA1fP_zoE_4Tqpdc0VUuOwq9-4vH6OTWiyAZBOoe0ZxPNmzKMEAcC2LD_eTbD0Sf2nv9plZwi8-NrL9g6UReKEx31U93MONuXK--fqXuFxqk5lwx1-k7vuTMUWkWU7_X0V3f1DOhCv4w9tZqAdP2lX4Y5r5C_klEsChNSORNEukb2Icqy7zrlPjYLflwexu7DXY_FTQ88F8RQvdoTTJpxbBH2A4tqDlM2IA7yPQaxoOAl2EesgTJ3WdfEev7lYrEOk3r9NC-Xnh-TDAzcAivWeO2meE0la1yZoDbtHMcbf2BD4q5EtUcFIiwbIhNTCKHYLMK3uXZFhquuNX5SuTiXGdbGxhTdC5Xtp_7oGFxkjGDoxLJPePL9Zx1VioDhxILfCUQWMvhtoUxbs8slS0XDrmEqLtidhyg620z9xbtGUGUuJfjTS2P_mxIVy3VWf45UF16AXFu--IlSyOw6qderA9Mltmbty-8ljVJgHYN5i0DV7tDwL7d6piHd9V6GOyZW=w257-h294-no?authuser=0)

#

Entrar em models.py
E escrever as seguintes linhas de comando:

![](https://lh3.googleusercontent.com/nsO4kCxSr0YlU15-77GUdnEktH5M5q5yg2_joe2tc5xk6Tj8bjOSo0jVe-84GGgeD3cvi2Ob117qySGcErIV9Ov1qpAoQk4Vu6YMgCEUewBDUnHsg6XvV5lAqvjKsBhZPkcZI1z9jlXQjB_OcT2KbXboc8L9z8r6B02Z6rtn-6GTXf6LSM9hAXIMVEpyUTsDqBRmcK8eY22gBDGTvY419mydIUvk-PBtnXJmeS25CZI_0w8F5dwHd1Rozc9tPWTaPaO7yj5J19wDwSjiig6_67QKwWghkuAoPXD6AfUOFGpKeVLWt9dfQsH8xSvG7MU-2W1ilq1wHrK2O7BqxsU-iA_TWwkvCrCpYFj7j5Smr3wtPN1d-ZrInqqMEGluXObKQWkQr5ThAYsXKHTi2mTpQtKPQMq74MThQnv0f50hF2E8p9_nkF77c-IIfPc5iJ5DlsPCr4-v4U3DTizNfLDRrW80X004mAHBwdUSkjW9_FETmVGrWD0nxhyYCZc24qusB-4aAl2sygFMQHh4Cn-xOMjpE9qt8dShdEgKt5-NqlnG5LwPXjiQ3Z3ZPH6JCSVgqOkIkO_3NyYsW4pf-ltgBJVAcchaa5-Te_y5whUGZxKZ3bYxzuX7Z7ctGA-GYTqbR1hOXWGWhXW_bcMAs9yTtZB5Wghk3VvIFcLIXcbptmb8ow4iuE7iiipXYxTFIyPwiOdMVvf2NcmFtf-1YDgYgF6d01FeZg2h8E7iYi3f0vQdxYPu_FT17M6tF_jdMj3g208s4ZKp4f78MzgClvyi2A1eUFKC4uUjiVr4=w1002-h296-no?authuser=0)

#

Dando continuidade, entrar em admin.py e escrever os seguintes comandos:

![](https://lh3.googleusercontent.com/aJ2jja6BtHHLkF5Q6FKMrewZHkhnUbVK1dJf3z2hVqiN03zzjyjfJCD5T2iPZHFMsppobJY_RknegKkpQdJTMNt6pGRIKa2AYR7IriG9cyBtiGOon9-ftyGxFAELhFWS0evkbG2bu9r3YSkQRv-7rD6aaydxDMwHyaLXgbNJut9ma1WTmWv1_UU9_sP4Q02kD1fhVxF4DtAGCf_C_4Vi1jTClzrz0tstSQIHeOnvQ1FsxUwHjumXj02DCjUo5LUKW9g9LywuDPMyYkQEmzFlYcNtaXR7xROmiTfZJjtHFTvX35B89OoLktfV97PtnXE24rWE1nYDgFWXXbrRepGRefmDSnYyZxgPiEk6Z0atvPUePUTL-72dZdFxWTTLK_g-_1AI2Rg3kWbqZcWfiivNhjFej5mySGDYjG1PHbvsR6aEElSZC59iymM8ohDQemNSIkFEK9QiLa3KKaCtuus-jrdgRYHcMIbCebYy4LsIeaflJqOLI0ZNGjJluGlIan0RNDISFFCFF6MY-kAoqP7QMdns8f-tcx_K1cZo5g2wu_zp82gLJuEOokA4e86fZaQWYqvaDP9R7nwATQ-GZUl00cFKcpeeYhetGAJV8rDB2GrqZRZqaw6XbPlAf2b7Jiw3XPlTF0o5QjMgYzRvW_CNQkrP_7usHTkbte-l5s6DYChLvMQ2tyQ-DZkVoXuWYdjiDnOwy5AkkW7sP5hOlWYQupgZNzEZRKUOevHjm_r6MO-78cu6JJJhtVsiwAyaZEW4mChpOXD5bK9KOWsYAN8Kjfxzahj_FxmQ86ao=w1315-h299-no?authuser=0)

#

Em sistema, entrar em settings.py, encontrar a linha de comando **INSTALLED_APPS** e adicionar o seguinte comando:

![](https://lh3.googleusercontent.com/_4GK1IxJCuv5xWB3l-RnoycE5m07T29eICrKF6Wsi5_-qwdTmTvkZKeccE90ciPbC_GSMMLaCDLQiJoKfsW_btpsSw8v6U3wyYmiEoKf3bJaukFm0JtiEhE7b1llmrtA5S9hLxRDzfadDcKxFCj5qQqKXWMqwtqZmRgXUKTlgGp4bMqedAPC7odlU7XD89atOUVclzvuXiBWW4srV9FYuNxl3-ebSI2jt5h2GaiK8XL_HstBGngok5VKOVipJArTPKlwaZ6pDWt-7jzgTgzJZAiUBNE-OCiviNF_otfqPf26RWkPe55U0vutBbPM8X3EuGJ2WhXeoRCCCUJD2R-juRw7ZAloGGo_Cz4xHS015gmhIFs27kFKgnxXkrVrS-LaS6kGcEXXJmni4DSi06d88bgtFCRrZMtCdSY7ivEnL7KmJ23spPmlXAFiV7j69YMpckiqAq5HwGidWv6OHS2NPxQ8L5ieAtYvAee9svq6-mAoJkFjsYj7ydU-ftaltiObCmVOsD3bmLTyxpavJa2c77Zz0c88_avQtKGiASCrqnm7FizfeQvOiOrLPpso3d-K5zDelmpVLHwL03WAVwSWTtgZxUoS-Qvz8kw98SSSY8fQ8dcpUUlPSDVCIH10qVbQHFZ_7_F3b0slX2dfrvJySJmLXmiNziHKp9Z71AyT4i6zDbkuwEO7VnxSM883DSv0AT6YP5tsXfQ0FkowzmoSxuneirpVOSIotAyx_hPwEIhr-vk568lFAVMGdF5WTzvKAF8fMjYB2ht9ZJn_YBUc1FXI-fDrP_K8KUn4=w1269-h249-no?authuser=0)

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

![](https://lh3.googleusercontent.com/zBjpyLyE5MbmGtdVGDpt-T9Hq5MBkIxo64WIAKlBF4eDqNDg5sbGYkzzGM4tMt9OqYnzTL6Z-GaGyWyi1W4IiMY-ZcAoMUCJknduFbLcPaCPo4d2d9tGqoIUUm4v3lVIg1qwBWYWydYqAB7fs4__TCJYZfvIwT1L2KXZEaD3xLYRBfFlC22Yi7jgsuUGlh_a3h8YrrKOIQ_4jalbtpgwwLs3hLftrzq6Bc46MK5tpFPn481lixrOBuGHrAazLsRANGM5MVEubA1Lu7_Ze3BrNJUnof5M0nQyVLskputOFMu7kwR2Qasnt6WYh00VscltrmPlSb7B_KU0cr5DX1podzzXuk3yVw8d-YlGJatCWBANltDtbcgFSzabaJO9l21yYw3GLYbiYKyQlqL4WooNTOWG6e6NjqHzFJbfMqQYxbsx7aaW8UOTlb1RlN-i8pxgk9OL2Sa_VJX9uo93b7OxDAjXFpAumvNWUNgu3rJtGoGVj4fa4E1d1OYmodrnzrJV0SczzFxjQOeetxrQ8SAloLc0AUqs04BGt2SMQtIQ5UDZTWWsTOYKYEVjWpWdu39g6jbqfph-RLQ0rzg--eUx5HvZy9F1X_z80KUJjvyl1Q_exS7kS_B5BO-sg6fB8YqJ1Qe2pl_PMZeNX-zjPAckN-WKm4shTS6HVTZ3hpci4OM_ONtnrgma9J366Yhjv0nBQHFJQqpdKV15apbLuTdEOoNSgwt5K_4kH4w7D-O_ZS4diUF8Zlbhb8StFe-OLHPlJNv2SJvGeVCOF4mVu4qcU2aXr1qQzUpezwGc=w1123-h310-no?authuser=0)



Iniciar novamente o servidor, e as mudanças serão feitas na interface gráfica, um visual mais moderno.
