import cv2
import os
import numpy as np
k = []
colors = [[255,0,0],[255,128,0],[255,153,255],[255,1,255],[25,255,150],[125,150,255]]
def funcBrightContrast(option=0,bright=0,h=1,Blur = 1,mor =1,size = 1,bord=1,bordclr=1):
    option = cv2.getTrackbarPos("option","Patel ki jaaki")
    h = cv2.getTrackbarPos("h","Patel ki jaaki")
    Blur = cv2.getTrackbarPos("Blur","Patel ki jaaki")
    bright = cv2.getTrackbarPos('bright', 'Patel ki jaaki')
    contrast = cv2.getTrackbarPos('contrast', 'Patel ki jaaki')
    mor = cv2.getTrackbarPos("mor","Patel ki jaaki")
    size = cv2.getTrackbarPos("size","Patel ki jaaki")
    bord = cv2.getTrackbarPos("bord","Patel ki jaaki")
    bordclr = cv2.getTrackbarPos("bordclr","Patel ki jaaki")
    for x in os.listdir('.'):
        if x.endswith(".jpg") or x.endswith(".png") or x.endswith(".jfif"):
            k.append(x)
    if option == 0:
       # colors = [[255,0,0],[255,128,0],[255,153,255],[255,1,255],[25,255,150],[125,150,255]]
        
        img = cv2.imread(k[h])

        h1,w = img.shape[:2]
        res = cv2.resize(img,((h1*5)//int(size+1),(w*5)//int(size+1)),interpolation = cv2.INTER_NEAREST)
        effect = apply_brightness_contrast(res,bright,contrast)
        blur = cv2.blur(effect,(Blur+2,Blur*2))
        #kernel = np.ones((mor,mor),np.uint8)
        #opening = cv2.morphologyEx(blur, cv2.MORPH_BLACKHAT, kernel)
        Bord= cv2.copyMakeBorder(blur,bord,bord,bord,bord,cv2.BORDER_CONSTANT,value=colors[bordclr])
        cv2.imshow('Patel ki jaaki1',Bord )
        print(str(k[h]),Bord.size)
        
        
        l = cv2.waitKey(0)
        if l==27:
            cv2.destroyAllWindows()
        elif l == ord('p'):
            s = k[h].split('.')
            s = str(s[0])+".png"
            cv2.imwrite(s,blur)
            print("success")
            
    else:
         img = cv2.imread(k[h])
         h1,w = img.shape[:2]
         res = cv2.resize(img,((h1*5)//int(size+1),(w*5)//int(size+1)),interpolation = cv2.INTER_NEAREST)
         effect = apply_brightness_contrast(res,bright,contrast)
         blur = cv2.blur(effect,(Blur+2,Blur*2))
         kernel = np.ones((mor,mor),np.uint8)
         opening = cv2.morphologyEx(blur, cv2.MORPH_BLACKHAT, kernel)
         cv2.imshow('Patel ki jaaki1',opening )
         print(str(k[h]),opening.size)
         l = cv2.waitKey(0)
         if l==27:
             cv2.destroyAllWindows()
         elif l == ord('p'):
             s = k[h].split('.')
             s = str(s[0])+"1"+".png"
             cv2.imwrite(s,opening)
             print("success")

def apply_brightness_contrast(input_img, brightness = 255, contrast = 127):
    brightness = map(brightness, 0, 510, -255, 255)
    contrast = map(contrast, 0, 254, -127, 127)
 
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow)/255
        gamma_b = shadow
 
        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()
 
    if contrast != 0:
        f = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127*(1-f)
 
        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)
 
    #cv2.putText(buf,'B:{},C:{}'.format(brightness,contrast),(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return buf
 
def map(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)
 
if __name__ == '__main__':
 
   # original = cv2.imread("prakash.jpg", 1)
    #img = original.copy()
 
    cv2.namedWindow('Patel ki jaaki')
    cv2.namedWindow('Patel ki jaaki1')
    
 
    bright = 255
    contrast = 127
    h = 1
    Blur=1
    mor=1
    option = 1
    size = 1
    bord = 1
    bordclr = 1
    #Brightness value range -255 to 255
    #Contrast value range -127 to 127
    cv2.createTrackbar("option","Patel ki jaaki",0,1,funcBrightContrast)
    cv2.createTrackbar("h","Patel ki jaaki",0,25,funcBrightContrast)
    Blur = cv2.createTrackbar("Blur","Patel ki jaaki",1,5,funcBrightContrast)
    cv2.createTrackbar('bright', 'Patel ki jaaki', bright, 2*255, funcBrightContrast)
    cv2.createTrackbar('contrast', 'Patel ki jaaki', contrast, 2*127, funcBrightContrast)
    cv2.createTrackbar("mor","Patel ki jaaki",0,1000,funcBrightContrast)
    cv2.createTrackbar("size","Patel ki jaaki",1,20,funcBrightContrast)
    cv2.createTrackbar("bord","Patel ki jaaki",1,20,funcBrightContrast)
    cv2.createTrackbar("bordclr","Patel ki jaaki",1,len(colors),funcBrightContrast)
    funcBrightContrast(0,0,0,0,0,0,0)
   # cv2.imshow('Patel ki jaaki', original)
 
 
cv2.waitKey(0)
  
