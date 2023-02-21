from bot import Bot
import MetaTrader5 as mt5


mt5.initialize()

macd_bot = Bot(20.00, 60, "EURUSD") # 0.00 - LOTS, || 60 is setting for M1 so 60 seconds. For M5 simple is 60*5, || "SYMBOL"

macd_bot.start()
macd_bot.wait()