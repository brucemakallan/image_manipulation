# from os import listdir, rename
# mypath = r'C:/Users/PingucG/PycharmProjects/Havy Tours RES/gallery/zanzibar/'
# i = 1
# for file in listdir(mypath):
#     rename(mypath + str(file), mypath + str(i) + '.jpg')  # rename all
#     i += 1


# from PIL import Image
# from resizeimage import resizeimage
# from os import listdir
#
#
# mypath = r'C:/Users/PingucG/PycharmProjects/Havy Tours RES/gallery/zipteam2/'
# for file in listdir(mypath):
#     with open(mypath + str(file), 'r+b') as f:
#         with Image.open(f) as image:
#             print('Resizing: ' + str(file) + ' ... ')
#             cover = resizeimage.resize_cover(image, [900, 600], validate=False)
#             cover.save(mypath + str(file), image.format)


# write paths to file
# from os import listdir
#
#
# gallery_name = 'zipteam2/'
# online_path = r'http://iviidev.info/downloads/havytours/gallery/' + gallery_name
# gallery_location = r'C:/Users/PingucG/PycharmProjects/Havy Tours RES/gallery/'
# local_path = gallery_location + gallery_name
#
# f = open(gallery_location + 'paths.txt', "a")  # a for append, w for overwrite
# for file in listdir(local_path):
#     if str(file).endswith('.jpg'):
#         f.write(online_path + str(file) + '\n')




# Resize images
from PIL import Image
from resizeimage import resizeimage
from os import listdir, path, rename


def is_image(file):
    if file.endswith('jpg') or file.endswith('JPG') or file.endswith('png') or file.endswith('PNG'):
        return True
    return False


def resize(path_passed):
    WIDTH_IN_PX = 900
    counter = 1
    for entry in listdir(path_passed):
        if path.isdir(path_passed + entry):
            print('\n\n-----------------------------\nDIRECTORY: ' + str(entry))
            resize(path_passed + entry + '/')
        elif path.isfile(path_passed + entry) and is_image(entry):
            with open(path_passed + str(entry), 'r+b') as f:
                with Image.open(f) as image:
                    width, height = image.size
                    if width > WIDTH_IN_PX:
                        print('\nResizing: ' + str(path_passed + entry) + '  ' + str(width) + 'X' + str(height))
                        new_height = (WIDTH_IN_PX * height) / width
                        print('h = ' + str(new_height))
                        cover = resizeimage.resize_cover(image, [WIDTH_IN_PX, int(new_height)], validate=False)
                        cover.save(path_passed + str(entry), image.format)
                        counter += 1
                    else:
                        print('\nNOT Resizing: ' + str(entry) + ' ' + str(width) + 'X' + str(height))
        else:
            print('\n**** Other File: ' + str(entry))

my_path = r'/Users/brucemakallan/Downloads/USF/firstInvitationalGala/'
resize(my_path)






# move all. NOT WORKING
# from os import listdir, path, rename
#
#
# def is_image(file):
#     if file.endswith('jpg') or file.endswith('JPG'):
#         return True
#     return False
#
#
# def move(path_passed):
#     i = 0
#     for entry in listdir(path_passed):
#         if path.isdir(path_passed + entry):
#             print('\n\n----------------\nDIRECTORY: ' + str(entry))
#             move(path_passed + entry + '/')
#         elif path.isfile(path_passed + entry) and is_image(entry):
#             while path.isfile(r'G:/images_temp/' + str(i) + '.jpg'):
#                 i += 1
#             rename(path_passed + str(entry), r'G:/images_temp/' + str(i) + '.jpg')
#             i += 1
#         else:
#             print('\n**** Other File: ' + str(entry))
#
#
# my_path = r'G:/kODDAK/'
# move(my_path)
