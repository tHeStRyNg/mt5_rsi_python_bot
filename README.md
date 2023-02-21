# mt5_rsi_python_bot
Client Server MT5 RSI Python Bot
## Dependencies Instalation
1. pip install requirements.txt
2. python main.py
3. compile the RSI_client.mq5
4. Make sure:
- main.py reflects the LOTS, TIMEFRAME, SYMBOL
- orders.py configure CANDLES_BETWEEN_OPERATIONS, SL, TP, RSI_TOP, RSI_BOTTOM
5. Add the new EA or RSI_client.ex5 (compiled version) to your Chart
6. Bot should start if you see on the Journal a similar line ```2023.02.21 22:33:05.718	Expert RSI_client (EURUSD,M1) loaded successfully```
