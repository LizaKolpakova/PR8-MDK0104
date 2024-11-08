class RealString:
    def __init__(self, string):
        self.string = string

    def __len__(self):
        return len(self.string)

    def __gt__(self, other):
        if isinstance(other, str):
            other = RealString(other)
        return len(self.string) > len(other.string)

    def __lt__(self, other):
        if isinstance(other, str):
            other = RealString(other)
        return len(self.string) < len(other.string)


real_apple = RealString("App")
real_yabliko = RealString("ф")

print(real_apple < "Яблоко")  
print(real_yabliko > "Apple")  
print(real_apple == real_yabliko)  





