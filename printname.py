class IntValueError(Exception):
    def __init__(self, msg):
        self.msg = msg
        

a = 10
b =2

if type(int(((a/b)**0.2)**2)) != int:
    raise IntValueError('result is not in integer')
else:
    print(a/b)