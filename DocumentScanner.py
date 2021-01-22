import cv2 #importing open-cv
from fpdf import FPDF #importing FPDF from fpdf
import os #importing os module used for interacting with operating system
url = "http://192.168.43.1:8080/video"
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
    k= cv2.waitKey(1) #waits for input from the keyboard
    if k==ord('s'):
        cv2.destroyWindow("camera feed")
        cv2.imshow("Scanned photo",frame)
        print("press u if its unreadable")
        print("press b to convert it to black and white form")
        k=cv2.waitKey(0)
        if  k== ord('u'):
            cv2.destroyWindow('Scanned photo')
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            new=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,155,1)
            cv2.imwrite("E://pdf//scanned%d.jpg"%i,new)
            i = i+1
            continue
        elif k==ord('b'):
            cv2.destroyWindow('Scanned photo')
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
            cv2.imwrite("E://pdf///scanned%d.jpg"%i,gray)
            i = i+1
            continue
    if k==ord('q'):
        ret= False
        break
            
cv2.destroyAllWindows()
imagelist = os.listdir("E://pdf")
pdf = FPDF()
for image in imagelist:
    image = "E://pdf//"+image
    pdf.add_page()
    pdf.image(image)
pdf.output("E://your_file.pdf", "F")
