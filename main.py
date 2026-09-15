import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# إعداد التسجيل للأخطاء
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# الحصول على التوكن من متغيرات البيئة أو التوكن المباشر
TOKEN = os.getenv("BOT_TOKEN", "8615081605:AAHU4-psk175-pg3ZYyyEscefPkkJqq1FV8")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك في بوت T-Deal Pro! البوت يعمل الآن بنجاح.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    # إضافة أمر /start
    app.add_handler(CommandHandler("start", start))
    
    print("البوت قيد التشغيل...")
    app.run_polling()
