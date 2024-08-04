class laptop:
    Price=0
    Processor = ""
    Ram = ""
dell = laptop()
dell.Price = 50000
dell.Processor = "Intel i5"
dell.Ram = "16 GB"

HP = laptop()
HP.Price = 40000
HP.Processor = "Intel i7"
HP.Ram = "32 GB"

Lenovo = laptop()
Lenovo.Price = 45000
Lenovo.Processor = "Intel i8"
Lenovo.Ram = "64 GB"

print("Dell :",dell.Price,dell.Processor,dell.Ram)
print("HP :",HP.Price,HP.Processor,HP.Ram)
print("Lenovo :",Lenovo.Price,Lenovo.Processor,Lenovo.Ram)

