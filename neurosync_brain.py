import cv2
import mediapipe as mp
import socket
import math
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

# --- CONFIGURATION ---
UDP_IP = "127.0.0.1" # Localhost (Same computer)
UDP_PORT = 5065      # Port to talk to Unity
AES_KEY = b'1234567890123456' # 16-byte Key (Must match Unity)

# --- SETUP MEDIA PIPE ---
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# --- SETUP UDP SOCKET ---
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# --- HELPER: ENCRYPTION (The Security Layer) ---
def encrypt_data(data_string):
    cipher = AES.new(AES_KEY, AES.MODE_ECB) # Using ECB for simplicity in demo
    encrypted_bytes = cipher.encrypt(pad(data_string.encode('utf-8'), AES.block_size))
    return base64.b64encode(encrypted_bytes).decode('utf-8')

# --- HELPER: CALCULATE DISTANCE ---
def get_distance(p1, p2):
    return math.hypot(p1.x - p2.x, p1.y - p2.y)

# --- MAIN LOOP ---
cap = cv2.VideoCapture(0)

print("NeuroSync AI Engine Started... Press 'q' to quit.")

while True:
    success, img = cap.read()
    if not success: break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    
    flex_value = 0.0 # 0 = Open, 100 = Closed
    fatigue_alert = False

    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_lms, mp_hands.HAND_CONNECTIONS)
            
            # Logic: Measure distance between Wrist (0) and Middle Finger Tip (12)
            wrist = hand_lms.landmark[0]
            tip = hand_lms.landmark[12]
            
            # Calculate distance (Normalized 0.0 to 1.0)
            dist = get_distance(wrist, tip)
            
            # Map distance to Flex Value (Adjust these thresholds based on your hand)
            # Example: Distance 0.3 is open, 0.1 is closed
            max_dist = 0.4
            min_dist = 0.1
            
            # Clamping and mapping
            flex_value = (max_dist - dist) / (max_dist - min_dist) * 100
            flex_value = max(0, min(100, flex_value))
            
            # SIMULATED AI FATIGUE LOGIC
            # If hand is shaking or moving erratically (Simulated here for demo)
            # In a real demo, you can toggle this with a keyboard key
            if cv2.waitKey(1) & 0xFF == ord('f'):
                fatigue_alert = True

    # --- PREPARE DATA ---
    data_packet = {
        "flex": int(flex_value),
        "fatigue": fatigue_alert
    }
    json_str = json.dumps(data_packet)
    
    # --- ENCRYPT & SEND ---
    encrypted_msg = encrypt_data(json_str)
    sock.sendto(str.encode(encrypted_msg), (UDP_IP, UDP_PORT))

    # --- DISPLAY ---
    cv2.putText(img, f"Flex: {int(flex_value)}%", (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    if fatigue_alert:
         cv2.putText(img, "FATIGUE DETECTED!", (10, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
         
    cv2.imshow("NeuroSync Vision", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()