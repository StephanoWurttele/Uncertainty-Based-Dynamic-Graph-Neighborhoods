import pydicom
from pydicom import dcmread
from pydicom.pixel_data_handlers.util import apply_voi_lut
import numpy as np
import matplotlib.pyplot as plt
import os
# Dicom in npy
# # url = "/content/drive/MyDrive/Colab Notebooks/images-test/tomografias1/1/patient11-19.dcm"
# url2 = "./Almenara/patient11-19.dcm" # https://drive.google.com/drive/u/1/folders/1qSgswvsiwJsSZJjh0r5gJFy7BoE7ahDy
path = "Almenara/AQUIJE_ZAPATA_VIOLETA 762239/2021-09-17 204101/IMG-0013" # https://drive.google.com/drive/u/1/folders/1svSRhd8VESelW2zA43uODAjCswlF2OcS
save_dir = "our_pancreas_ct/pancreas_npy_3d/test/IMG-0013/IMG-0013.npy"
save_dir_256 = "our_pancreas_ct/pancreas_npy_3d/test/IMG-0013/256cap/IMG-0013.npy"
# V1
counter = dict()
def read_dcm(url): # must transform to npy an entire folder!!
    i = 0
    arr_1=np.empty([219,512,512], dtype="int32")
    for filename in os.listdir(url):
        f = os.path.join(url,filename)
        print(f)
        ds = dcmread(f)
        arr_1[i] = ds.pixel_array
        i+=1
    # ds_1 = dcmread(url)
    # values = np.unique(ds_1.pixel_array, return_counts=True)
    # print("values are")
    # print(values)
    # for i in range(len(values[0])):
    #     counter[values[0][i]] = values[1][i]
    # print("----value counter")
    # print(counter)
    # print(ds_1)
    # print(ds_1.pixel_array.shape) #Pixel Data is https://dicom.innolitics.com/ciods/segmentation/image-pixel/7fe00010
    # print(np.amax(ds_1.pixel_array))
    # arr_1 = ds_1.pixel_array
    arr_1 = np.moveaxis(arr_1, 0, -1)
    print(arr_1.shape)
    np.save(save_dir, arr_1)
    return arr_1

def read_dcm_256(url): # must transform to npy an entire folder!!
    i = 0
    arr_1=np.empty([219,512,512], dtype="uint8")
    for filename in os.listdir(url):
        f = os.path.join(url,filename)
        print(f)
        ds = dcmread(f)
        arr_1[i] = ds.pixel_array
        i+=1
    # arr_1 = np.moveaxis(arr_1, 0, -1)
    print(arr_1.shape)

    values = np.unique(arr_1[0], return_counts=True)
    print("values are")
    print(values)
    
    np.save(save_dir_256, arr_1)
    return arr_1

# V2
def read_xray(path, voi_lut = False, fix_monochrome = True):
    # This might be the key https://www.kaggle.com/code/raddar/convert-dicom-to-np-array-the-correct-way

    dicom = pydicom.read_file(path)
    print(dicom.pixel_array.shape)
    print(dicom.PhotometricInterpretation)
    # VOI LUT (if available by DICOM device) is used to transform raw DICOM data to "human-friendly" view
    if voi_lut:
        data = apply_voi_lut(dicom.pixel_array, dicom)
    else:
        data = dicom.pixel_array
    # print(data == data2.pixel_array)
    # depending on this value, X-ray may look inverted - fix that:
    if fix_monochrome and dicom.PhotometricInterpretation == "MONOCHROME1":
        print("fixing monochrome")
        data = np.amax(data) - data
        
    data = data - np.min(data)
    data = data / np.max(data)
    data = (data * 255).astype(np.uint8)
        
    return data

# img = read_xray(path)
img = read_dcm_256(path)
# plt.figure(figsize = (12,12))
# plt.imshow(img[0], 'gray')
# plt.show()
# print("done")