import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# إعداد السجل (Logging) لمعرفة حالة البوت أولاً بأول
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# التوكن الخاص ببوت T-Deal Pro
TOKEN = '8615081605:AAHPghjKyYB0alTH6cHqgkBIRz7y62QjspY'

# دالة أمر البدء /start لإظهار الأزرار السفلية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    
    # رسالة الترحيب الاحترافية
    welcome_message = (
        f"أهلاً بك يا {user_name} في **T-Deal Pro** للخدمات العقارية.\n"
        "هذا البوت مخصص لإدارة التحقق من التراخيص العقارية واستقبال الاستفسارات.\n"
        "اختر إحدى الخدمات من القائمة أدناه أو أرسل رقم الترخيص:"
    )
    
    # تصميم الأزرار السفلية (Reply Keyboard)
    keyboard = [
        [KeyboardButton("لوحة تحكم إدارة البوت (الأدمن)")],
        [KeyboardButton("تقديم طلب اعتماد (التراخيص العقارية)")],
        [KeyboardButton("إدارة حالة العقارات (للمسوق)")],
        [KeyboardButton("استعراض العقارات (للعميل)")],
        [KeyboardButton("إدخال صفقة عقارية (للمسوق)")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(welcome_message, reply_markup=reply_markup, parse_mode='Markdown')

# دالة الاستجابة لضغطات الأزرار والنصوص المرسلة
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if "لوحة تحكم" in text:
        await update.message.reply_text("⚙️ أهلاً بك في لوحة تحكم الأدمن. جاري تحميل الصلاحيات والإعدادات...")
    elif "تقديم طلب اعتماد" in text:
        await update.message.reply_text("📝 تم استلام طلب التحقق من الترخيص بنجاح. جاري مراجعة البيانات...")
    elif "إدارة حالة العقارات" in text:
        await update.message.reply_text("📋 قائمة العقارات المسجلة لديناميكية التحديث وتعديل حالتها.")
    elif "استعراض العقارات" in text:
        await update.message.reply_text("🏢 تفضل استعراض أحدث العقارات المتاحة حالياً في السوق العقاري.")
    elif "إدخال صفقة عقارية" in text:
        await update.message.reply_text("💰 مرحباً بك. يرجى إرسال تفاصيل الصفقة أو الاستفسار العقاري الجديد.")
    else:
        await update.message.reply_text(f"أهلاً بك. لقد استلمت نصك: {text}")

def main():
    # بناء التطبيق وإدخال التوكن
    application = ApplicationBuilder().token(TOKEN).build()

    # ربط الأوامر والمعالجات بالبوت
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_buttons))

    print("جاري تشغيل بوت T-Deal Pro...")
    # تشغيل البوت بسلاسة
    application.run_polling()

if __name__ == '__main__':
    main()
