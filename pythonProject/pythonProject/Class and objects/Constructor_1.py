class laptop:
    def __init__(self):
        self.ram =""
        self.processor = ""
    def config(self):
        print("RAM: ",self.ram)
        print("Processor: ",self.processor)
enq = laptop()
enq.ram = "16 GB"
enq.processor = "i5"
enq.config()

dell = laptop()
dell.ram = "32 GB"
dell.processor = "i7"
dell.config()