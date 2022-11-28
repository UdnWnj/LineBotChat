from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
#from linebot.models import MessageEvent, TextMessage, TextSendMessage
import configparser
import random

from linebot.models import *


app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        print(body, signature)
        handler.handle(body, signature)

    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent)
def prettyEcho(event):

    sendString = ""
    if "@客戶資訊" == event.message.text:
        line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                title='客戶資訊',
                                text='請選擇客戶',
                                actions=[
                                    MessageTemplateAction(
                                        label='遠銀',
                                        text='@遠銀'
                                    ),
                                    MessageTemplateAction(
                                        label='保誠',
                                        text='@保誠'
                                    ),
                                    MessageTemplateAction(
                                        label='松下',
                                        text='@松下'
                                    ),
                                    MessageTemplateAction(
                                        label='下一頁',
                                        text='@客戶資訊頁02'
                                    )
                                ]
                            )
                        )
                    )
    elif "@客戶資訊頁02" == event.message.text:
        line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                title='客戶資訊',
                                text='請選擇客戶',
                                actions=[
                                    MessageTemplateAction(
                                        label='安麗',
                                        text='@安麗'
                                    ),
                                    MessageTemplateAction(
                                        label='聯合',
                                        text='@聯合'
                                    )
                                ]
                            )
                        )
                    )
    elif "@遠銀" == event.message.text:
        line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                title='遠銀客戶資訊',
                                text='請選擇資訊',
                                actions=[
                                    MessageTemplateAction(
                                        label='遠銀聯絡窗口',
                                        text='@遠銀聯絡窗口'
                                    )
                                ]
                            )
                        )
                    )
    elif "@保誠" == event.message.text:
        line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                title='保誠客戶資訊',
                                text='請選擇資訊',
                                actions=[
                                    MessageTemplateAction(
                                        label='保誠聯絡窗口',
                                        text='@保誠聯絡窗口'
                                    )
                                ]
                            )
                        )
                    )
    elif "@松下" == event.message.text:
        line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                title='松下客戶資訊',
                                text='請選擇資訊',
                                actions=[
                                    MessageTemplateAction(
                                        label='松下聯絡窗口',
                                        text='@松下聯絡窗口'
                                    )
                                ]
                            )
                        )
                    )
    elif "@安麗" == event.message.text:
        line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                title='安麗客戶資訊',
                                text='請選擇資訊',
                                actions=[
                                    MessageTemplateAction(
                                        label='安麗聯絡窗口',
                                        text='@安麗聯絡窗口'
                                    )
                                ]
                            )
                        )
                    )
    elif "@聯合" == event.message.text:
        line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                title='聯合客戶資訊',
                                text='請選擇資訊',
                                actions=[
                                    MessageTemplateAction(
                                        label='聯合聯絡窗口',
                                        text='@聯合聯絡窗口'
                                    )
                                ]
                            )
                        )
                    )
        
    elif "@遠銀設備訊息" in event.message.text or "@保誠設備訊息" in event.message.text or "@松下設備訊息" in event.message.text or "@聯合設備訊息" in event.message.text:
        sendString = "http://gofile.me/6YIKR/7kR08UplZ" + " 密碼:123456"
    

    elif "聯絡窗口" in event.message.text:
        sendString = drawCline(event.message.text)
    elif "@NTT" in event.message.text:
        sendString = drawC()
    else:
        sendString = ""

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=sendString)
    )
def drawEatMeal():
    drawStrawsList = ["滷肉飯", "三寶飯", "雞肉飯", "雞腿飯", "控肉販", "魚肉飯", "排骨飯", "炒飯"]
    return drawStrawsList[random.randint(0, len(drawStrawsList) - 1)]
def drawEatNoodle():
    drawStrawsList = ["烏龍麵", "鍋燒麵", "拉麵", "擔仔麵", "炒麵", "泡麵", "麵線", "米粉湯", "牛肉麵"]
    return drawStrawsList[random.randint(0, len(drawStrawsList) - 1)]
def drawEatSpecial():
    drawStrawsList = ["小火鍋", "日本料理", "排餐", "大火鍋", "燒烤", "韓國料理", "泰國菜", "鐵板燒"]
    return drawStrawsList[random.randint(0, len(drawStrawsList) - 1)]
def drawCline(text):
    match(text):
        case ("@遠銀聯絡窗口"):
            print("1")
            return "張峻源"
        case ("@保誠聯絡窗口"):
            print("2")
            return "邱梅芳"
        case ("@松下聯絡窗口"):
            print("3")
            return "吳坤錫"
        case ("@聯合聯絡窗口"):
            print("3")
            return "廖志明"

def drawC():
    drawStrawsList = ("遠銀, 保誠, 松下, 聯輔, 安麗, 聯合")
    return drawStrawsList


if __name__ == "__main__":
    app.run()
