from behave import step
import time

@step('quando acesso a url "{url}" pelo navegador "{browser}" e clico no botão automobile')
def test_soma(context, url, browser):
    context.driver.get(url)
    time.sleep(3)

@step('o titulo da tela deve ser "{mensage}"')
def test_soma_result(context, mensage):
    context.val = context.driver.find_element_by_name('btnK').get_attribute('value')
    assert  context.val == mensage, 'O texto não foi encontrado na pagina'

