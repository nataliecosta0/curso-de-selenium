"""
Crie um programa com selenium que:
* Gere um dicionário, onde a chave é a tag h1
  * O valor deve ser um novo dicionário 
  * Cada chave do valor deverá ser o valor do 'atributo'
  * Cada valor deve ser o texto contido no elemento 
  
url: https://curso-python-selenium.netlify.app/exercicio_01.html
"""

from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

navegador = Firefox()

navegador.get(url)

sleep(1)

a = navegador.find_element_by_tag_name('a')


for click in range(10):
    ps = navegador.find_elements_by_tag_name('p')
    a.click()
    print(f'Valor do ultimo p: {ps[-1].text} valor do click: {click}')

    print(f'Os valors são iguais {ps[-1].text == str(click)}')


navegador.quit()