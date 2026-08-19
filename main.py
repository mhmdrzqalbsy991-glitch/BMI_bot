import telebot

API_TOKEN = '8937260104:AAHV42biNVvPdcck3So5FEMXVdoLHz2vHFQ'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً بك! أنا بوت ذكي. أرسل طولك ووزنك (مثال: 155 78) وسأخبرك بنتيجتك ونصائح صحية.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.strip()
    try:
        parts = text.split()
        if len(parts) == 2:
            h = float(parts[0]) / 100
            w = float(parts[1])
            bmi = round(w / (h ** 2), 2)
            
            # الرد الذكي المدمج
            advice = "💡 نصيحة: حافظ على شرب الماء وممارسة الرياضة!"
            if bmi < 18.5: advice = "💡 لديك نقص وزن، اهتم بزيادة السعرات الصحية."
            elif bmi >= 25: advice = "💡 لديك زيادة وزن، جرب المشي يومياً لـ 30 دقيقة."
            
            bot.reply_to(message, f"📊 مؤشر كتلة جسمك هو: {bmi}\n{advice}")
        else:
            bot.reply_to(message, "أهلاً! أنا هنا للمساعدة. أرسل الطول والوزن كرقمين فقط (مثال: 155 78).")
    except:
        bot.reply_to(message, "من فضلك تأكد من إرسال أرقام صحيحة.")

print("البوت الذكي يعمل الآن...")
bot.infinity_polling()
