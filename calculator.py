class Calculator:
    def add(self, a , b):
        if not isinstance(a, (float, int)) or not instance(b, (float, int)):
            raise TypeError("[CUSTOM ERROR] - numeric only!")
        return a + b