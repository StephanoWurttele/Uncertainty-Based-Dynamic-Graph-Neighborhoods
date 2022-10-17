import numpy as np
import SimpleITK as sitk

outlined_segment = "./Almenara/Pred_npys/fullvalues/results-outline/119.npy"
save_outlined_segment = "./Almenara/Pred_npys/fullvalues/results-outline-img/119.png"

inp = outlined_segment
out = save_outlined_segment

data = np.load(inp)
print(data)
print("amax", np.amax(data))
ints = 32

castFilter = sitk.CastImageFilter()
if (ints == 16):
    castFilter.SetOutputPixelType(sitk.sitkInt16)
elif(ints == 32):
    castFilter.SetOutputPixelType(sitk.sitkInt32)

img = sitk.GetImageFromArray(data)
data = castFilter.Execute(img)
# print(data.GetDimension())
# print(data.GetDepth())
# print(data.GetNumberOfPixels ())
# print(data[0][0])

sitk.WriteImage(data, f'./Almenara/Pred_npys/fullvalues/results_in_dicom/test1_{ints}.dcm')
print("dicom written")