import cv2
import numpy as np
import cx_Oracle as ora
import datetime

# 현재 시간을 가져와서 포맷팅
current_time = datetime.datetime.now()
formatted_time = current_time.strftime('%Y-%m-%d %H:%M')

# Oracle 데이터베이스에 연결하기 위한 정보
dsn = ora.makedsn(host='localhost', port=1521, service_name='xe')
user = 'hr'
password = 'hr'

# 데이터베이스 연결
connection = ora.connect(user=user, password=password, dsn=dsn)

# 커서 생성
cursor = connection.cursor()

# YOLO 얼굴 탐지 모델 파일 경로
YOLO_CFG = "D:\\Project\\face.cfg"
YOLO_WEIGHTS = "D:\\Project\\face.weights"

# YOLO 얼굴 탐지 모델 불러오기
net = cv2.dnn.readNet(YOLO_WEIGHTS, YOLO_CFG)

# Get the names of the output layers
output_layers_names = net.getUnconnectedOutLayersNames()

# 나이 예측 모델 파일 경로
AGE_MODEL = 'D:\\Project\\weights\\deploy_age.prototxt'
AGE_PROTO = 'D:\\Project\\weights\\age_net.caffemodel'

# 나이 예측 모델 불러오기
age_model = cv2.dnn.readNet(AGE_PROTO, AGE_MODEL)

# 성별 예측 모델 파일 경로
GENDER_MODEL = 'D:\\Project\\weights\\deploy_gender.prototxt'
GENDER_PROTO = 'D:\\Project\\weights\\gender_net.caffemodel'

# 성별 예측 모델 불러오기
gender_model = cv2.dnn.readNet(GENDER_PROTO, GENDER_MODEL)

# 나이 구간 목록
age_list = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(21-25)', '(25-32)', '(33-37)', '(38-43)', '(48-53)', '(60-100)']

# 성별 클래스 목록
gender_list = ['Male', 'Female']

# 프레임의 너비와 높이 초기화
frame_width = 1280
frame_height = 720

# Initialize the webcam (0 indicates the default camera)
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('D:\\Project\\in.avi')

# Initialize a dictionary to store information about detected faces
detected_faces = {}
face_id = 0

# Load the Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Initialize a dictionary for the current frame's faces
    frame_faces = {}

    for (x, y, w, h) in faces:
        # Crop the face from the frame
        face = frame[y:y + h, x:x + w]
        frame_faces[(x, y, w, h)] = face  # Store face and its location

    # Update the dictionary of detected faces for the current frame
    detected_faces = frame_faces

    # Perform age and gender prediction and draw bounding boxes for each detected face
    for (x, y, w, h), face in detected_faces.items():
        # Ensure that the face image is not empty
        if face.size == 0:
            continue

        # Preprocess the face for age and gender prediction
        face_blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746), swapRB=False)

        # Predict age
        age_model.setInput(face_blob)
        age_pred = age_model.forward()
        age = age_list[np.argmax(age_pred)]

        # Predict gender
        gender_model.setInput(face_blob)
        gender_pred = gender_model.forward()
        gender = gender_list[np.argmax(gender_pred)]

        # Draw bounding box around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Adjust the text size and display age, gender, and face ID on the frame
        label = f'Face ID: {face_id}, Gender: {gender}, Age: {age}'
        font_scale = 0.5  # Adjust this value to change text size
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, label, (x, y - 10), font, font_scale, (0, 255, 0), 1, cv2.LINE_AA)

        # Check if a face is already in the dictionary
        found = False
        for (id, f) in detected_faces.items():
            if np.array_equal(face, f):
                found = True
                break

        # If it's a new face, add it to the dictionary with a unique ID
        if not found:
            detected_faces[(x, y, w, h)] = face
            face_id += 1

    # Display the frame with detections
    cv2.imshow("Webcam Feed", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()