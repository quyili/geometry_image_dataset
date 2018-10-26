from skimage import draw
import numpy as np
from matplotlib import pyplot as plt
import random
import os

num=1000
max_size=1024
min_size=256

i=0
while (i<num):
    img_h = random.randint(min_size,max_size)
    img_w = random.randint(min_size,max_size)
    img_w = random.randint(min_size, max_size)
    r=random.randint(32,int(min(img_h,img_w)/4))
    center_x=random.randint(r,img_w-r)
    center_y = random.randint(r,img_h-r)
    img = np.zeros((img_h,img_w,3),np.uint8)
    img_color_r= random.randint(1,255)
    img_color_g = random.randint(1, 255)
    img_color_b = random.randint(1, 255)
    rr, cc = draw.circle(center_y,center_x, r)
    draw.set_color(img, [rr, cc], [img_color_r,img_color_g,img_color_b])
    check_path = "data/unfixed_size_geometry_data/src_data/1-circle/"
    if os.path.exists(check_path) == False: os.makedirs(check_path)
    plt.imsave(check_path+"circle_"+str(i)+".jpg",img)
    print(check_path+"circle_"+str(i)+".jpg")
    i = i + 1

i=0
while (i<num):
    img_h = random.randint(min_size, max_size)
    img_w = random.randint(min_size, max_size)
    a = random.randint(32, int(min(img_h, img_w) / 4))
    b = random.randint(32, int(min(img_h, img_w) / 4))
    if abs(a-b)<=16 or  abs(a-b)>=64:
        continue
    center_x = random.randint(b, img_w - b)
    center_y = random.randint(a, img_h - a)
    img = np.zeros((img_h, img_w, 3), np.uint8)
    img_color_r = random.randint(1, 255)
    img_color_g = random.randint(1, 255)
    img_color_b = random.randint(1, 255)
    rr, cc = draw.ellipse(center_y, center_x, a,b)
    draw.set_color(img, [rr, cc], [img_color_r, img_color_g, img_color_b])
    check_path = "data/unfixed_size_geometry_data/src_data/2-ellipse/"
    if os.path.exists(check_path) == False: os.makedirs(check_path)
    plt.imsave(check_path+"ellipse_"+str(i)+".jpg",img)
    print(check_path+"ellipse_"+str(i)+".jpg")
    i = i + 1

i=0
while (i<num):
    img_h = random.randint(min_size, max_size)
    img_w = random.randint(min_size, max_size)
    l = random.randint(32, int(min(img_h, img_w)*3 / 8))
    center_x = random.randint(l, img_w - l)
    center_y = random.randint(l, img_h - l)
    img = np.zeros((img_h, img_w, 3), np.uint8)
    img_color_r = random.randint(1, 255)
    img_color_g = random.randint(1, 255)
    img_color_b = random.randint(1, 255)
    Y = np.array([center_y - l, center_y - l, center_y + l, center_y + l])
    X = np.array([center_x - l, center_x + l, center_x + l, center_x - l])
    rr, cc = draw.polygon(Y, X)
    draw.set_color(img, [rr, cc], [img_color_r, img_color_g, img_color_b])
    check_path = "data/unfixed_size_geometry_data/src_data/3-square/"
    if os.path.exists(check_path) == False: os.makedirs(check_path)
    plt.imsave(check_path+"square_"+str(i)+".jpg",img)
    print(check_path+"square_"+str(i)+".jpg")
    i = i + 1

i=0
while (i<num):
    img_h = random.randint(min_size, max_size)
    img_w = random.randint(min_size, max_size)
    a = random.randint(32, int(min(img_h, img_w)*3 / 8))
    b = random.randint(32, int(min(img_h, img_w)*3 / 8))
    if abs(a - b) <= 24 or abs(a - b) >= 192:
        continue
    center_x = random.randint(b, img_w - b)
    center_y = random.randint(a, img_h - a)
    img = np.zeros((img_h, img_w, 3), np.uint8)
    img_color_r = random.randint(1, 255)
    img_color_g = random.randint(1, 255)
    img_color_b = random.randint(1, 255)
    Y = np.array([center_y - a, center_y - a, center_y + a, center_y + a])
    X = np.array([center_x - b, center_x + b, center_x + b, center_x - b])
    rr, cc = draw.polygon(Y, X)
    draw.set_color(img, [rr, cc], [img_color_r, img_color_g, img_color_b])
    # plt.imshow(img,'brg')
    # plt.show()
    check_path = "data/unfixed_size_geometry_data/src_data/4-rectangle/"
    if os.path.exists(check_path) == False: os.makedirs(check_path)
    plt.imsave(check_path+"rectangle_"+str(i)+".jpg",img)
    print(check_path+"rectangle_"+str(i)+".jpg")
    i = i + 1

