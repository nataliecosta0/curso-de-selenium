"""
http://selenium.dunossauro.live/exercicio_04.html
"""
from selenium.webdriver import Firefox
from time import sleep


url = 'http://selenium.dunossauro.live/exercicio_04.html'
browser = Firefox()
browser.get(url)
sleep(10)

def fill_fields(browser, name, email, password, phone):
	"""
	Preenche o formulário do exercício 04 da aula 05
	"""
	browser.find_element_by_id('nome').send_keys(name)
	browser.find_element_by_id('email').send_keys(email)
	browser.find_element_by_id('senha').send_keys(password)
	browser.find_element_by_id('telefone').send_keys(phone)
	browser.find_element_by_id('btn').click()

fill_fields(browser, "Natalie", "natalie@mail.com", "always", "1178945612")

sleep(5)

result = {
	'nome': 'Natalie',
	'email': 'natalie@mail.com',
	'senha': 'always',
	'telefone': '1178945612'
}

fill_fields(browser, **result)

url_parse = urlparse(browser.current_url)

sleep(5)

result = browser.find_element_by_id

browser.quit()