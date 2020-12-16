import cv2 as c
import os
import matplotlib.pyplot as plt
face=c.CascadeClassifier(c.data.haarcascades+'haarcascade_frontalface_default.xml')
eye=c.CascadeClassifier(c.data.haarcascades+"haarcascade_eye.xml")
#img1=c.imread('sabari.jpg')
#gray1=c.cvtColor(img1,c.COLOR_BGR2GRAY)
#f1=face.detectMultiScale(gray1,1.3,5)
cap1=c.VideoCapture(0)
xl=1000
xh=0
yl=1000
yh=0
wl=1000
wh=0
hl=100
hh=0
ewl=1000
ewh=0
ehl=100
ehh=0
c1=0
while True:
    ret1,img1=cap1.read()
    gray1=c.cvtColor(img1, c.COLOR_BGR2GRAY)
    f1=face.detectMultiScale(gray1,1.3,1)
    print(len(f1))
    if len(f1)==1:
        for (x1,y1,w1,h1) in f1:
            #x2,y2,w2,h2=x1,y1,w1,h1
            if xh<x1 :
                xh=x1
            if xl>x1:
                xl=x1
            if yh<y1:
                yh=y1
            if yl>y1:
                yl=y1
            if wh<w1:
                wh=w1
            if wl>w1:
                wl=w1
            if hh<h1:
                hh=h1
            if hl>h1:
                hl=h1

            c.rectangle(img1,(x1,y1),(x1+w1 , y1+h1),(255,0,0),5)
            
            e1=eye.detectMultiScale(gray1,1.3,2)
            if len(e1)==2:
                for (ex1,ey1,ew1,eh1) in e1:
                    if ewh<ew1:
                        ewh=ew1
                    if ewl>ew1:
                        ewl=ew1
                    if ehh<eh1:
                        ehh=eh1
                    if ehl>eh1:
                        ehl=eh1
                    c.rectangle(img1,(ex1,ey1),(ex1+ew1 , ey1+eh1),(0,255,0),5)
                    c.putText(img1,'correct',org=(x1,y1),fontFace=c.FONT_HERSHEY_SIMPLEX,fontScale=2,color=(0,0,255),thickness=5)
        c.imshow('img1',img1) 
        k1=c.waitKey(1)
        if k1==ord('a'):
            break
cap1.release()
c.destroyAllWindows()
cap=c.VideoCapture(0)
while True:
    ret, img=cap.read()
   # c.imshow('img',img)
    gray=c.cvtColor(img, c.COLOR_BGR2GRAY)
    f=face.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in f:
        c1=0
        if (x<xh and y<yh) and (x>xl and y>xl) and h>hl and h<hh:
            c.rectangle(img,(x,y),(x+w , y+h),(0,255,0),5)
            #c.addText(img,"you are correct",org=None,nameFont=None,color='red')
            c.putText(img,'correct',org=(x1,y1),fontFace=c.FONT_HERSHEY_SIMPLEX,fontScale=2,color=(255,0,0),thickness=5)
           
        else:
            c.rectangle(img,(x,y),(x+w , y+h),(0,0,255),5) 
            c.putText(img,'your position wrong',org=(x1,y1),fontFace=c.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(255,0,0),thickness=5)
        e=eye.detectMultiScale(gray,1.3,2)
        for (ex,ey,ew,eh) in e:
            if ew>ewl and ew<ewh and eh>ehl and eh<ehh:
                c.rectangle(img,(ex,ey),(ex+ew , ey+eh),(0,255,0),5)
            else:
                c.rectangle(img,(ex,ey),(ex+ew , ey+eh),(0,0,255),5)
    else:
        c1=c1+1
    if c1>100:
        c.putText(img,'face not detect',org=(x1,y1),fontFace=c.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,0,255),thickness=5)
    #plt.imshow(img)
    c.imshow('img',img)
    k= c.waitKey(1) 
    if k==ord('q'):
        break


cap.release()
c.destroyAllWindows()


