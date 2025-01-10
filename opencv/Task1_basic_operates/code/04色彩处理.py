import cv2

# 读取原始图像
image = cv2.imread('all.jpg')

# 将彩色图像转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# 将灰度图像保存为新的文件
cv2.imwrite('gray_all.jpg', gray_image)

# 关闭所有窗口
cv2.destroyAllWindows()