import cv2
import pytesseract

def get_games(file, remove):
    known_names = []

    if remove is not None:
        print("huh")

    cap = cv2.VideoCapture(file)

    fps = cap.get(cv2.CAP_PROP_FPS)
    interval_seconds = 0.1
    frame_interval = int(fps * interval_seconds)
    
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_count += 1

        if frame_count % frame_interval != 0:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY_INV)
        
        text = pytesseract.image_to_string(thresh)
        
        cv2.imshow("Frame", thresh)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()

            if not line:
                continue
            
            known_names.append(line)

        known_names = list(dict.fromkeys(known_names))
        print(len(known_names))

    cap.release()
    cv2.destroyAllWindows()

    print(sorted(known_names))
