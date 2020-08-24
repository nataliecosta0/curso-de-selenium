"""
Encontre o unicornio
link: https://selenium.dunossauro.live/exercicio_03.html'
"""
from selenium.webdriver import Firefox
from time import sleep


url = 'https://selenium.dunossauro.live/exercicio_03.html'
browser = Firefox()
browser.get(url)
sleep(5)

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

def select_answer(browser, main, anchor, answer):
	"""
	Encontra o link com a resposta desejada dentro da atráves do atributo
	attr.
	
	Args: 
		browser: Instância do browser
		main: Será procurado dentro da tag 'main'
		anchor: Será procurando dentro da tag 'a'
		answer: Resposta desejada

	Return:
		element: Retorna link encontrado dentro do atributo attr.
	"""
	main = browser.find_element_by_tag_name(main)
	anchor = main.find_elements_by_tag_name(anchor)

	for element in anchor:
		if (element.get_attribute('attr')) == answer:
			return element

find_start(browser, 'main', 'a').click()
select_answer(browser, 'main', 'a', "errado").click()