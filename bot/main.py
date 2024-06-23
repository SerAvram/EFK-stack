import telebot
import logging
import logstash


def logger() :
    extra = {'app_name': "FASTAPI_APP"}
    test_logger = logging.getLogger('FASTAPI_APP')
    test_logger.setLevel(logging.INFO)
    test_logger.addHandler(logstash.TCPLogstashHandler('127.0.0.1', 6000, version=1))

    test_logger.info('Main endpoint accessed', extra=extra)
    return test_logger


bot = telebot.TeleBot('7493472977:AAGeK-hlJUPhUBpFlSFdO0e0FI1uu-rL5x8')

log = logger()

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я готов к работе. Попробуйте отправить мне сообщение.")
    logger().info("Привет! Я готов к работе. Попробуйте отправить мне сообщение.")

# Обработчик команды /start
@bot.message_handler(commands=['end'])
def send_end(message):
    bot.reply_to(message, "Допобачення")
    logger().info("Допобачення")

# Обработчик команды /start
@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, "Ваш бот")
    logger().info("Ваш бот")

# Обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_message(self, message):
    self.bot.reply_to(message, message.text)  # Простое эхо

# Запуск бота
bot.polling()
