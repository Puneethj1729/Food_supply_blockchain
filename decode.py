
from pyzbar.pyzbar import decode
from PIL import Image
import hashlib

# function to return key for any value
def get_key(val, dict):
    for key, value in dict.items():
         if val == value:
             return key

    return "key doesn't exist"
class Food:
    def __init__(self, name, variety, farm, size, production_date, expiry_date):
        self.name = name
        self.variety = variety
        self.farm = farm
        self.size = size
        self.production_date = production_date
        self.expiry_date = expiry_date
        self.info = name + ";" + variety + ";" + farm + ";" + size + ";" + production_date + ";" + expiry_date

#create a dictionary of farmers with their unique has code
farmers_dict = {
  "Farm Bangalore": str(hashlib.sha256("Farm Bangalore".encode()).hexdigest()),
  "Farm Chennai": str(hashlib.sha256("Farm Chennai".encode()).hexdigest()),
  "Farm Hyderabad": str(hashlib.sha256("Farm Hyderabad".encode()).hexdigest())
}

qr = decode(Image.open('qrcode_butter.png'))

print(qr[0].data)
decoded_item = str(qr[0].data).split(";")

farm = get_key(decoded_item[2], farmers_dict)
food_item = Food(decoded_item[0], decoded_item[1], farm, decoded_item[3], decoded_item[4], decoded_item[5])

#Info
print("Item name: " + food_item.name + "\n")
print("Variety: " + food_item.variety + "\n")
print("Farm: " + food_item.farm + "\n")
print("Size: " + food_item.size + "\n")
print("Production date: " + food_item.production_date + "\n")
print("Expiry date: " + food_item.expiry_date + "\n")
