def func():
    pass

class Abc(object):

    template_name = "index.html"

    def __init__(self, value):
        self.value = value

obj = Abc('smth')
print obj.template_name
obj.template_name = '123'
print obj.template_name
print Abc.template_name