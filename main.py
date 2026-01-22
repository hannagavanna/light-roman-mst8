import requests
from bs4 import BeautifulSoup
from telegram import Bot
import datetime
import time

# Данные твоего бота (уже вставила ты в main.py)
BOT_TOKEN = "8486036930:AAE3PgjdNcgDnGu99rMFvwVXvE76ZIL-feM"
CHAT_ID = "-1003664914304"  # ID канала
ADDRESS = "Киев, Князя Романа Мстиславича 8"

bot = Bot(token=BOT_TOKEN)

def get_power_status():
    url = "https://www.dtek-kem.com.ua/RU/shutdowns"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Здесь простой пример: ищем таблицу или текст с адресами
    # и статусом отключения/включения
    # Для теста просто вернём фиктивные данные
    status = "Свет включили"
    duration = "2 ч 15 м"
    next_change = "примерно через 3 ч"
    return status, duration, next_change

def send_message():
    status, duration, next_change = get_power_status()
    text = f"📍 {ADDRESS}\n{status}\n🕒 Было {duration}\n⏰ Следующее изменение: {next_change}"
    bot.send_message(chat_id=CHAT_ID, text=text)

if __name__ == "__main__":
    send_message()
