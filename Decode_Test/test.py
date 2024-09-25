# Just a test cus i was having trouble with decode initially hahaha
import base64
target_path = "target.png"

with open(target_path, 'rb') as file:
    target_encode = base64.b64encode(file.read())
    target_encode = target_encode.decode()

print(target_encode)    