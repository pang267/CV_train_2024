import cv2

# 读取原始图像
image = cv2.imread('all.jpg')

# 裁剪图像，获取指定区域
crop = image[185:375, 185:585]

# 将裁剪后的图像保存为新的文件，这里保存为'cropped_image.jpg'，可根据需求修改文件名及路径
cv2.imwrite('phone.jpg', crop)

# 关闭所有窗口，释放资源
cv2.destroyAllWindows()