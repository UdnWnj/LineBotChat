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
    if "擲筊" in event.message.text:
        sendString = divinationBlocks()
    elif "抽簽" in event.message.text or "抽" in event.message.text:
        sendString = drawStraws()
    elif "奕葶" in event.message.text or "南傑" in event.message.text:
        sendString = drawStraws1()
    elif "吃啥" in event.message.text:
        line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                title='Menu',
                                text='請選擇主食',
                                actions=[
                                    MessageTemplateAction(
                                        label='吃飯',
                                        text='吃飯'
                                    ),
                                    MessageTemplateAction(
                                        label='吃麵',
                                        text='吃麵'
                                    ),
                                    MessageTemplateAction(
                                        label='來點不一樣的',
                                        text='來點不一樣的'
                                    )
                                ]
                            )
                        )
                    )
    elif "吃飯" in event.message.text:
        sendString = drawEatMeal()
    elif "吃麵" in event.message.text:
        sendString = drawEatNoodle()
    elif "來點不一樣的" in event.message.text:
        sendString = drawEatSpecial()
    elif "老王" in event.message.text:
        sendString = "請說，目前詞彙不夠多，你沒講到關鍵字我不會回應您"
    elif "jimmy" in event.message.text:
        line_bot_api.reply_message(
                        event.reply_token,
                        ImageSendMessage(
                            original_content_url='https://upload.wikimedia.org/wikipedia/commons/3/35/%E4%B8%80%E4%BA%BA%C2%B7%E4%B8%80%E5%BC%A0%EF%BD%9CNO.150_%E7%8E%8B%E5%8A%9B%E5%AE%8F.jpg',
                            preview_image_url='https://upload.wikimedia.org/wikipedia/commons/3/35/%E4%B8%80%E4%BA%BA%C2%B7%E4%B8%80%E5%BC%A0%EF%BD%9CNO.150_%E7%8E%8B%E5%8A%9B%E5%AE%8F.jpg'
                            )
                        )
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

def divinationBlocks():
    divinationBlocksList = ["笑杯", "正杯", "正杯", "笑杯"] 
    return divinationBlocksList[random.randint(0, len(divinationBlocksList) - 1)]

def drawStraws():
    drawStrawsList = ["大吉", "中吉", "小吉", "吉", "凶", "小凶", "中凶", "大凶"]
    return drawStrawsList[random.randint(0, len(drawStrawsList) - 1)]

def drawStraws1():
    drawStrawsList = ["這是愛", "三餐都有對方", "床頭吵床尾和", "加油", "王八狗", "不要整天罵髒話", "低能兒", "加油啦"]
    return drawStrawsList[random.randint(0, len(drawStrawsList) - 1)]

def drawC():
    drawStrawsList = ("遠銀, 保誠, 松下, 聯輔, 安麗, 聯合")
    return drawStrawsList


if __name__ == "__main__":
    app.run()
