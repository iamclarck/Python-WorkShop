import cv2

import glob
all_images = glob.glob('*.jpg')
# print(all_images)
# images = ['galaxy.jpg','Lighthouse.jpg','person4.jpg','news.jpg']

for image in all_images:
    python_images = cv2.imread(image, 0)

    resized_height = python_images.shape[0]//2
    resized_width = python_images.shape[1]//2

    resized_images = cv2.resize(python_images, (resized_width, resized_height))
    name = "new"  + image
    cv2.imwrite(name, resized_images)

    # cv2.imshow('Marshal Mathers', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # # print(img.shape)
