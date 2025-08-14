from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole


def giga_request(prompt):
   CREDENTILS = "MDc1Zjk1YWItNjY2YS00ZDBiLWFiMzctMzUwMWUyOGYzYzA0OmY3ZTk1ZDY4LTE1ZTMtNGI5Ny1iZDI5LWI2NTVkYWI4NzgwYg=="
   with GigaChat(
           credentials=CREDENTILS,
           verify_ssl_certs=False
         ) as giga:
      response = giga.chat(
          Chat(
            messages= prompt
          )
      )
      return response.choices[0].message.content

def send_giga_message(question, context):
    pages_data = context
    prompt = [
        Messages(role=MessagesRole.ASSISTANT,
                 content=f"Данные для анализа:{pages_data}"
                         f"Ты менеджер компании EORA. Твоя задача используя данные для анализа ответить"
                         f"на вопрос: {question} с примерами конкретных кейсов."
                         f"Для каждой части ответа нужно прикрепить гиперссылку"
                         f"на источник. Ответ должен быть коротким,"
                         f"максимум 2 предложения которые не повторяют друг друга по смыслу, либо одно "
                         f"предложение. Ответ должен быть таким, чтоб заинтересовать клиента приобрести у"
                         f"тебя похожий продукт для своей компании. Гипперссылки должны иметь формат"
                         f"[x](https://eora.ru/cases/chat-boty/hr-bot-dlya-magnit-kotoriy-priglashaet-na-sobesedovanie)"
                         f"в каждой гипперссылке замени x на число по порядку начиная с 1. "
                 ),
        Messages(role=MessagesRole.USER, content=question)
    ]
    request=giga_request(prompt=prompt)
    print(request)
    return request

