import cv2
import numpy as np
import os

# 打开摄像头
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# 创建保存图像的目录，如果目录已存在则不会重复创建
save_dir = "processed_images"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

image_count = 0

while True:
    # 从摄像头读取一帧图像
    ret, frame = cap.read()
    if not ret:
        break

    # 将彩色图像转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 对灰度图像进行高斯模糊
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # 进行边缘检测
    edges = cv2.Canny(blurred, 100, 200)

    kernel = np.ones((5, 5), np.uint8)
    # 对边缘图像进行膨胀操作
    dilated = cv2.dilate(edges, kernel, iterations=1)
    # 进行闭运算，填充物体内部细小孔洞
    closed = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)

    # 寻找图像的轮廓
    contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 100:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        center_x, center_y = x + w // 2, y + h // 2
        # 设置绘制颜色为蓝色
        blue_color = (255, 0, 0)

        cv2.drawContours(frame, [contour], -1, blue_color, 2)
        cv2.drawMarker(frame, (center_x, center_y), blue_color, markerType=cv2.MARKER_CROSS, markerSize=10, thickness=2)

    # 显示处理后的图像
    cv2.imshow('Webcam', frame)

    # 等待按键按下，这里等待1毫秒
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        #保存图片
        save_path = os.path.join(save_dir, f"processed_image_{image_count}.jpg")
        cv2.imwrite(save_path, frame)
        print(f"已保存图像至 {save_path}")


# 释放摄像头资源
cap.release()
# 关闭所有创建的窗口
cv2.destroyAllWindows()