import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('أهلاً بك! أنا بوت حساب مؤشر كتلة الجسم. أرسل لي طولك (بالسم) ووزنك (بالكجم) وسأحسب لك النتيجة.')

async def calculate_bmi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = update.message.text.split()
        height = float(text[0]) / 100
        weight = float(text[1])
        bmi = weight / (height * height)
        await update.message.reply_text(f'مؤشر كتلة جسمك هو: {bmi:.2f}')
    except:
        await update.message.reply_text('يرجى إرسال الطول والوزن فقط، مثل: 175 70')

if __name__ == '__main__':
    TOKEN = os.environ.get('TOKEN')
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("bmi", calculate_bmi))
    
    print("البوت يعمل الآن...")
    app.run_polling()
