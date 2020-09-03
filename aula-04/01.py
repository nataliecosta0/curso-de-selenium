"""
Encontre o unicornio
link: https://selenium.dunossauro.live/exercicio_03.html'
"""
from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse


url = 'https://selenium.dunossauro.live/exercicio_03.html'
browser = Firefox()
browser.get(url)
sleep(7)

def find_start(browser, main, anchor):
	"""
	Encontra o link começar por aqui pela tag 'a'.
	
	Args: 
		browser: Instância do browser.
		main: Será procurado dentro da tag 'main'.
		anchor: Será procurando dentro da tag 'a'.

	Return:
		anchor: Retorna link encontrado dentro da tag 'a'
	"""
	main = browser.find_element_by_tag_name(main)
	anchor = main.find_element_by_tag_name(anchor)
	return anchor

def select_answer(browser, main, anchor, attribute_answer, answer):
	"""
	Encontra o link com a resposta desejada dentro da do atributo
	attr.
	
	Args: 
		browser: Instância do browser
		main: Será procurado dentro da tag 'main'
		anchor: Será procurando dentro da tag 'a'
		attribute_answer = Atributo desejado para procura
		answer: Resposta desejada

	Return:
		element: Retorna link encontrado dentro do atributo attr.
	"""
	sleep(7)
	main = browser.find_element_by_tag_name(main)
	anchor = main.find_elements_by_tag_name(anchor)

	for element in anchor:
		if (element.get_attribute(attribute_answer)) == answer:
			return element

def select_correct_url(browser, main, anchor):
	"""
	Encontra o link que seja igual o path do browser
	
	Args: 
		browser: Instância do browser
		main: Será procurado dentro da tag 'main'
		anchor: Será procurando dentro da tag 'a'

	Return:
		element: Retorna elemento encontrado que seja igual ao path.
	"""
	sleep(7)
	main = browser.find_element_by_tag_name(main)
	anchor = main.find_elements_by_tag_name(anchor)

	parse_url = urlparse(browser.current_url)

	for element in anchor:
		if element.text == parse_url.path[1:]:
			return element

#inicio
find_start(browser, 'main', 'a').click()
#primeira pagina
select_answer(browser, 'main', 'a', "attr", "errado").click()
#segunda pagina
sleep(20)
select_answer(browser, 'main', 'a', "attr", "certo").click()
#terceira pagina
select_correct_url(browser, 'main', 'a').click()
#quarta pagina
sleep(5)
browser.refresh()
