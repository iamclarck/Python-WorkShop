import cv2
img = cv2.imread('eminem.jpg',0) # 0 means black and white, 1 means colorful, -1 means colorful with transperancy

print(type(img))
print(img)
height = img.shape[0]
width = img.shape[1]
print('Height:', height)
print('Width:', width)

resized_height = height//2
resized_width = width//2

resized_images = cv2.resize(img,(resized_width,resized_height))

cv2.imwrite('mashal eminem.jpg', resized_images)

cv2.imshow('Marshal Mathers', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# print(img.shape)
