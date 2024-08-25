# import streamlit as st
# import cv2
# from ultralytics import YOLOv10

# model_class_names = {
#     0: 'Anger',
#     1: 'Contempt',
#     2: 'Disgust',
#     3: 'Fear',
#     4: 'Happy',
#     5: 'Neutral',
#     6: 'Sad',
#     7: 'Surprise'
# }

# def draw_boxes(frame, boxes, names, color):
#     for box, name in zip(boxes, names):
#         x1, y1, x2, y2 = box[:4]

#         center_x = (x1 + x2) / 2
#         center_y = (y1 + y2) / 2
#         width = x2 - x1
#         height = y2 - y1
        
#         new_width = width / 2
#         new_height = height / 2

#         x1_new = center_x - new_width / 2
#         x2_new = center_x + new_width / 2
#         y1_new = center_y - new_height / 2
#         y2_new = center_y + new_height / 2

#         x1_new, x2_new = max(0, x1_new), min(frame.shape[1], x2_new)
#         y1_new, y2_new = max(0, y1_new), min(frame.shape[0], y2_new)

#         conf = box[4] if len(box) > 4 else 1.0
#         frame = cv2.rectangle(frame, (int(x1_new), int(y1_new)), (int(x2_new), int(y2_new)), color, 3)
#         label = f"{name} {conf:.2f}"
#         frame = cv2.putText(frame, label, (int(x1_new), int(y1_new) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)
    
#     return frame


# def crop_center_square(frame):
#     height, width = frame.shape[:2]
#     min_dim = min(height, width)
    
#     center_x, center_y = width // 2, height // 2
#     half_dim = min_dim // 2

#     x1 = center_x - half_dim
#     x2 = center_x + half_dim
#     y1 = center_y - half_dim
#     y2 = center_y + half_dim

#     x1, x2 = max(0, x1), min(width, x2)
#     y1, y2 = max(0, y1), min(height, y2)

#     cropped_frame = frame[y1:y2, x1:x2]
#     return cropped_frame

# def main():
#     st.title(":orange[Back To Hometown DEMO]")
#     st.markdown(':blue[ทดสอบ]:green[ระบบตรวจจับ]:red[อารมณ์]:violet[จาก]:orange[ใบหน้าผู้ใช้]')
#     st.caption("Powered by YOLOv10")

#     model = YOLOv10('best.onnx', task='detect')

#     names_dict = model_class_names

#     start_button = st.button("Activate camera")
#     frame_placeholder = st.empty()
    
#     if start_button:
#         cap = st.camera_input()

#         if not cap.isOpened():
#             st.error("Could not open video capture.")
#             return

#         while True:
#             ret, frame = cap.read()
#             if not ret:
#                 st.write("Video Capture Ended")
#                 break

#             frame = crop_center_square(frame)

#             results = model(frame, imgsz=96, conf=0.50, iou=0.9)
            
#             boxes = results[0].boxes.xyxy.cpu().numpy()
#             scores = results[0].boxes.conf.cpu().numpy()
#             classes = results[0].boxes.cls.cpu().numpy()

#             names = [names_dict.get(int(cls), 'Unknown') for cls in classes]

#             color = (0, 0, 255)
#             annotated_frame = draw_boxes(frame, boxes, names, color)

#             annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
#             frame_placeholder.image(annotated_frame, channels="RGB")

#             if not start_button:
#                 break

#         cap.release()
#         cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()

import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLOv10

model_class_names = {
    0: 'Anger',
    1: 'Contempt',
    2: 'Disgust',
    3: 'Fear',
    4: 'Happy',
    5: 'Neutral',
    6: 'Sad',
    7: 'Surprise'
}

def draw_boxes(frame, boxes, names, color):
    for box, name in zip(boxes, names):
        x1, y1, x2, y2 = box[:4]

        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        width = x2 - x1
        height = y2 - y1
        
        new_width = width / 2
        new_height = height / 2

        x1_new = center_x - new_width / 2
        x2_new = center_x + new_width / 2
        y1_new = center_y - new_height / 2
        y2_new = center_y + new_height / 2

        x1_new, x2_new = max(0, x1_new), min(frame.shape[1], x2_new)
        y1_new, y2_new = max(0, y1_new), min(frame.shape[0], y2_new)

        conf = box[4] if len(box) > 4 else 1.0
        frame = cv2.rectangle(frame, (int(x1_new), int(y1_new)), (int(x2_new), int(y2_new)), color, 3)
        label = f"{name} {conf:.2f}"
        frame = cv2.putText(frame, label, (int(x1_new), int(y1_new) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)
    
    return frame


def crop_center_square(frame):
    height, width = frame.shape[:2]
    min_dim = min(height, width)
    
    center_x, center_y = width // 2, height // 2
    half_dim = min_dim // 2

    x1 = center_x - half_dim
    x2 = center_x + half_dim
    y1 = center_y - half_dim
    y2 = center_y + half_dim

    x1, x2 = max(0, x1), min(width, x2)
    y1, y2 = max(0, y1), min(height, y2)

    cropped_frame = frame[y1:y2, x1:x2]
    return cropped_frame

def main():
    st.title(":orange[Back To Hometown DEMO]")
    st.markdown(':blue[ทดสอบ]:green[ระบบตรวจจับ]:red[อารมณ์]:violet[จาก]:orange[ใบหน้าผู้ใช้]')
    st.caption("Powered by YOLOv10")

    model = YOLOv10('best.onnx', task='detect')

    names_dict = model_class_names

    img_file_buffer = st.camera_input("Take a picture")

    with st.container() as frame_container:
        if img_file_buffer is not None:

            bytes_data = img_file_buffer.getvalue()
            cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
            
            frame = crop_center_square(cv2_img)

            results = model(frame, imgsz=96, conf=0.50, iou=0.9)
            
            boxes = results[0].boxes.xyxy.cpu().numpy()
            scores = results[0].boxes.conf.cpu().numpy()
            classes = results[0].boxes.cls.cpu().numpy()

            names = [names_dict.get(int(cls), 'Unknown') for cls in classes]

            color = (0, 0, 255)
            annotated_frame = draw_boxes(frame, boxes, names, color)

            annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
            
            st.markdown('Processed image')
            st.image(annotated_frame, channels="RGB", width=200)

if __name__ == "__main__":
    main(