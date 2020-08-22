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
	Encontra o link começar por aqui pela tag 'a'
	
	Args: 
		browser: Instância do browser
		main: Será procurado dentro da tag 'main'
		anchor: Será procurando dentro da tag 'a'

	Return:
		anchor: Retorna link encontrado dentro da tag 'a'
	"""
	main = browser.find_element_by_tag_name(main)
	anchor = main.find_element_by_tag_name(anchor)
	return anchor

find_start(browser, 'main', 'a').click()