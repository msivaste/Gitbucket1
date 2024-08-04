class laptop():
    class laptop:
        def __init__(self):
            self.ram = ""
            self.processor = ""

        def config(self):
            print("RAM: ", self.ram)
            print("Processor: ", self.processor)

    hp = laptop()
    hp.ram = "16 GB"
    hp.processor = "i7"

    dell = laptop()
    dell.ram = "8 GB"
    dell.processor = "i5"

    hp.config()
    dell.config()