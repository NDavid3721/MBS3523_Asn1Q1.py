import cv2

cap = cv2.VideoCapture(0)

cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('Faces', cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    font = cv2.FONT_HERSHEY_SIMPLEX
    text = "MBS3523 Assignment 1 - Q2 Name: Ngan Wai Tak"
    thickness = 2
    color = (255, 0, 0)
    text_size, _ = cv2.getTextSize(text, font, 1, thickness)
    width, height = text_size
    x = int((frame.shape[1] - width) / 2)
    y = int(height + 10)
    cv2.putText(frame, text, (x, y), font, 1, color, thickness, cv2.LINE_AA)

    cv2.imshow('Original', frame)
    cv2.imshow('Faces', gray)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

