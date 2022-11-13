from PIL import Image, ImageGrab
import pyautogui
import time

rw1 = 195
rw2 = 167
rw3 = 193

start = time.time()
pyautogui.press("up")
end = time.time()
print(end - start)

# while True:
#     im2 = ImageGrab.grab(bbox = None)
#     r1, g1, b1 = im2.getpixel((656, 515))
#     r2, g2, b2 = im2.getpixel((745, 655))
#     r3, g3, b3 = im2.getpixel((775, 795))
    
#     if r1 == 185 or r1 == 153:
#         print("Apple Detected Top.")
#         pyautogui.press("up")  
        
    
#     if r2 == 185 or r2 == 153:
#         print("Apple Detected Middle.")
#         pyautogui.press("right")

#     if r3 == 185 or r3 == 153:
#         print("Apple Detected Bottom.")
#         pyautogui.press("down")
