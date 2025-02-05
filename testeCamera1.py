import cv2

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("N abriu a camera")
    exit()

while True:
    
    ret, frame = cam.read()

    if not ret:
        print("N leu o frame")
        break

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()