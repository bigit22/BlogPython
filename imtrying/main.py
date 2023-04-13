from email import message
import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from config import open_weather_token, telebot_token
bot = telebot.TeleBot(telebot_token)
owm = OWM(open_weather_token)
mgr = owm.weather_manager()

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hi, bastard. Enter city u need. U will see temperature and sky status")

@bot.message_handler(content_types = ['text'])
def chooseCityAndGetWeather(message):
    place = message.text
    try:
        observation = mgr.weather_at_place(place)
        w = observation.weather
        answer = "in " + place + " now " + str(w.temperature('celsius')['temp']) + " degrees Celsius and " + str(w.detailed_status)
        print("in " + place + " now " + str(w.temperature('celsius')['temp']) + " degrees Celsius and " + str(w.detailed_status))
        bot.send_message(message.chat.id, answer)
    except:
        bot.send_message(message.chat.id, "enter the correct city")

bot.polling(none_stop = True)

