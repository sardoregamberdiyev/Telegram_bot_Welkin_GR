from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater, CallbackQueryHandler

from services import *


def btns(tip=None):
    bts = []
    if tip == "menu":
        bts = [
            [KeyboardButton("Welkin GR✈"), KeyboardButton("Jamoa azolari 🫡")],
            [KeyboardButton("Welkin shop 🛒"), KeyboardButton("Loyihaga buyurtma 📰")],
            [KeyboardButton("Bog'lanish 📲")]
        ]
    elif tip == "conection":
        bts = [
            [KeyboardButton("Futbo'lka👕"), KeyboardButton("Bakal🥃")],
            [KeyboardButton("Braslet🎗")]
        ]

    # elif tip == "contact":
    #     bts.append([KeyboardButton("Raqamingizni kiritni", request_contact=True)])
    return ReplyKeyboardMarkup(bts, resize_keyboard=True)


def inline_btn(btn_type=None, ctg=None, tip=None, bts=None):
    if btn_type == "site":
        btn = [
            [InlineKeyboardButton("Bot 🤖", callback_data="site_1", url="https://t.me/Welkin_Project_Order"),
             InlineKeyboardButton("Sayt📁", callback_data="site_2", url="https://t.me/Welkin_Project_Order")],
            [InlineKeyboardButton("Praduct qism💳", callback_data="site_3", url="https://t.me/Welkin_Project_Order"),
             InlineKeyboardButton("Animation sayt📱", callback_data="site_4", url="https://t.me/Welkin_Project_Order")],
            [InlineKeyboardButton("Sayt📁 - Bot🤖", callback_data="site_5", url="https://t.me/Welkin_Project_Order")],
            [InlineKeyboardButton("𝐁𝐨𝐬𝐡𝐪𝐚♾", callback_data="site_6", url="https://t.me/Welkin_Project_Order")]
        ]
    elif btn_type == "call":
        btn = [
            [InlineKeyboardButton("𝑴𝒆𝒏𝒆𝒏𝒅𝒋𝒆𝒓: Sardor ", callback_data="#", url="https://t.me/Welkin_SA"),
             InlineKeyboardButton("𝑴𝒆𝒏𝒆𝒏𝒅𝒋𝒆𝒓: Kamron ", callback_data="#",
                                  url="https://link-to-tel.herokuapp.com/tel/"
                                      "+998 (94) 315 - 13 - 37")],
        ]
    elif btn_type == "order":
        btn = [
            [InlineKeyboardButton("Mahsulotni yo'naltiring 👉🏻", callback_data="#", url="https://t.me"
                                                                                       "/Welkin_Project_Order")],
        ]
    elif btn_type == "team":
        btn = [
            [InlineKeyboardButton("Sardor: Backend", callback_data="#", url="https://t.me/Welkin_SA")],
            [InlineKeyboardButton("Kamron: Frontend", callback_data="#", url="https://t.me/S_P_E_K_T_R")],
            [InlineKeyboardButton("Muhammadyusuf: Frontend", callback_data="#", url="https://t.me/lkkkklll")],
        ]
    else:
        btn = [
            [InlineKeyboardButton("Saytga tashrif ✈", callback_data="sayt", url="https://www.remove.bg/ru"),
             InlineKeyboardButton("Kanal📱", callback_data="sayt", url="https://t.me/Welkin_GR")],
        ]

    return InlineKeyboardMarkup(btn)


try:
    create_table()
except Exception as e:
    pass


def start(update, context):
    user = update.message.from_user
    if get_one(user.id):
        a = update.message.from_user.first_name
        print(a)
    else:
        create_user(user_id=user.id, username=user.username)
    update.message.reply_text("<b>𝘼𝙨𝙨𝙖𝙡𝙤𝙢𝙪 𝘼𝙡𝙚𝙠𝙪𝙢</b> {}  😁 \n \n <b> 𝙒𝙚𝙡𝙠𝙞𝙣 </b>jamoasiga tashrif "
                              "uchun rahmat 🤝 \n\n Siz botni kezish davomida ko'proq malumot olasiz.\n\n"
                              " O'zingizga kerakli bo'lga buttoni bosing👇🏻"
                              .format(update.message.from_user.first_name),
                              reply_markup=btns("menu"), parse_mode="HTML")


