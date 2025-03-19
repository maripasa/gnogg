import cv2
import pytesseract

def get_games(file, remove=None):

    known_names = set()

    if remove is not None:
        print("huh")

    cap = cv2.VideoCapture(file)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY_INV)
        
        text = pytesseract.image_to_string(thresh)

        lines = text.split('\n')

        for line in lines:
            line = line.strip()
            if line:
                known_names.add(line)
        print(known_names)

    cap.release()
    cv2.destroyAllWindows()

    print(known_names)
