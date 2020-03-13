def str_data():
    data = "hi Dave"
    for item in data:
        return item

char = iter(str_data())
next(char)

def str_data():
    data = "hi Dave"
    for item in data:
        yield item
str_data()
char = iter(str_data())
next(char)