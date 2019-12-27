## 모듈, 패키지


# from animal import dog  # animal 패키지에서 dog 라는 모듈을 갖고와줘
# from animal import cat  # animal 패키지에서 cat 라는 모듈을 갖고와줘
# from animal import *    # animal 패키지에가 갖고있는 모듈을 다 불러와
#
# d = dog.Dog()   # instancd
#
# c = cat.Cat()
#
# d.hi()
# c.hi()


from geopy.geocoders import Nominatim       #from animal.dog import Dog와 같음
geolocator = Nominatim(user_agent="daewon")
location = geolocator.geocode("Seoul, South Korea")
print(location.address)
print(location.latitude, location.longitude)
print(location.raw)