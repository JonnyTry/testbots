
import config
import text_glava1
import telebot
from telebot import types
bot = telebot.TeleBot(config.token)
import random 
#import random, randrange, randint
global WIN2
WIN2 = 'false'
game1= [50, 70, 20]


@bot.message_handler(commands=['start'])
def start(message):
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.Next, callback_data='1')  # поменять на 1
        keyboard.add(Next)
        bot.send_photo(message.chat.id, photo=text_glava1.electric_train, caption=text_glava1.message_1, reply_markup=keyboard)
        #bot.delete_message(message.chat.id, message.message_id)      #потом разкоментить что б не ебстись

@bot.message_handler(content_types=["text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact", "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo", "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id", "migrate_from_chat_id", "pinned_message"])  # Типы сообщений
def chatting(message):
    if message.text != 'start':
        bot.delete_message(message.chat.id, message.message_id)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global WIN2
    if  call.data == 'start2':
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.Next, callback_data='1')   # поменять на 1
        keyboard.add(Next)
        bot.edit_message_media(types.InputMediaPhoto(text_glava1.electric_train), chat_id=call.message.chat.id, message_id=call.message.message_id)              # Меняет пикче
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_1, reply_markup=keyboard) 
        #bot.send_photo(message.chat.id, photo=text_glava1.electric_train, caption=text_glava1.message_1, reply_markup=keyboard)

    elif call.data == '1':
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.Next, callback_data='2')   
        keyboard.add(Next)
        #bot.edit_message_media(types.InputMediaPhoto(text_glava1.hospital), chat_id=call.message.chat.id, message_id=call.message.message_id)              # Меняет пикче
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_2, reply_markup=keyboard)  # меняет текст      
    elif call.data == '2':
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.Next, callback_data='3')
        keyboard.add(Next)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_3, reply_markup=keyboard) 
    elif call.data == '3':
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.Next, callback_data='4')
        keyboard.add(Next)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_4, reply_markup=keyboard) 
    elif call.data == '4':
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.Next, callback_data='menu_1')
        keyboard.add(Next)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_5, reply_markup=keyboard) 
    elif call.data == 'menu_1':
        keyboard = types.InlineKeyboardMarkup()
        Pravda = types.InlineKeyboardButton(text=text_glava1.answer_1, callback_data='Pravda')
        Opp = types.InlineKeyboardButton(text=text_glava1.answer_2, callback_data='Opp')
        Palka = types.InlineKeyboardButton(text=text_glava1.answer_3, callback_data='Palka')
        Inostr = types.InlineKeyboardButton(text=text_glava1.answer_4, callback_data='Inostr')
        keyboard.add(Pravda)
        keyboard.add(Opp)
        keyboard.add(Palka)
        keyboard.add(Inostr)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_6, reply_markup=keyboard) 
    elif call.data == 'Pravda':
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.Next, callback_data='8')
        keyboard.add(Next)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_7, reply_markup=keyboard) 
    elif call.data == 'Opp':
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.Next, callback_data='opp1')
        keyboard.add(Next)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_2_1, reply_markup=keyboard) 
    elif call.data == 'Palka':
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.Next, callback_data='Palka1')
        keyboard.add(Next)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_3_1, reply_markup=keyboard) 
    elif call.data == 'Inostr':
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.Next, callback_data='Inostr1')
        keyboard.add(Next)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_4_1, reply_markup=keyboard) 
    elif call.data == 'Palka1':
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.Next, callback_data='Palka2')
        keyboard.add(Next)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_3_2, reply_markup=keyboard)
    elif call.data == 'Palka2':
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.Next, callback_data='Pravda')
        keyboard.add(Next)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_3_3, reply_markup=keyboard) 
    elif call.data == 'opp1':
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.Next, callback_data='opp2')
        keyboard.add(Next)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_2_2, reply_markup=keyboard)
    elif call.data == 'opp2':
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.Next, callback_data='opp3')
        keyboard.add(Next)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_2_3, reply_markup=keyboard) 
    elif call.data == 'opp3':
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.Next, callback_data='opp4')
        keyboard.add(Next)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_2_4, reply_markup=keyboard) 
    elif call.data == 'opp4':
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.Next, callback_data='Pravda')
        keyboard.add(Next) 
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_2_5, reply_markup=keyboard) 
    elif call.data == 'Inostr1':
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.Next, callback_data='Inostr2')
        keyboard.add(Next)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_4_2, reply_markup=keyboard)
    elif call.data == 'Inostr2':
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.Next, callback_data='Pravda')
        keyboard.add(Next)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_4_3, reply_markup=keyboard) 
    elif call.data == '8':
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.Next, callback_data='9')
        keyboard.add(Next)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_8, reply_markup=keyboard)
    elif call.data == '9':
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.Next, callback_data='10')
        keyboard.add(Next)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_9, reply_markup=keyboard) 
    elif call.data == '10':
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.Next, callback_data='railway_station')
        keyboard.add(Next)
        bot.edit_message_media(types.InputMediaPhoto(text_glava1.railway_station), chat_id=call.message.chat.id, message_id=call.message.message_id) 
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_10, reply_markup=keyboard)

