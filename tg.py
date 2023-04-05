from telegram import *
from telegram.ext import *
import random

class Telebot:
    def __init__(self):
        self.pic_dic = ["https://disk.yandex.com/i/BNPWNDziqMtC3g", "https://disk.yandex.com/i/QhzMO6lgWwYPgQ","https://disk.yandex.com/i/qPuTpmRxKIjZHw", "https://disk.yandex.com/i/iQomGoXE-J3WBA","https://disk.yandex.com/i/-YpFCV0iWMn7Mw", "https://disk.yandex.com/i/BzQxp7Wgn3JO9g","https://disk.yandex.com/i/31dPREDCEwRlyA", "https://disk.yandex.com/i/9AQSz_Rgx43Qmg", "https://disk.yandex.com/i/IiT71Njr13kQDQ","https://disk.yandex.com/i/4VImSn2cXBLtiA", "https://disk.yandex.com/i/jFYvW8b3CFEjxw", "https://disk.yandex.com/i/XmLi-3v43WVAJw", "https://disk.yandex.com/i/xB7cviDykSGcLQ", "https://disk.yandex.com/i/Dn_sYSZCvuQRbg", "https://disk.yandex.com/i/a2_lMWJNlq4IaQ", "https://disk.yandex.com/i/gwCVOIh1QeVBZA", "https://disk.yandex.com/i/TDBF_MSWysi6SA", "https://disk.yandex.com/i/XLUH8ccdixdLLw", "https://disk.yandex.com/i/ssq6GmqjH_87ag","https://disk.yandex.com/i/EH3XgDIENNn_ZA", "https://disk.yandex.com/i/Qhj_eV6EMWDM3Q", "https://disk.yandex.com/i/HR7aMPUI6r6z6g", "https://disk.yandex.com/i/Cr6gcrxBhvT36w", "https://disk.yandex.com/i/CrgoOGE-v_xwVA", "https://disk.yandex.com/i/iuSJrlDNts7YTg", "https://disk.yandex.com/i/NNjDUOrpdSCNLg", "https://disk.yandex.com/i/YYMP6iF6XUL4DA", "https://disk.yandex.com/i/TA55EO0KKAVCDw", "https://disk.yandex.com/i/DfR-PSQorlRzxQ", "https://disk.yandex.com/i/zDS8OYsPwMcVVg", "https://disk.yandex.com/i/a7nVflgGyxmQ9A", "https://disk.yandex.com/i/FwrQOwd2EWqpCQ", "https://disk.yandex.com/i/q8jhdp0rTzT_IQ", "https://disk.yandex.com/i/6OGZsn_KDmNRCg", "https://disk.yandex.com/i/D2uU4ZZViKm2EA", "https://disk.yandex.com/i/a4_oqs6oB0yXOg", "https://disk.yandex.com/i/wunStNA32pLJ1A", "https://disk.yandex.com/i/AVENNHJMBfy36g", "https://disk.yandex.com/i/r1ecQr70-K8tXg", "https://disk.yandex.com/i/1eGg-hqIwEVAIQ", "https://disk.yandex.com/i/TNwigp5PThmKdQ", "https://disk.yandex.com/i/z2-VHeK5oeZHMA", "https://disk.yandex.com/i/7cBW0qZPnktSYw", "https://disk.yandex.com/i/5CqR6XlFdvbxig", "https://disk.yandex.com/i/ARo3081UbKmXKg", "https://disk.yandex.com/i/k4lwHctm2ZZuqw", "https://disk.yandex.com/i/6x9SYnrhffbd6Q","https://disk.yandex.com/i/BqdzetkopHm81Q", "https://disk.yandex.com/i/S6QBs9VQsyRZ3A", "https://disk.yandex.com/i/ONmpY9gLSpxtUQ", "https://disk.yandex.com/i/4gTBPO3tPjaahg", "https://disk.yandex.com/i/gsQifMWh3roTOQ", "https://disk.yandex.com/i/49s4xgZ0lViQRg", "https://disk.yandex.com/i/qcO88cvIp-7mrQ", "https://disk.yandex.com/i/hwYr3WBZ4JTctA", "https://disk.yandex.com/i/HX3GOs6eMDfICQ", "https://disk.yandex.com/i/4xG3coIuAICX5A", "https://disk.yandex.com/i/IZoCIwwtqLXbVQ", "https://disk.yandex.com/i/ddICE7sb1-yElg", "https://disk.yandex.com/i/S0zgNclBfgC_EQ", "https://disk.yandex.com/i/x568tazSCKIKwQ", "https://disk.yandex.com/i/cBFKnxpNEHOf5Q", "https://disk.yandex.com/i/QdC3zgPKHNBrmQ", "https://disk.yandex.com/i/uGRAy3lbtkoIxw", "https://disk.yandex.com/i/kp1ZO8RxStLNVw", "https://disk.yandex.com/i/GF09Jb8UwLLPNw", "https://disk.yandex.com/i/Le9_bwXZzL6TYQ", "https://disk.yandex.com/i/D5PZzFknU3p8uQ", "https://disk.yandex.com/i/ixZgF3ZvhRpmpg", "https://disk.yandex.com/i/KczThrwdvudVsQ", "https://disk.yandex.com/i/UpJ8DHbVBnxZkQ", "https://disk.yandex.com/i/rAeHVtAqGNRAnA", "https://disk.yandex.com/i/9NTkUnRYnessRg", "https://disk.yandex.com/i/XA95wgTw4t1YhQ", "https://disk.yandex.com/i/WnbkId5YwZUVfg", "https://disk.yandex.com/i/zpOIUCdNVSwKdQ", "https://disk.yandex.com/i/UMsitc19H5n34w", "https://disk.yandex.com/i/jnpmpCW46VixXg", "https://disk.yandex.com/i/7dnwomY6DrB2UQ", "https://disk.yandex.com/i/9zDs82f1wQSdFA", "https://disk.yandex.com/i/hH6Nq_BZPgvyyQ", "https://disk.yandex.com/i/J6GD0C_GHEgXPw", "https://disk.yandex.com/i/vdwfByQldQ_CDQ", "https://disk.yandex.com/i/anQzQrvZ3ZJH1g", "https://disk.yandex.com/i/2X6_3utqCk0a8A", "https://disk.yandex.com/i/sen8BA3U4EOnfw", "https://disk.yandex.com/i/PTLQKdzXgtbChw", "https://disk.yandex.com/i/Fb5iY7sMu9KvIQ", "https://disk.yandex.com/i/5JU8tYK8BxrB-w", "https://disk.yandex.com/i/_R-GyAe6XNUbhw", "https://disk.yandex.com/i/_Hj8FZW84FHAIA", "https://disk.yandex.com/i/fiXvTLHFY1M9MQ", "https://disk.yandex.com/i/oqTIosJTO4E3HQ", "https://disk.yandex.com/i/9e9d01YUmgtOlg", "https://disk.yandex.com/i/jHi498EBStB2SQ", "https://disk.yandex.com/i/9EunX09arNJP1w", "https://disk.yandex.com/i/kay6Ph9Bqc-LSA", "https://disk.yandex.com/i/JpBDUM1KUpO7Dg", "https://disk.yandex.com/i/AFghinTtnue4lg", "https://disk.yandex.com/i/O9f_hT2k_j6XJw", "https://disk.yandex.com/i/qymR1lojrX-f8w", "https://disk.yandex.com/i/2vLvcVbJH1mgTg", "https://disk.yandex.com/i/Qrq408g_EZcZKg"]
        self.quite_dic = ["Мамочка! Мой самый близкий, самый мудрый и самый любимый человек! Желаю тебе здоровья крепкого, счастья бесконечного, вечной молодости, кипучей энергии и роскошных подарков от судьбы по праздникам и просто так!", "Мама, пусть весенними цветами благоухает каждое твое утро, радостными ожиданиями будет наполнен день и только умиротворение приносит вечер.", "Твои руки всегда самые нежные. Твой голос всегда самый мягкий. Твоя забота загорается огоньком счастья в наших глазах. Мама, будь счастлива и здорова. Мы очень тобой дорожим, ценим каждый миг с тобой рядом и помним каждое твое объятие.", "Родная, единственная моя и всепрощающая мама, хочу пожелать тебе никогда не унывать, всегда радоваться жизни и произошедшим событиям, пускай ангел-хранитель оберегает от недобрых и завистливых людей.", "Мамочка! Желаю здоровья и хорошего настроения, всех благ и удовольствий жизни, благополучия и домашнего уюта, любви и человеческого счастья!", "Мамочка! Огромного тебе здоровья, поменьше каждодневных забот и побольше солнечных и радостных дней. Мы счастливы, когда видим твою улыбку.", "Милая мама! Настал новый день, и я спешу пожелать тебе легкого подъема, продуктивного дня и массы положительных эмоций! Пусть дела делаются легко, а душа поет от счастья!", "Мамочка, пускай твои глаза плачут только от радостных мгновений и счастливых минут, твои руки пускай никогда не знают тяжелой и изнурительной работы, душа твоя только улыбается, смотря на мои успехи и удачи.", "Мам, я поздравляю и желаю яркого солнца, счастья, а главное – здоровья! Ты – самая лучшая в мире мама! Для тебя - вся моя любовь и признательность!", "Ты подарила мне огромный мир! Все хорошее, что во мне есть — от тебя. Я тебя очень люблю и желаю, чтобы дорога твоей жизни была светлой и радостной, очень длинной и счастливой!"]
        self.been = []

    def start_command (self, update, context: CallbackContext):
        context.bot.sendMediaGroup(chat_id=update.effective_chat.id,
                                   media=[InputMediaPhoto("https://pixabay.com/illustrations/heart-love-love-heart-valentine-3097905/", caption="")])
   
        context.bot.send_message(chat_id=update.effective_chat.id, text="🎉Привет и с днем рождения дорогая мамочка!🎉\nНадеюсь что этот бот поднимет тебе настроение!\nНажимай на кнопку дальше!",
         reply_markup=ReplyKeyboardMarkup([["Дальше🏎"]]))

    def handle_message (self, update, context):
        text = str(update.message.text)
        pic = 0
        if self.been == len(self.pic_dic)-1:
            self.been = []
        if text == "Дальше🏎":
            while pic in self.been:
                pic = random.randint(0, len(self.pic_dic))
            self.been.append(pic)
            cap = random.randint(0, len(self.quite_dic))
            context.bot.sendMediaGroup(chat_id=update.effective_chat.id,
                media=[InputMediaPhoto(self.pic_dic[pic], caption=self.quite_dic[cap])])
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Пожалуйста используй кнопки!")


    def main(self):                 #call all the functions, create the bot
        updater = Updater("5776561971:AAFlNRva1f_s6iFL0b3tI1iiKl2lYFx0kyU", use_context=True)
        
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", self.start_command)) 
        dp.add_handler(MessageHandler(Filters.text, self.handle_message))
        updater.start_polling()
        updater.idle()


if __name__ == '__main__':
    print("bot is running")
    bot = Telebot()
    bot.main()