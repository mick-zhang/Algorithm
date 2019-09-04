class Laptop:
    
    def __init__(self, brandName, screenSize):
        self.brandName = brandName
        self.screenSize = screenSize
    
    def specs(self):
        return self.brandName + " " + self.screenSize
    
    def __str__(self):
        return self.brandName + " " + self.screenSize
    
class Desktop(Laptop):
    
    def __init__(self, brandName, screenSize, keyboard, mouse, speaker):
        super(Desktop, self).__init__(brandName, screenSize)
        
        self.keyboard = keyboard
        self.mouse = mouse
        self.speaker = speaker
        
    def peripherals(self):
        return self.keyboard + ", " + self.mouse + ", " + self.speaker
    
    
def main():
    Computer1 = Laptop("Mac", "15.1 inch")
    Computer2 = Desktop("Asus", "27 inch", "wireless keyboard", "gaming mouse", "bluetooth speaker")
    
    results = [Computer1.specs(), Computer2.specs(), Computer2.peripherals()]
    
    for result in results:
        print(result)
        
main()
