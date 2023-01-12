import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5979614687:AAHbj6UprKT9hq7jSOSBMS4Ln683EwSEdJg")

API_ID = int(os.environ.get("API_ID", "18995918"))

API_HASH = os.environ.get("API_HASH", "0b9323a97d100a344f88d1fba29efc6a")

STRING = os.environ.get("STRING", "BQAhIHQAnFZVgxCv4JNP9LKtr8CI4zv18rr9cbwGZN1drv7rEMI-bXJF0y64NNpMD5xeBQFOpNOHloV2Xs30LnxhlWExq2Kil7550NV_Wrp9wtBA6g1yFiuGPWYsgyKYfQN43_ikeHu8ygd0ZoMrs2TsdHtt64iCWAn7ovHkraho-bDTWBzY7Rcb97o0pfRDRpQJQvC9BkbKu_2cMno0QqpURU998MBdBvX4WuRsuQ4W3oKlfxQK77ttJqmzU3xOhspW0WZByiwiRPVNqYyDiBpJOJzg0_q_q3uFC6MhFoIaf2OcwUqkdb_Qnhp636tOueG1PIorp0Pafy8JjwS5rc2xwB8qwQAAAAB-SFukAA")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
