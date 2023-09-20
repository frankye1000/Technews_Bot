import os
import telebot
import requests
from datetime import date
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters


# 爬取最新科技新報資訊
def CrawlUrl(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html5lib")
    t = soup.select("td.maintitle > h1.entry-title > a")
    newest5 = [i.get("href") for i in t[:5]]  # 只拿五個最新新聞
    return newest5


# 手動要求(使用/)傳送最新資訊
async def MaunalCommands_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text=='/component':
        newest5 = CrawlUrl("https://technews.tw/category/component/")
        for text in newest5:
            await update.message.reply_text(text)
        await update.message.reply_text("預知更多最新新聞，請參考:\nhttps://technews.tw/category/component/")

    elif update.message.text=='/mobiledevice':
        newest5 = CrawlUrl("https://technews.tw/category/mobiledevice/")
        for text in newest5:
            await update.message.reply_text(text)
        await update.message.reply_text("預知更多最新新聞，請參考:\nhttps://technews.tw/category/mobiledevice/")

    elif update.message.text=='/internet':
        newest5 = CrawlUrl("https://technews.tw/category/internet/")
        for text in newest5:
            await update.message.reply_text(text)
        await update.message.reply_text("預知更多最新新聞，請參考:\nhttps://technews.tw/category/internet/")

    elif update.message.text=='/ai':
        newest5 = CrawlUrl("https://technews.tw/category/ai/")
        for text in newest5:
            await update.message.reply_text(text)
        await update.message.reply_text("預知更多最新新聞，請參考:\nhttps://technews.tw/category/ai/")

    elif update.message.text=='/cuttingedge':
        newest5 = CrawlUrl("https://technews.tw/category/cutting-edge/")
        for text in newest5:
            await update.message.reply_text(text)
        await update.message.reply_text("預知更多最新新聞，請參考:\nhttps://technews.tw/category/cutting-edge/")

    elif update.message.text=='/biotech':
        newest5 = CrawlUrl("https://technews.tw/category/biotech/")
        for text in newest5:
            await update.message.reply_text(text)
        await update.message.reply_text("預知更多最新新聞，請參考:\nhttps://technews.tw/category/biotech/")

    elif update.message.text=='/finance':
        newest5 = CrawlUrl("https://finance.technews.tw/")
        for text in newest5:
            await update.message.reply_text(text)
        await update.message.reply_text("預知更多最新新聞，請參考:\nhttps://finance.technews.tw/")

# 手動(隨意傳送任意訊息)傳送最新資訊
async def MaunalCommands_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatid = "1093911183"
    # print(update.message.chat.id)
    
    title = "   {} 科技新報   \n".format(date.today())
    await context.bot.send_message(chat_id=chatid, text=title)
    newest5 = CrawlUrl("https://technews.tw/")
    for text in newest5:
        await context.bot.sendMessage(chat_id=chatid, text=text)


# 主動傳遞最新訊息
def AutoCommand(tokens, chatid):
    bot = telebot.TeleBot(tokens)
    title = "   {} 科技新報   \n".format(date.today())
    bot.send_message(chatid, title)
    newest5 = CrawlUrl("https://technews.tw/")
    for text in newest5:
        bot.send_message(chat_id=chatid, text=text)


if __name__ == '__main__':
    tokens = os.getenv('TELEBOT_TOKENS')
    chatid = os.getenv('TELEBOT_CHATID')
    
    app = Application.builder().token(tokens).build()

    # commands 科技新報各單元
    app.add_handler(CommandHandler("component", MaunalCommands_1))
    app.add_handler(CommandHandler("mobiledevice", MaunalCommands_1))
    app.add_handler(CommandHandler("internet", MaunalCommands_1))
    app.add_handler(CommandHandler("ai", MaunalCommands_1))
    app.add_handler(CommandHandler("cuttingedge", MaunalCommands_1))
    app.add_handler(CommandHandler("biotech", MaunalCommands_1))
    app.add_handler(CommandHandler("finance", MaunalCommands_1))
    app.add_handler(MessageHandler(filters=filters.TEXT, callback=MaunalCommands_2))
    
    print("start polling")
    AutoCommand(tokens, chatid)
    # 開始運作bot
    app.run_polling()