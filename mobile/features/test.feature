Feature: Registering a tester

Scenario: when I try to login 
        When I click login without informing a user or password
        Then system should display the message regarding the user "Insira um usuário válido"
        Then system should display the message regarding the password "Insira uma senha válida"

Scenario: When I forget my username or password
        Given I clicked on the option I forgot my password
        When I click send without informing a user
        Then system should display the message "Informe o usuário"
        Then the title of the page should be "Esqueci minha senha"
        Then Help information "Preencha a informação abaixo para recuperar sua senha." should be displayed
