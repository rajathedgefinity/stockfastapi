import yfinance as yf

hgs = yf.Ticker("SBIN.NS")

print(hgs.info)
