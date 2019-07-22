import cv2

filepath = r'C:\Users\Wargon\Pictures\Saved Pictures\Leaf.jpg'
# \u表示其后是unicode编码
# 不支持中文路径
img = cv2.imread(filepath)
cv2.namedWindow('Image')
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
