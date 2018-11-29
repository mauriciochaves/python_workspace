# language: pt

Funcionalidade: Automobile
    Cenario: Validar se a tela de automobile é aberta
        Quando quando acesso a url "http://www.google.com" pelo navegador "chrome" e clico no botão automobile
            Então o titulo da tela deve ser "Pesquisa Google"