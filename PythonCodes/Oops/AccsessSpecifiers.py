class MyClass:
    def __init__(self):
        self._internal_variable = 42

    def get_internal_variable(self):
        return self._internal_variable

obj = MyClass()
print(obj.get_internal_variable())
