import cv2
import mediapipe as mp
import time
import pyautogui



# Video capture settings
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Hand definitions
mpHand = mp.solutions.hands
hands = mpHand.Hands()
mpDraw = mp.solutions.drawing_utils

# Actually the program calculates distance between two finger, we must give which fingers
calculated_distances = [[5, 4], [6, 8], [10, 12], [14, 16], [18, 20]]

# Variables for countdown
start_time = None
message = ""
display_time = None
disable_tracking_time = None

while cap.isOpened():
    success, img = cap.read()

    if success:
        # It's optional, we used mirror effect
        img = cv2.flip(img, 1)

        # BGR to RGB Color conversion
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Process hands to count
        results = hands.process(img_rgb)

        # Finger counter
        counter = 0

        # When record every fingers, this condition will use
        if results.multi_hand_landmarks and (disable_tracking_time is None or time.time() - disable_tracking_time > 5):

            # Motions array for record positions of all fingers
            motions = []

            for handLms in results.multi_hand_landmarks:
                # Draw 20 landmarks
                mpDraw.draw_landmarks(img, handLms, mpHand.HAND_CONNECTIONS)

                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    # Convert ratios to reel positions
                    cx, cy = int(lm.x * w), int(lm.y * h)

                    # If it's head finger, calculate avg. (exceptional situation)
                    if id == 4:
                        cy = ((cy + motions[3][2]) / 2) + cap.get(4) / 30

                    # Add finger landmark position [id, coordinat x, coordinat y]
                    motions.append([id, cx, cy])

            for item in calculated_distances:
                downFingerPosY = motions[item[0]][2]
                upperFingerPosY = motions[item[1]][2]
                # If down landmark of finger y position bigger than upper:
                # The finger increases counter
                isFingerOpen = downFingerPosY > upperFingerPosY
                counter += 1 if isFingerOpen else 0

        # Check if a countdown should start
        if start_time is None and counter > 0:
            start_time = time.time()
            if counter == 1:
                pyautogui.click()
                print("Photo Done")
                disable_tracking_time = time.time()

            elif counter == 2:
                pyautogui.click()
                print("Photo Done")
                disable_tracking_time = time.time()

            elif counter == 3:
                pyautogui.click()
                print("Photo Done")
                disable_tracking_time = time.time()


        elif start_time is not None and time.time() - start_time >= 2:
            # Display the message on the OpenCV window
            display_time = time.time()
            start_time = None

        # Display the message for 2 seconds
        if display_time is not None and time.time() - display_time <= 2:
            cv2.putText(img, message, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        else:
            display_time = None
            message = ""

        # Draw rectangle and put text for counting operation
        cv2.rectangle(img, (0, 0), (200, 50), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, str(counter), (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
        # Show all of these
        cv2.imshow("Capture", img)
        cv2.waitKey(1)
