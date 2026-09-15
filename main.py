import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    welcome_message = (
        f"أهلاً بكِ يا {user_name} في نظام **T-Deal Pro** للخدمات العقارية.\n\n"
        "هذا البوت مخصص لإدارة التحقق من التراخيص العقارية واستقبال الاستفسارات.\n"
        "أرسلي رقم الترخيص أو الاستفسار للبدء."
    )
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "ترخيص" in text or "رقم" in text:
        reply_text = "تم استلام طلب التحقق من الترخيص بنجاح. جاري مراجعة البيانات..."
    else:
        reply_text = "مرحباً بكِ. يرجى إرسال تفاصيل الطلب أو الاستفسار العقاري."
        
    await update.message.reply_text(reply_text)

def main():
    TOKEN = "8615081605:AAHPghjKyYB0alTH6cHqgkBIRz7y62QjspY"

    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("جاري تشغيل بوت T-Deal Pro...")
    application.run_polling()

if __name__ == '__main__':
    main()
