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


url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
browser = Firefox()
browser.get(url)
sleep(7)

title = browser.find_element_by_tag_name('h1')
dict2 = {}

for number in range(3):
  find_p = browser.find_elements_by_tag_name('p')
  valor = find_p[number].text
  chave = browser.find_element_by_xpath(f'/html/body/p[text()="{valor}"]').get_attribute("atributo")
  dict2.update({chave:valor})

print({title.text:dict2})
browser.quit()