def message_handler(update, context):
    msg = update.message.text
    if msg == "Welkin GR✈":
        update.message.reply_text("📲 Saytga tashrif buyursangiz ko'proq malumotlarga ega bo'lasi va bizning. \n \n "
                                  "𝐊𝐚𝐧𝐚𝐥𝐠𝐚 ham ❗️𝐎𝐛𝐮𝐧𝐚 bo'lib qoy'ysangiz Hursand bo'lamiz.",
                                  reply_markup=inline_btn("btn"), parse_mode="HTML")

    elif msg == "Jamoa azolari 🫡":
        update.message.reply_text("<b>😉Sardor Egamberdiyev</b>:  Backend, Full Stack Developer \n\n"
                                  "<b>😉Mamasidiqov  Muhammadyusuf</b>:  Frontend Full Stack Developer\n\n"
                                  "<b>😉Bakberganov Kamronbek</b>:  Frontend Full Stack Developer \n\n"
                                  "<b>Siz Biz bilan bog'lanishig'iz va o'z loyihangiz ustida suhbat \n"
                                  "olib borishingiz mumkin sizga kerakli malumotlarni beramiz😊</b>",
                                  reply_markup=inline_btn("team"), parse_mode="HTML")

    elif msg == "Welkin shop 🛒":
        update.message.reply_photo(photo=open("welkin.png", "rb"),
                                   caption="𝐅𝐮𝐭𝐛𝐨'𝐥𝐤𝐚 𝟏𝟓𝟎𝐦𝐢𝐧𝐠 𝐬𝐨'𝐦\n\n "
                                           "𝐁𝐚𝐤𝐚𝐥 𝟏𝟎𝟎𝐦𝐢𝐧𝐠 𝐬𝐨'𝐦 \n\n "
                                           "𝐁𝐫𝐚𝐬𝐥𝐞𝐭 𝟓𝟎𝐦𝐢𝐧𝐠 𝐬𝐨'𝐦 \n \n"
                                           "𝐎'𝐳𝐢𝐧𝐠𝐢𝐳 𝐭𝐚𝐧𝐥𝐚𝐦𝐨𝐪𝐜𝐡𝐢 𝐛𝐨'𝐥𝐠𝐚 𝐦𝐚𝐡𝐬𝐮𝐥𝐨𝐭𝐧𝐢 "
                                           "𝐭𝐚𝐧𝐥𝐚𝐧𝐠 𝐯𝐚 𝐮 𝐡𝐚𝐪𝐢𝐝𝐚 𝐦𝐚𝐮𝐦𝐨𝐭𝐠𝐚 𝐞𝐠𝐚 "
                                           "𝐛𝐨'𝐥𝐢𝐧𝐠."
                                           "\n\n𝐐𝐚𝐲𝐭𝐚 𝐬𝐭𝐚𝐫𝐭:  /start",
                                   reply_markup=btns("conection"))

    elif msg == "Futbo'lka👕":
        update.message.reply_photo(photo=open("futbo'lka.png", "rb"),
                                   caption="💵𝐅𝐮𝐭𝐛𝐨'𝐥𝐤𝐚 𝟏𝟓𝟎𝐦𝐢𝐧𝐠 𝐬𝐨'𝐦\n\n"
                                           "𝐒𝐢𝐳 𝐟𝐮𝐭𝐛𝐨'𝐥𝐤𝐚 𝐭𝐚𝐧𝐥𝐚𝐝𝐢𝐧𝐠𝐢𝐳 𝐞𝐧𝐝𝐢 𝐛𝐮𝐲𝐮𝐫𝐦𝐚 "
                                           "𝐛𝐞𝐫𝐢𝐬𝐡 𝐮𝐜𝐡𝐮𝐧 𝐬𝐡𝐮 👇🏻 𝐲𝐞𝐫𝐠𝐚 𝐲𝐨𝐳𝐢𝐧𝐠. \n\n 𝐓𝐨𝐬𝐡𝐤𝐞𝐧𝐭 𝐬𝐡𝐚𝐡𝐫𝐢𝐠𝐚 𝟒"
                                           " 𝐤𝐮𝐧 𝐢𝐜𝐡𝐢𝐝𝐚 𝐲𝐞𝐭𝐪𝐚𝐳𝐢𝐥𝐚𝐝𝐢 𝐲𝐨𝐳𝐢𝐬𝐡𝐢𝐧𝐠𝐢𝐳 "
                                           "𝐛𝐢𝐥𝐚𝐧 𝐬𝐢𝐳𝐠𝐚 𝐨𝐩𝐞𝐫𝐭𝐚𝐨𝐫 𝐛𝐨𝐠'𝐥𝐚𝐧𝐚𝐝𝐢.\n\n𝐐𝐚𝐲𝐭𝐚 𝐬𝐭𝐚𝐫𝐭:  /start",
                                   reply_markup=inline_btn("order"))

    elif msg == "Bakal🥃":
        update.message.reply_photo(photo=open("stakan.png", "rb"),
                                   caption="💵𝐁𝐚𝐤𝐚𝐥 𝟏𝟎𝟎𝐦𝐢𝐧𝐠 𝐬𝐨'𝐦\n\n"
                                           "𝐒𝐢𝐳 𝐁𝐚𝐤𝐚𝐥 𝐭𝐚𝐧𝐥𝐚𝐝𝐢𝐧𝐠𝐢𝐳 𝐞𝐧𝐝𝐢 𝐛𝐮𝐲𝐮𝐫𝐦𝐚 "
                                           "𝐛𝐞𝐫𝐢𝐬𝐡 𝐮𝐜𝐡𝐮𝐧 𝐬𝐡𝐮 👇🏻 𝐲𝐞𝐫𝐠𝐚 𝐲𝐨𝐳𝐢𝐧𝐠. \n\n 𝐓𝐨𝐬𝐡𝐤𝐞𝐧𝐭 𝐬𝐡𝐚𝐡𝐫𝐢𝐠𝐚 𝟑"
                                           " 𝐤𝐮𝐧 𝐢𝐜𝐡𝐢𝐝𝐚 𝐲𝐞𝐭𝐪𝐚𝐳𝐢𝐥𝐚𝐝𝐢 𝐲𝐨𝐳𝐢𝐬𝐡𝐢𝐧𝐠𝐢𝐳 "
                                           "𝐛𝐢𝐥𝐚𝐧 𝐬𝐢𝐳𝐠𝐚 𝐨𝐩𝐞𝐫𝐭𝐚𝐨𝐫 𝐛𝐨𝐠'𝐥𝐚𝐧𝐚𝐝𝐢.\n\n𝐐𝐚𝐲𝐭𝐚 𝐬𝐭𝐚𝐫𝐭:  /start",
                                   reply_markup=inline_btn("order"))

    elif msg == "Braslet🎗":
        update.message.reply_photo(photo=open("bog'ich.png", "rb"),
                                   caption="💵𝐁𝐫𝐚𝐬𝐥𝐞𝐭 𝟓𝟎𝐦𝐢𝐧𝐠 𝐬𝐨'𝐦\n\n"
                                           "𝐒𝐢𝐳 𝐁𝐫𝐚𝐬𝐥𝐞𝐭  𝐭𝐚𝐧𝐥𝐚𝐝𝐢𝐧𝐠𝐢𝐳 𝐞𝐧𝐝𝐢 𝐛𝐮𝐲𝐮𝐫𝐦𝐚 "
                                           "𝐛𝐞𝐫𝐢𝐬𝐡 𝐮𝐜𝐡𝐮𝐧 𝐬𝐡𝐮 👇🏻 𝐲𝐞𝐫𝐠𝐚 𝐲𝐨𝐳𝐢𝐧𝐠. \n\n 𝐓𝐨𝐬𝐡𝐤𝐞𝐧𝐭 𝐬𝐡𝐚𝐡𝐫𝐢𝐠𝐚 𝟑"
                                           " 𝐤𝐮𝐧 𝐢𝐜𝐡𝐢𝐝𝐚 𝐲𝐞𝐭𝐪𝐚𝐳𝐢𝐥𝐚𝐝𝐢 𝐲𝐨𝐳𝐢𝐬𝐡𝐢𝐧𝐠𝐢𝐳 "
                                           "𝐛𝐢𝐥𝐚𝐧 𝐬𝐢𝐳𝐠𝐚 𝐨𝐩𝐞𝐫𝐭𝐚𝐨𝐫 𝐛𝐨𝐠'𝐥𝐚𝐧𝐚𝐝𝐢.\n\n𝐐𝐚𝐲𝐭𝐚 𝐬𝐭𝐚𝐫𝐭:  /start",
                                   reply_markup=inline_btn("order"))

    elif msg == "Loyihaga buyurtma 📰":
        update.message.reply_text("𝐒𝐢𝐳 𝐨'𝐳 𝐥𝐨𝐲𝐢𝐡𝐚𝐧𝐠𝐢𝐳𝐧𝐢 𝐲𝐚𝐫𝐚𝐭𝐦𝐨𝐪𝐜𝐡𝐢 𝐬𝐢𝐳. 𝐁𝐢𝐳 𝐬𝐢𝐳𝐠𝐚 𝐲𝐨𝐫𝐝𝐚𝐦 𝐛𝐞𝐫𝐚𝐦𝐢𝐳,\n"
                                  " 𝐒𝐢𝐳 𝐬𝐡𝐮 👇🏻 𝐲𝐞𝐫𝐠𝐚 𝐘𝐨𝐳𝐦𝐚 𝐲𝐨𝐤𝐢 𝐎𝐯𝐨𝐳𝐥𝐢 𝐡𝐚𝐛𝐚𝐫 𝐨𝐫𝐪𝐚𝐥𝐢 𝐦𝐮𝐫𝐨𝐣𝐚𝐭"
                                  " 𝐪𝐢𝐥𝐢𝐧𝐠 𝐯𝐚 𝐬𝐢𝐳𝐠𝐚 𝐨𝐩𝐞𝐫𝐚𝐭𝐨𝐫 𝐛𝐨𝐠'𝐥𝐚𝐧𝐚𝐝𝐢.\n\n "
                                  "❗𝐃𝐢𝐪𝐪𝐚𝐭: 𝐊𝐞𝐫𝐚𝐤𝐬𝐢𝐳 𝐧𝐚𝐫𝐬𝐚𝐥𝐚𝐫 𝐯𝐚 𝐦𝐚𝐥𝐮𝐦𝐨𝐭𝐥𝐚𝐫 𝐛𝐥𝐨𝐜𝐤𝐥𝐚𝐧𝐚𝐝𝐢...",
                                  reply_markup=inline_btn("site"), parse_mode="HTML")

    elif msg == "Bog'lanish 📲":
        update.message.reply_text(
            "𝑴𝒆𝒏𝒆𝒏𝒅𝒋𝒆𝒓: +998 (88) 007 - 41 - 81 \n \n 𝑴𝒆𝒏𝒆𝒏𝒅𝒋𝒆𝒓: +998 (94) 315 - 13 - 37"
            "\n \n  𝑩𝒊𝒛 𝒃𝒊𝒍𝒂𝒏 𝒃𝒐𝒈'𝒍𝒂𝒏𝒊𝒏𝒈 📱  ",
            reply_markup=inline_btn("call"), parse_mode="HTML")


def main():
    Token = "5446923384:AAF3tzJcXKC6ZR0UqFjKeaCUcuCBrr7ldgY"
    updater = Updater(Token)

    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    # updater.dispatcher.add_handler(CallbackQueryHandler(inline_handler))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
