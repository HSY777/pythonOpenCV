import cv2

capture = cv2.VideoCapture("video/dog.mp4")

while cv2.waitKey(33) < 0:
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.set(cv2.CPA_PROP_POS_FRAMES, 0)

    
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

capture.release()
cv2.destroyAllWindows()


# 비디오 속성 반환 메서드(capture.get)로 비디오의 속성을 반환합니다.
