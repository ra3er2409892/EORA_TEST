from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def parse():
    service = Service(ChromeDriverManager().install()) # Автоматическая установка и запуск ChromeDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Запускаем браузер в фоновом режиме
    options.add_argument("--log-level=3")  # Минимальный уровень логов
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Отключаем лишние логи
    driver = webdriver.Chrome(service=service, options=options)

    pages_urls = []

    try:
        # Открываем файл 'sites.txt' в режиме чтения ('r')
        with open('sites.txt', 'r') as file:
            for line in file:
                # Удаляем лишние пробелы и перенос строки в конце каждой строки
                pages_urls.append(line.strip())
    except FileNotFoundError:
        print("Файл sites.txt не найден.")
    pages_content = {}
    for URL in pages_urls:
        driver.get(URL) # Получаем HTML-код страницы
        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser') # Парсим HTML с помощью BeautifulSoup
        for element in soup(['header',]): # Удаляем ненужные элементы
            element.decompose()
        text = soup.get_text(separator='\n', strip=True) # Получаем текст

        pages_content.update({URL: text})
        print(text)
    driver.quit() # Закрываем браузер
    return pages_content

if __name__ == '__main__':
    parse()