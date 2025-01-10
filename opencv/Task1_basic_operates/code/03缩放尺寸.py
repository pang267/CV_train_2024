import cv2


# 读取原始图像
image = cv2.imread('all.jpg')

# 裁剪图像，获取指定区域
crop = image[185:375, 185:585]

# 获取原始图像和裁剪图像的尺寸信息
original_height, original_width, _ = image.shape
crop_height, crop_width, _ = crop.shape

# 计算高度缩放比例
scale_height = original_height/crop_height
# 根据缩放比例计算缩放后的宽度（保持纵横比）
new_width = int(crop_width * scale_height)

# 对裁剪后的图像进行缩放
resized_crop = cv2.resize(crop, (new_width, original_height))

# 显示缩放后的裁剪图像（可选）
cv2.imshow("phone_Resized", resized_crop)
cv2.waitKey(0)

# 将缩放后的裁剪图像保存为新的文件（可选）
cv2.imwrite('.phone_Resized.jpg', resized_crop)

# 关闭所有窗口，释放资源
cv2.destroyAllWindows()