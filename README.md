
#Projeto para aprendizagem de automação de testes
* pip install -r requirements.txt

#Generate Report 
[allure-behave](https://pypi.org/project/allure-behave/)


Installation and Usage
======================

 #Windows (PowerShell comand lines)
 .. code:: bash 
    $ iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
    $ [scoop](https://github.com/lukesampson/scoop) install allure

 #Linux (Ubuntu comand lines)
* sudo apt-get install allure

 #Run Tests
* behave -f allure_behave.formatter:AllureFormatter -o allure_results ./features
* allure serve allure_results