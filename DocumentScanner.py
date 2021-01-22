import cv2 # importing openCV
from fpdf import FPDF #importing FPDF from fpdf
import os #importing os module used for interacting with operating system
url ="http://192.168.43.1:8080/video" #write your url here
cap= cv2.VideoCapture(url)
ret =True
f1=0
i=0
while ret:
    ret, frame=cap.read()
    if f1==0:
        print("press 's' to scan the document")
        f1=f1+1
    cv2.imshow("camera feed",frame)
    k= cv2.waitKey(1)
    if k==ord('s'):
        cv2.destroyWindow("camera feed")
        cv2.imshow("Scanned photo",frame)
        print("press u if its unreadable")
        print("press b to convert it to black and white form")
        print("press anything else to esc")
        k=cv2.waitKey(0)
        if  k== ord('u'):
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            new=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,155,1)
            cv2.imwrite("E://pdf//scanned%d.jpg"%i,new)
            i = i+1
            f1 = 0
            continue
        elif k==ord('b'):
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
            cv2.imwrite("E://pdf//scanned%d.jpg"%i,gray)
            i = i+1
            f1 = 0
            continue
    else:
        ret= False
        break
            
cv2.destroyAllWindows()
pdf = FPDF()
a = os.listdir("E://pdf")
for image in a:
    pdf.add_page()
    pdf.image("E://pdf//"+image)
pdf.output("E://my_file.pdf")
