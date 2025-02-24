import cv2
import os
import string

img = cv2.imread("rolls.jpg") # Replace with the correct image path#image

msg = input("Enter secret message:")
password = input("Enter a passcode:")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption")
if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")   

# Decryption Process
img = cv2.imread("encryptedImage.jpg")  # Reload the image
decrypted_message = ""
msg_index = 0

# User enters the passcode for decryption
pas = input("Enter passcode for Decryption: ")

if pas == password:  # Verify password
    for row in range(height):
        for col in range(width):
            for channel in range(3):
                char = chr(img[row, col, channel])  # Convert ASCII back to character
                if char == "~":  # Stop at termination marker
                    print("Decrypted message:", decrypted_message)
                    exit()
                decrypted_message += char
else:
    print("ERROR: Incorrect passcode!")

