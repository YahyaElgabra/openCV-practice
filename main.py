import cv2
from pprint import pprint

# img = cv2.imread('./mario.jpeg', cv2.IMREAD_UNCHANGED)
 
# dimensions = img.shape
 
# height = img.shape[0]
# width = img.shape[1]
# channels = img.shape[2]
 
# print('Image Dimension    : ',dimensions)
# print('Image Height       : ',height)
# print('Image Width        : ',width)
# print('Number of Channels : ',channels)



# print("which image do you want to resize?")
# img = cv2.imread(input(), cv2.IMREAD_UNCHANGED)
# print("what do you want its height to be?")
# height = int(input())
# print("what do you want its width to be?")
# width = int(input())

# resized = cv2.resize(img, [width, height])

# cv2.imwrite('./resized.png', resized)



# print("which image do you want to process?")
# img = cv2.imread(input(), cv2.IMREAD_UNCHANGED)
# color = ''
# while color not in ['R', 'G', 'B']:
#     print("Which color channel do you want to view the image in? (R/G/B)")
#     color = input()

# # for j in range(len(img)):
# #     for i in range(len(img[j])):
# #         if color == 'B':
# #             img[j][i] = [img[j][i][0], 0, 0, img[j][i][3]]
# #         elif color == 'G':
# #             img[j][i] = [0, img[j][i][1], 0, img[j][i][3]]
# #         else:
# #             img[j][i] = [0, 0, img[j][i][2], img[j][i][3]]

# if color == 'B':
#     img[:, :, 1] = 0
#     img[:, :, 2] = 0

# elif color == 'G':
#     img[:, :, 0] = 0
#     img[:, :, 2] = 0

# elif color == 'R':
#     img[:, :, 1] = 0
#     img[:, :, 0] = 0

# cv2.imwrite('./filtered.png', img)



print("which image do you want to pixelate?")
img = cv2.imread(input(), cv2.IMREAD_UNCHANGED)

width = 32
height = 32
small = cv2.resize(img, [width, height], interpolation = cv2.INTER_AREA)
large = cv2.resize(small, [width * 23, height * 23], interpolation = cv2.INTER_AREA)
cv2.imwrite('./pixelated2.png', large)