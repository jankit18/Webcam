import cv2  # importing open-cv
from fpdf import FPDF  # importing FPDF from fpdf
import os  # importing os module used for interacting with operating system
url = 'http://192.168.1.3:8080/video'
cap = cv2.VideoCapture(url)
ret = True
f1 = 0
i = 0
PATH_TO_PICS = "./images"
PATH_TO_PDF = "./pdf"

try:
    os.mkdir(PATH_TO_PDF)
    os.mkdir(PATH_TO_PICS)
except OSError as error:
    pass
while ret:
    ret, frame = cap.read()
    if f1 == 0:
        print("press s to scan")
        f1 = f1+1

    cv2.namedWindow("camera feed", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("camera feed", 600, 600)
    cv2.imshow('camera feed', frame)

    k = cv2.waitKey(1)  # waits for input from the keyboard
    if k == ord('s'):
        cv2.destroyWindow("camera feed")
        cv2.namedWindow("scanned photo", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("scanned photo", 600, 600)
        cv2.imshow("scanned photo", frame)
        print("press u if unreadable")
        print("press b for black and white")
        k = cv2.waitKey(0)
        if k == ord('u'):
            cv2.destroyWindow('Scanned photo')
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            new = cv2.adaptiveThreshold(
                gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155, 1)

            cv2.imwrite(f"{PATH_TO_PICS}/scanned{i}.jpg", new)
            print(f"{PATH_TO_PICS}/scanned{i}.jpg")
            i = i+1
            print("press 's' to scan more document")
            print("press 'q' to quit")
            continue

        elif k == ord('b'):
            cv2.destroyWindow('Scanned photo')
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f"{PATH_TO_PICS}/scanned{i}.jpg", gray)
            print(f"{PATH_TO_PICS}/scanned{i}.jpg")
            i = i + 1
            print("press 's' to scan more document")
            print("press 'q' to quit")
            continue

    elif k == ord('q'):
        ret = False
        break

cv2.destroyAllWindows()
imagelist = [f for f in os.listdir(
    PATH_TO_PICS) if not os.path.isdir(os.path.join(PATH_TO_PICS, f))]
pdf = FPDF()
for image in imagelist:
    image = f"{PATH_TO_PICS}/"+image
    pdf.add_page()
    print(f"Added {image} into pdf")
    pdf.image(image)

pdf.output(f"{PATH_TO_PDF}/your_file.pdf", "F")
print("PDF created successfully")
