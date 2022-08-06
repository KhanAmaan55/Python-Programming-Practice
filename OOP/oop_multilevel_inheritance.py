class electronic_devices:
    electricity=12

class pocket_gadget(electronic_devices):
    size=34

class phone(pocket_gadget):
    functions= 12


tv= electronic_devices()
mini_radio= pocket_gadget()
micromax= phone()

print(tv.electricity)
print(pocket_gadget.electricity)
print(pocket_gadget.size)
print(phone.electricity)
print(phone.size)
print(phone.functions)