#Глава 2. Карта города


    elif call.data == 'railway_station':
        keyboard = types.InlineKeyboardMarkup()
        mall = types.InlineKeyboardButton(text=text_glava1.local_2, callback_data='mall')
        hospital = types.InlineKeyboardButton(text=text_glava1.local_3, callback_data='hospital')
        mining_railway_station = types.InlineKeyboardButton(text=text_glava1.mining_railway_station, callback_data='mining_railway_station')
        keyboard.add(mall, hospital)
        keyboard.add(mining_railway_station)
        if WIN2 == 'true':
            win_win = types.InlineKeyboardButton(text=text_glava1.WIN_text, callback_data='flat')
            keyboard.add(win_win)
        Indicators = text_glava1.HP + '   ' + str(game1[0]) + text_glava1.Energy + '     ' +  str(game1[1]) + text_glava1.Cash + '        ' +  str(game1[2]) 
        bot.edit_message_media(types.InputMediaPhoto(text_glava1.railway_station), chat_id=call.message.chat.id, message_id=call.message.message_id) 
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=Indicators + text_glava1.message_11, reply_markup=keyboard)
 
    elif call.data == 'mall':        # Торговый центр
        keyboard = types.InlineKeyboardMarkup()
        railway_station = types.InlineKeyboardButton(text=text_glava1.local_1, callback_data='railway_station')
        embankment = types.InlineKeyboardButton(text=text_glava1.local_4, callback_data='embankment')
        embankment_shop = types.InlineKeyboardButton(text=text_glava1.embankment_shop_text, callback_data='embankment_shop')
        keyboard.add(embankment, railway_station)
        keyboard.add(embankment_shop)
        if WIN2 == 'true':
            win_win = types.InlineKeyboardButton(text=text_glava1.WIN_text, callback_data='flat')
            keyboard.add(win_win)
        Indicators = text_glava1.HP + '   ' + str(game1[0]) + text_glava1.Energy + '     ' +  str(game1[1]) + text_glava1.Cash + '        ' +  str(game1[2]) 
        bot.edit_message_media(types.InputMediaPhoto(text_glava1.mall), chat_id=call.message.chat.id, message_id=call.message.message_id) 
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=Indicators + text_glava1.message_12, reply_markup=keyboard)

    elif call.data == 'hospital':   #Больница
        keyboard = types.InlineKeyboardMarkup()
        railway_station = types.InlineKeyboardButton(text=text_glava1.local_1, callback_data='railway_station')
        bridge = types.InlineKeyboardButton(text=text_glava1.local_5, callback_data='bridge')
        treatment = types.InlineKeyboardButton(text=text_glava1.treatment_text, callback_data='treatment')
        keyboard.add(railway_station, bridge)
        keyboard.add(treatment)
        
        if WIN2 == 'true':
            win_win = types.InlineKeyboardButton(text=text_glava1.WIN_text, callback_data='flat')
            keyboard.add(win_win)
        Indicators = text_glava1.HP + '   ' + str(game1[0]) + text_glava1.Energy + '     ' +  str(game1[1]) + text_glava1.Cash + '        ' +  str(game1[2])
        bot.edit_message_media(types.InputMediaPhoto(text_glava1.hospital), chat_id=call.message.chat.id, message_id=call.message.message_id) 
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=Indicators + text_glava1.message_13, reply_markup=keyboard)

    elif call.data == 'bridge':   #Мост
        keyboard = types.InlineKeyboardMarkup()
        hospital = types.InlineKeyboardButton(text=text_glava1.local_3, callback_data='hospital')
        embankment = types.InlineKeyboardButton(text=text_glava1.local_4, callback_data='embankment')
        sleep = types.InlineKeyboardButton(text=text_glava1.leep_text, callback_data='sleep')
        keyboard.add(hospital, embankment)
        keyboard.add(sleep)
        if WIN2 == 'true':
            win_win = types.InlineKeyboardButton(text=text_glava1.WIN_text, callback_data='flat')
            keyboard.add(win_win)
        Indicators = text_glava1.HP + '   ' + str(game1[0]) + text_glava1.Energy + '     ' +  str(game1[1]) + text_glava1.Cash + '        ' +  str(game1[2])
        bot.edit_message_media(types.InputMediaPhoto(text_glava1.bridge), chat_id=call.message.chat.id, message_id=call.message.message_id) 
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=Indicators + text_glava1.message_14, reply_markup=keyboard)

    elif call.data == 'embankment':   #Набережная
        keyboard = types.InlineKeyboardMarkup()
        mall = types.InlineKeyboardButton(text=text_glava1.local_2, callback_data='mall')
        bridge = types.InlineKeyboardButton(text=text_glava1.local_5, callback_data='bridge')
        loto = types.InlineKeyboardButton(text=text_glava1.loto_text, callback_data='loto')
        keyboard.add(bridge, mall)
        keyboard.add(loto)
        if WIN2 == 'true':
            win_win = types.InlineKeyboardButton(text=text_glava1.WIN_text, callback_data='flat')
            keyboard.add(win_win)
        Indicators = text_glava1.HP + '   ' + str(game1[0]) + text_glava1.Energy + '     ' +  str(game1[1]) + text_glava1.Cash + '        ' +  str(game1[2])
        bot.edit_message_media(types.InputMediaPhoto(text_glava1.embankment), chat_id=call.message.chat.id, message_id=call.message.message_id) 
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=Indicators + text_glava1.message_15, reply_markup=keyboard)

    elif call.data == 'mining_railway_station':         # описания майнингов и всех функций игры 1     описание работы вогзала
        if game1[0] > 0:
            if random.randint(1, 100) <= 50: #50% на урон
                game1[2] = game1[2] + random.randint(5, 10)   
                game1[1] = game1[1] - 1
                keyboard = types.InlineKeyboardMarkup()
                mall = types.InlineKeyboardButton(text=text_glava1.local_2, callback_data='mall')
                hospital = types.InlineKeyboardButton(text=text_glava1.local_3, callback_data='hospital')
                mining_railway_station = types.InlineKeyboardButton(text=text_glava1.mining_railway_station, callback_data='mining_railway_station')
                keyboard.add(mall, hospital)
                keyboard.add(mining_railway_station)
                if WIN2 == 'true':
                    win_win = types.InlineKeyboardButton(text=text_glava1.WIN_text, callback_data='flat')
                    keyboard.add(win_win)
                Indicators = text_glava1.HP + '   ' + str(game1[0]) + text_glava1.Energy + '     ' +  str(game1[1]) + text_glava1.Cash + '        ' +  str(game1[2]) 
                bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=Indicators + text_glava1.message_11, reply_markup=keyboard)
            else:
                damage_ed = random.randint(3, 5)
                damage= text_glava1.mining_railway_station_polise[random.randint(0, 2)] + text_glava1.mining_railway_station_damage + str(damage_ed) + text_glava1.mining_railway_station_damage_2
                game1[0] = game1[0] - damage_ed
                if game1[0] <= 0:
                    damage = text_glava1.mining_railway_station_polise[random.randint(0, 2)] + text_glava1.mining_railway_station_damage + str(damage_ed) + text_glava1.mining_railway_station_damage_2 +'\n\n'+ text_glava1.death_text
                    bot.edit_message_media(types.InputMediaPhoto(text_glava1.death), chat_id=call.message.chat.id, message_id=call.message.message_id) 
                    bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.death_text) 
                    bot.answer_callback_query(call.id, show_alert=True, text=damage)
                    return
                bot.answer_callback_query(call.id, show_alert=True, text=damage)
                keyboard = types.InlineKeyboardMarkup()
                mall = types.InlineKeyboardButton(text=text_glava1.local_2, callback_data='mall')
                hospital = types.InlineKeyboardButton(text=text_glava1.local_3, callback_data='hospital')
                mining_railway_station = types.InlineKeyboardButton(text=text_glava1.mining_railway_station, callback_data='mining_railway_station')
                keyboard.add(mall, hospital)
                keyboard.add(mining_railway_station)
                if WIN2 == 'true':
                    win_win = types.InlineKeyboardButton(text=text_glava1.WIN_text, callback_data='flat')
                    keyboard.add(win_win)
                Indicators = text_glava1.HP + '   ' + str(game1[0]) + text_glava1.Energy + '     ' +  str(game1[1]) + text_glava1.Cash + '        ' +  str(game1[2]) 
                bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=Indicators + text_glava1.message_11, reply_markup=keyboard)
        elif game1[0] <= 0:
            bot.edit_message_media(types.InputMediaPhoto(text_glava1.death), chat_id=call.message.chat.id, message_id=call.message.message_id) 
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.death_text) 
            bot.answer_callback_query(call.id, show_alert=True, text=text_glava1.death_text)
            return    

    elif call.data == 'embankment_shop':         # описания работы ТЦ Мощь
        if game1[2] >=5 and game1[1] <= 97:         
            game1[2] = game1[2] - 5
            game1[1] = game1[1] + 3
            keyboard = types.InlineKeyboardMarkup()
            railway_station = types.InlineKeyboardButton(text=text_glava1.local_1, callback_data='railway_station')
            embankment = types.InlineKeyboardButton(text=text_glava1.local_4, callback_data='embankment')
            embankment_shop = types.InlineKeyboardButton(text=text_glava1.embankment_shop_text, callback_data='embankment_shop')
            keyboard.add(embankment, railway_station)
            keyboard.add(embankment_shop)
            if WIN2 == 'true':
                win_win = types.InlineKeyboardButton(text=text_glava1.WIN_text, callback_data='flat')
                keyboard.add(win_win)
            Indicators = text_glava1.HP + '   ' + str(game1[0]) + text_glava1.Energy + '     ' +  str(game1[1]) + text_glava1.Cash + '        ' +  str(game1[2]) 
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=Indicators + text_glava1.message_12, reply_markup=keyboard)
        elif game1[2] < 5:
            bot.answer_callback_query(call.id, show_alert=True, text=text_glava1.non_cash)
        elif game1[2] >=5 and game1[1] > 97:
            game1[1] = 100
            game1[2] = game1[2] - 5
            keyboard = types.InlineKeyboardMarkup()
            railway_station = types.InlineKeyboardButton(text=text_glava1.local_1, callback_data='railway_station')
            embankment = types.InlineKeyboardButton(text=text_glava1.local_4, callback_data='embankment')
            embankment_shop = types.InlineKeyboardButton(text=text_glava1.embankment_shop_text, callback_data='embankment_shop')
            keyboard.add(embankment, railway_station)
            keyboard.add(embankment_shop)
            if WIN2 == 'true':
                win_win = types.InlineKeyboardButton(text=text_glava1.WIN_text, callback_data='flat')
                keyboard.add(win_win)
            Indicators = text_glava1.HP + '   ' + str(game1[0]) + text_glava1.Energy + '     ' +  str(game1[1]) + text_glava1.Cash + '        ' +  str(game1[2]) 
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=Indicators + text_glava1.message_12, reply_markup=keyboard)

    elif call.data == 'treatment':   #Описание больницы
        if game1[2] >10 and game1[0] < 99:
            game1[0] = game1[0] +random.randint(1, 5)
            game1[2] = game1[2] - 10
            keyboard = types.InlineKeyboardMarkup()
            railway_station = types.InlineKeyboardButton(text=text_glava1.local_1, callback_data='railway_station')
            bridge = types.InlineKeyboardButton(text=text_glava1.local_5, callback_data='bridge')
            treatment = types.InlineKeyboardButton(text=text_glava1.treatment_text, callback_data='treatment')
            keyboard.add(railway_station, bridge)
            keyboard.add(treatment)
            if WIN2 == 'true':
                win_win = types.InlineKeyboardButton(text=text_glava1.WIN_text, callback_data='flat')
                keyboard.add(win_win)
            Indicators = text_glava1.HP + '   ' + str(game1[0]) + text_glava1.Energy + '     ' +  str(game1[1]) + text_glava1.Cash + '        ' +  str(game1[2])
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=Indicators + text_glava1.message_13, reply_markup=keyboard)
        elif game1[2] < 10:
            bot.answer_callback_query(call.id, show_alert=True, text=text_glava1.non_cash)
        elif game1[2] >=10 and game1[0] >= 99:
            game1[0] = 100
            game1[2] = game1[2] - 10
            keyboard = types.InlineKeyboardMarkup()
            railway_station = types.InlineKeyboardButton(text=text_glava1.local_1, callback_data='railway_station')
            bridge = types.InlineKeyboardButton(text=text_glava1.local_5, callback_data='bridge')
            treatment = types.InlineKeyboardButton(text=text_glava1.treatment_text, callback_data='treatment')
            keyboard.add(railway_station, bridge)
            keyboard.add(treatmenttrue)
            if WIN2 == 'true':
                win_win = types.InlineKeyboardButton(text=text_glava1.WIN_text, callback_data='flat')
                keyboard.add(win_win)            
            Indicators = text_glava1.HP + '   ' + str(game1[0]) + text_glava1.Energy + '     ' +  str(game1[1]) + text_glava1.Cash + '        ' +  str(game1[2])
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=Indicators + text_glava1.message_13, reply_markup=keyboard)
        
    elif call.data == 'loto':   #описание набережной
        if game1[2] >= 20:
            if random.randint(0, 100) > 20:
                game1[2] = game1[2] - 20
                keyboard = types.InlineKeyboardMarkup()
                mall = types.InlineKeyboardButton(text=text_glava1.local_2, callback_data='mall')
                bridge = types.InlineKeyboardButton(text=text_glava1.local_5, callback_data='bridge')
                loto = types.InlineKeyboardButton(text=text_glava1.loto_text, callback_data='loto')
                keyboard.add(bridge, mall)
                keyboard.add(loto)
                if WIN2 == 'true':
                    win_win = types.InlineKeyboardButton(text=text_glava1.WIN_text, callback_data='flat')
                    keyboard.add(win_win)
                Indicators = text_glava1.HP + '   ' + str(game1[0]) + text_glava1.Energy + '     ' +  str(game1[1]) + text_glava1.Cash + '        ' +  str(game1[2])
                bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=Indicators + text_glava1.message_15, reply_markup=keyboard)
                bot.answer_callback_query(call.id, show_alert=True, text=text_glava1.loto_lose[random.randint(0, 3)])
            else:
                bot.answer_callback_query(call.id, show_alert=True, text=text_glava1.loto_win)
                
                WIN2 = 'true'
        elif game1[2] < 20:
            bot.answer_callback_query(call.id, show_alert=True, text=text_glava1.non_cash)

    elif call.data == 'sleep':   #описание моста
        if game1[0]>=1 and game1[1]<=90:
            game1[0] = game1[0] - random.randint(0, 10)
            game1[1] = game1[1] + 10
            if game1[0] <= 0:
                bot.answer_callback_query(call.id, show_alert=True, text=text_glava1.death_text)
                bot.edit_message_media(types.InputMediaPhoto(text_glava1.death), chat_id=call.message.chat.id, message_id=call.message.message_id) 
                bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.death_text) 
                return
            keyboard = types.InlineKeyboardMarkup()
            hospital = types.InlineKeyboardButton(text=text_glava1.local_3, callback_data='hospital')
            embankment = types.InlineKeyboardButton(text=text_glava1.local_4, callback_data='embankment')
            sleep = types.InlineKeyboardButton(text=text_glava1.leep_text, callback_data='sleep')
            keyboard.add(hospital, embankment)
            keyboard.add(sleep)
            if WIN2 == 'true':
                win_win = types.InlineKeyboardButton(text=text_glava1.WIN_text, callback_data='flat')
                keyboard.add(win_win)
            Indicators = text_glava1.HP + '   ' + str(game1[0]) + text_glava1.Energy + '     ' +  str(game1[1]) + text_glava1.Cash + '        ' +  str(game1[2])
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=Indicators + text_glava1.message_14, reply_markup=keyboard)
        elif game1[0]>=1 and game1[1]>90:
            game1[0] = game1[0] - random.randint(0, 10)
            game1[1] = 100
            keyboard = types.InlineKeyboardMarkup()
            hospital = types.InlineKeyboardButton(text=text_glava1.local_3, callback_data='hospital')
            embankment = types.InlineKeyboardButton(text=text_glava1.local_4, callback_data='embankment')
            sleep = types.InlineKeyboardButton(text=text_glava1.leep_text, callback_data='sleep')
            keyboard.add(hospital, embankment)
            keyboard.add(sleep)
            if WIN2 == 'true':
                win_win = types.InlineKeyboardButton(text=text_glava1.WIN_text, callback_data='flat')
                keyboard.add(win_win)
            Indicators = text_glava1.HP + '   ' + str(game1[0]) + text_glava1.Energy + '     ' +  str(game1[1]) + text_glava1.Cash + '        ' +  str(game1[2])
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=Indicators + text_glava1.message_14, reply_markup=keyboard)
        elif game1[0]<1 and game1[1]>90:
            bot.edit_message_media(types.InputMediaPhoto(text_glava1.death), chat_id=call.message.chat.id, message_id=call.message.message_id) 
            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.death_text) 
            bot.answer_callback_query(call.id, show_alert=True, text=text_glava1.death_text)
            return    

    elif call.data == 'flat':
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.Next, callback_data='flat2')
        keyboard.add(Next)        
        bot.edit_message_media(types.InputMediaPhoto(text_glava1.flat_photo), chat_id=call.message.chat.id, message_id=call.message.message_id) 
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_flat_1, reply_markup=keyboard) 
    elif call.data == 'flat2':
        keyboard = types.InlineKeyboardMarkup()
        Next = types.InlineKeyboardButton(text=text_glava1.new_game, callback_data='start2')
        keyboard.add(Next)        
        bot.edit_message_media(types.InputMediaPhoto(text_glava1.flat_photo), chat_id=call.message.chat.id, message_id=call.message.message_id) 
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=text_glava1.message_flat_2, reply_markup=keyboard) 




if __name__ == '__main__':
     bot.infinity_polling()