i=0
while (i<num):
    img_h = min_size
    img_w = min_size
    r=random.randint(32,int(min(img_h,img_w)/4))
    center_x=random.randint(r,img_w-r)
    center_y = random.randint(r,img_h-r)
    img = np.zeros((img_h,img_w,3),np.uint8)
    img_color_r= random.randint(1,255)
    img_color_g = random.randint(1, 255)
    img_color_b = random.randint(1, 255)
    rr, cc = draw.circle(center_y,center_x, r)
    draw.set_color(img, [rr, cc], [img_color_r,img_color_g,img_color_b])
    check_path = "data/fixed_size_geometry_data/src_data/1-circle/"
    if os.path.exists(check_path) == False: os.makedirs(check_path)
    plt.imsave(check_path+"circle_"+str(i)+".jpg",img)
    print(check_path+"circle_"+str(i)+".jpg")
    i = i + 1

i=0
while (i<num):
    img_h = min_size
    img_w = min_size
    a = random.randint(32, int(min(img_h, img_w) / 4))
    b = random.randint(32, int(min(img_h, img_w) / 4))
    if abs(a-b)<=16 or  abs(a-b)>=64:
        continue
    center_x = random.randint(b, img_w - b)
    center_y = random.randint(a, img_h - a)
    img = np.zeros((img_h, img_w, 3), np.uint8)
    img_color_r = random.randint(1, 255)
    img_color_g = random.randint(1, 255)
    img_color_b = random.randint(1, 255)
    rr, cc = draw.ellipse(center_y, center_x, a,b)
    draw.set_color(img, [rr, cc], [img_color_r, img_color_g, img_color_b])
    check_path = "data/fixed_size_geometry_data/src_data/2-ellipse/"
    if os.path.exists(check_path) == False: os.makedirs(check_path)
    plt.imsave(check_path+"ellipse_"+str(i)+".jpg",img)
    print(check_path+"ellipse_"+str(i)+".jpg")
    i = i + 1

i=0
while (i<num):
    img_h = min_size
    img_w = min_size
    l = random.randint(32, int(min(img_h, img_w)*3 / 8))
    center_x = random.randint(l, img_w - l)
    center_y = random.randint(l, img_h - l)
    img = np.zeros((img_h, img_w, 3), np.uint8)
    img_color_r = random.randint(1, 255)
    img_color_g = random.randint(1, 255)
    img_color_b = random.randint(1, 255)
    Y = np.array([center_y - l, center_y - l, center_y + l, center_y + l])
    X = np.array([center_x - l, center_x + l, center_x + l, center_x - l])
    rr, cc = draw.polygon(Y, X)
    draw.set_color(img, [rr, cc], [img_color_r, img_color_g, img_color_b])
    check_path = "data/fixed_size_geometry_data/src_data/3-square/"
    if os.path.exists(check_path) == False: os.makedirs(check_path)
    plt.imsave(check_path+"square_"+str(i)+".jpg",img)
    print(check_path+"square_"+str(i)+".jpg")
    i = i + 1

i=0
while (i<num):
    img_h = min_size
    img_w = min_size
    a = random.randint(32, int(min(img_h, img_w)*3 / 8))
    b = random.randint(32, int(min(img_h, img_w)*3 / 8))
    if abs(a - b) <= 24 or abs(a - b) >= 192:
        continue
    center_x = random.randint(b, img_w - b)
    center_y = random.randint(a, img_h - a)
    img = np.zeros((img_h, img_w, 3), np.uint8)
    img_color_r = random.randint(1, 255)
    img_color_g = random.randint(1, 255)
    img_color_b = random.randint(1, 255)
    Y = np.array([center_y - a, center_y - a, center_y + a, center_y + a])
    X = np.array([center_x - b, center_x + b, center_x + b, center_x - b])
    rr, cc = draw.polygon(Y, X)
    draw.set_color(img, [rr, cc], [img_color_r, img_color_g, img_color_b])
    check_path = "data/fixed_size_geometry_data/src_data/4-ectangle/"
    if os.path.exists(check_path) == False: os.makedirs(check_path)
    plt.imsave(check_path+"rectangle_"+str(i)+".jpg",img)
    print(check_path+"rectangle_"+str(i)+".jpg")
    i = i + 1