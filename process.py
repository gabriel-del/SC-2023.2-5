import datetime

timestamp = 1230940800000 / 1000  # Seconds since Unix epoch
date = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')

print(date)
