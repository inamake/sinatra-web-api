# coding: utf-8

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
import requests
import json

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                               文字列中に':'はいらない

# weather hack から取得
location_id = 280010  # 神戸
weather_data = requests.get(
    'http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'
        % location_id).json()

crip = weather_data['description']['text']

@respond_to('こんにちは')
def mention_func(message):
    message.reply('ごきげんよう') # メンション

@listen_to('こんばんは')
def listen_func(message):
    message.send('もう夜ですね')      # ただの投稿
    message.reply('おこんばんは')         # メンション

@respond_to('こんばんは')
def mention_func(message):
    message.reply('おこんばんは') # メンション

@listen_to('こんにちは')
def listen_func(message):
    #message.send('')      # ただの投稿
    message.reply('ごきげんよう')         # メンション

@respond_to('天気')
def mention_func(message):
    message.send('今日の神戸市の天気です')
    message.reply(crip) # メンション

@listen_to('天気')
def listen_func(message):
    message.send('今日の神戸市の天気です')      # ただの投稿
    message.reply(crip)         # メンション

@respond_to('ありがとう')
def cool_func(message):
    message.reply('こちらこそ')     # メンション
    message.react('+1')     # リアクション
