from datetime import datetime
dt = datetime(2015, 4, 19, 12, 20)
print( dt.timestamp() )
tt = dt.timestamp()
print( datetime.fromtimestamp( tt ) )
print(datetime.utcfromtimestamp( tt ))
# from datetime import datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)