from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater, CallbackQueryHandler

from services import *


def btns(tip=None):
    bts = []
    if tip == "menu":
        bts = [
            [KeyboardButton("Welkin GRβ"), KeyboardButton("Jamoa azolari π«‘")],
            [KeyboardButton("Welkin shop π"), KeyboardButton("Loyihaga buyurtma π°")],
            [KeyboardButton("Bog'lanish π²")]
        ]
    elif tip == "conection":
        bts = [
            [KeyboardButton("Futbo'lkaπ"), KeyboardButton("Bakalπ₯")],
            [KeyboardButton("Brasletπ")]
        ]

    # elif tip == "contact":
    #     bts.append([KeyboardButton("Raqamingizni kiritni", request_contact=True)])
    return ReplyKeyboardMarkup(bts, resize_keyboard=True)


def inline_btn(btn_type=None, ctg=None, tip=None, bts=None):
    if btn_type == "site":
        btn = [
            [InlineKeyboardButton("Bot π€", callback_data="site_1", url="https://t.me/Welkin_Project_Order"),
             InlineKeyboardButton("Saytπ", callback_data="site_2", url="https://t.me/Welkin_Project_Order")],
            [InlineKeyboardButton("Praduct qismπ³", callback_data="site_3", url="https://t.me/Welkin_Project_Order"),
             InlineKeyboardButton("Animation saytπ±", callback_data="site_4", url="https://t.me/Welkin_Project_Order")],
            [InlineKeyboardButton("Saytπ - Botπ€", callback_data="site_5", url="https://t.me/Welkin_Project_Order")],
            [InlineKeyboardButton("ππ¨π¬π‘πͺπβΎ", callback_data="site_6", url="https://t.me/Welkin_Project_Order")]
        ]
    elif btn_type == "call":
        btn = [
            [InlineKeyboardButton("π΄ππππππππ: Sardor ", callback_data="#", url="https://t.me/Welkin_SA"),
             InlineKeyboardButton("π΄ππππππππ: Kamron ", callback_data="#",
                                  url="https://link-to-tel.herokuapp.com/tel/"
                                      "+998 (94) 315 - 13 - 37")],
        ]
    elif btn_type == "order":
        btn = [
            [InlineKeyboardButton("Mahsulotni yo'naltiring ππ»", callback_data="#", url="https://t.me"
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
            [InlineKeyboardButton("Saytga tashrif β", callback_data="sayt", url="https://www.remove.bg/ru"),
             InlineKeyboardButton("Kanalπ±", callback_data="sayt", url="https://t.me/Welkin_GR")],
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
    update.message.reply_text("<b>πΌπ¨π¨ππ‘π€π’πͺ πΌπ‘ππ πͺπ’</b> {}  π \n \n <b> πππ‘π ππ£ </b>jamoasiga tashrif "
                              "uchun rahmat π€ \n\n Siz botni kezish davomida ko'proq malumot olasiz.\n\n"
                              " O'zingizga kerakli bo'lga buttoni bosingππ»"
                              .format(update.message.from_user.first_name),
                              reply_markup=btns("menu"), parse_mode="HTML")


def message_handler(update, context):
    msg = update.message.text
    if msg == "Welkin GRβ":
        update.message.reply_text("π² Saytga tashrif buyursangiz ko'proq malumotlarga ega bo'lasi va bizning. \n \n "
                                  "πππ§ππ₯π π ham βοΈπππ?π§π bo'lib qoy'ysangiz Hursand bo'lamiz.",
                                  reply_markup=inline_btn("btn"), parse_mode="HTML")

    elif msg == "Jamoa azolari π«‘":
        update.message.reply_text("<b>πSardor Egamberdiyev</b>:  Backend, Full Stack Developer \n\n"
                                  "<b>πMamasidiqov  Muhammadyusuf</b>:  Frontend Full Stack Developer\n\n"
                                  "<b>πBakberganov Kamronbek</b>:  Frontend Full Stack Developer \n\n"
                                  "<b>Siz Biz bilan bog'lanishig'iz va o'z loyihangiz ustida suhbat \n"
                                  "olib borishingiz mumkin sizga kerakli malumotlarni beramizπ</b>",
                                  reply_markup=inline_btn("team"), parse_mode="HTML")

    elif msg == "Welkin shop π":
        update.message.reply_photo(photo=open("welkin.png", "rb"),
                                   caption="ππ?π­ππ¨'π₯π€π ππππ¦π’π§π  π¬π¨'π¦\n\n "
                                           "πππ€ππ₯ ππππ¦π’π§π  π¬π¨'π¦ \n\n "
                                           "ππ«ππ¬π₯ππ­ πππ¦π’π§π  π¬π¨'π¦ \n \n"
                                           "π'π³π’π§π π’π³ π­ππ§π₯ππ¦π¨πͺππ‘π’ ππ¨'π₯π π π¦ππ‘π¬π?π₯π¨π­π§π’ "
                                           "π­ππ§π₯ππ§π  π―π π? π‘ππͺπ’ππ π¦ππ?π¦π¨π­π π ππ π "
                                           "ππ¨'π₯π’π§π ."
                                           "\n\nπππ²π­π π¬π­ππ«π­:  /start",
                                   reply_markup=btns("conection"))

    elif msg == "Futbo'lkaπ":
        update.message.reply_photo(photo=open("futbo'lka.png", "rb"),
                                   caption="π΅ππ?π­ππ¨'π₯π€π ππππ¦π’π§π  π¬π¨'π¦\n\n"
                                           "ππ’π³ ππ?π­ππ¨'π₯π€π π­ππ§π₯πππ’π§π π’π³ ππ§ππ’ ππ?π²π?π«π¦π "
                                           "πππ«π’π¬π‘ π?ππ‘π?π§ π¬π‘π? ππ» π²ππ«π π π²π¨π³π’π§π . \n\n ππ¨π¬π‘π€ππ§π­ π¬π‘ππ‘π«π’π π π"
                                           " π€π?π§ π’ππ‘π’ππ π²ππ­πͺππ³π’π₯πππ’ π²π¨π³π’π¬π‘π’π§π π’π³ "
                                           "ππ’π₯ππ§ π¬π’π³π π π¨π©ππ«π­ππ¨π« ππ¨π 'π₯ππ§πππ’.\n\nπππ²π­π π¬π­ππ«π­:  /start",
                                   reply_markup=inline_btn("order"))

    elif msg == "Bakalπ₯":
        update.message.reply_photo(photo=open("stakan.png", "rb"),
                                   caption="π΅πππ€ππ₯ ππππ¦π’π§π  π¬π¨'π¦\n\n"
                                           "ππ’π³ πππ€ππ₯ π­ππ§π₯πππ’π§π π’π³ ππ§ππ’ ππ?π²π?π«π¦π "
                                           "πππ«π’π¬π‘ π?ππ‘π?π§ π¬π‘π? ππ» π²ππ«π π π²π¨π³π’π§π . \n\n ππ¨π¬π‘π€ππ§π­ π¬π‘ππ‘π«π’π π π"
                                           " π€π?π§ π’ππ‘π’ππ π²ππ­πͺππ³π’π₯πππ’ π²π¨π³π’π¬π‘π’π§π π’π³ "
                                           "ππ’π₯ππ§ π¬π’π³π π π¨π©ππ«π­ππ¨π« ππ¨π 'π₯ππ§πππ’.\n\nπππ²π­π π¬π­ππ«π­:  /start",
                                   reply_markup=inline_btn("order"))

    elif msg == "Brasletπ":
        update.message.reply_photo(photo=open("bog'ich.png", "rb"),
                                   caption="π΅ππ«ππ¬π₯ππ­ πππ¦π’π§π  π¬π¨'π¦\n\n"
                                           "ππ’π³ ππ«ππ¬π₯ππ­  π­ππ§π₯πππ’π§π π’π³ ππ§ππ’ ππ?π²π?π«π¦π "
                                           "πππ«π’π¬π‘ π?ππ‘π?π§ π¬π‘π? ππ» π²ππ«π π π²π¨π³π’π§π . \n\n ππ¨π¬π‘π€ππ§π­ π¬π‘ππ‘π«π’π π π"
                                           " π€π?π§ π’ππ‘π’ππ π²ππ­πͺππ³π’π₯πππ’ π²π¨π³π’π¬π‘π’π§π π’π³ "
                                           "ππ’π₯ππ§ π¬π’π³π π π¨π©ππ«π­ππ¨π« ππ¨π 'π₯ππ§πππ’.\n\nπππ²π­π π¬π­ππ«π­:  /start",
                                   reply_markup=inline_btn("order"))

    elif msg == "Loyihaga buyurtma π°":
        update.message.reply_text("ππ’π³ π¨'π³ π₯π¨π²π’π‘ππ§π π’π³π§π’ π²ππ«ππ­π¦π¨πͺππ‘π’ π¬π’π³. ππ’π³ π¬π’π³π π π²π¨π«πππ¦ πππ«ππ¦π’π³,\n"
                                  " ππ’π³ π¬π‘π? ππ» π²ππ«π π ππ¨π³π¦π π²π¨π€π’ ππ―π¨π³π₯π’ π‘ππππ« π¨π«πͺππ₯π’ π¦π?π«π¨π£ππ­"
                                  " πͺπ’π₯π’π§π  π―π π¬π’π³π π π¨π©ππ«ππ­π¨π« ππ¨π 'π₯ππ§πππ’.\n\n "
                                  "βππ’πͺπͺππ­: πππ«ππ€π¬π’π³ π§ππ«π¬ππ₯ππ« π―π π¦ππ₯π?π¦π¨π­π₯ππ« ππ₯π¨ππ€π₯ππ§πππ’...",
                                  reply_markup=inline_btn("site"), parse_mode="HTML")

    elif msg == "Bog'lanish π²":
        update.message.reply_text(
            "π΄ππππππππ: +998 (88) 007 - 41 - 81 \n \n π΄ππππππππ: +998 (94) 315 - 13 - 37"
            "\n \n  π©ππ πππππ πππ'ππππππ π±  ",
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
