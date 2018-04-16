#coding:utf-8
'''
图像卷积
'''
def convd_2d(img,kernel):
    kernel_height = kernel.shape[0]
    kernel_width = kernel.shape[1]

    conv_height = img.shape[0] - kernel_height + 1
    conv_width = img.shape[1] - kernel_width + 1

    conv_img = np.zeros((conv_height,conv_width),dtype=np.uint8)

    for i in range(conv_height):
        for j in range(conv_width):
            conv_img[i][j] = wise_element_sum(img[i:i + kernel_height,j:j + kernel_width],kernel)

    return conv_img

def wise_element_sum(img,kernel):

    res = (img * kernel).sum()

    if res < 0:
        res = 0
    elif res > 255:
        res = 255
    return res