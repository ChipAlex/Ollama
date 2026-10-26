def get_client():
    return Client(host='http://127.0.0.1:11434', trust_env=False)

from ollama import Client

# Создаем клиента с таймаутом в 5 минут (300 секунд)
#client = Client(timeout=300.0)
#client = Client(trust_env=False)
client = get_client()
#client = Client(host='http://127.0.0.1:11434', trust_env=False)

print("Привет!!!")

response = client.chat(
    model='deepseek-r1:1.5b',
    messages=[{'role': 'user', 'content': 'Как дела ?'}],
)
print(response.message.content)

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
