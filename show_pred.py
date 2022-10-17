from PIL import Image
import numpy as np

input = "./our_pancreas_ct/pancreas_npy_3d/test/IMG-0013/IMG-0013.npy"
input_jpg = './Almenara/Pred_npys/input-aquije-13-CT.png'

input_generate_pred = "Almenara\Pred_npys\ejemplo0013-aquije.npy"
input_generate_png_pred = 'Almenara\Pred_npys\ejemplo0013-aquije.png'

bw_to_segment = "./Almenara/Pred_npys/results/119.npy"
save_color_segmentation = "./Almenara/Pred_npys/119.png"

outlined_segment = "./Almenara/Pred_npys/results-outline/119.npy"
save_outlined_segment = "./Almenara/Pred_npys/results-outline-img/119.png"
# Fullvalues
input_generate_pred_fullvalues = "Almenara/Pred_npys/fullvalues/ejemplo0013-aquije.npy"
input_generate_png_pred_fullvalues = 'Almenara/Pred_npys/fullvalues/ejemplo0013-aquije.png'

bw_to_segment_fullvalues = "./Almenara/Pred_npys/fullvalues/results/119.npy"
save_color_segmentation_fullvalues = "./Almenara/Pred_npys/fullvalues/119-segmentation-result.png"

outlined_segment_fullvalues = "./Almenara/Pred_npys/fullvalues/results-outline/119.npy"
save_outlined_segment_fullvalues = "./Almenara/Pred_npys/fullvalues/results-outline-img/119.png"

inp = input_generate_pred_fullvalues
out = input_generate_png_pred_fullvalues

data = np.load(inp)
if(len(data.shape) == 4):
    print("shape 4")
    img = Image.fromarray((data[0][120] * 255).astype('uint8') , 'L')
elif(len(data.shape) == 3):
    print("shape 3")
    data = np.moveaxis(data, 0, -1)
    data = np.moveaxis(data, 0, -1)
    img = Image.fromarray((data[120] * 255).astype('uint8') , 'L')
else:
    print("shape not 3 or 4")
    img = Image.fromarray((data * 255).astype('uint8') , 'L')
    # img = Image.fromarray((data*255).astype('int32'))
    # print(data.shape)
img.save(out)
img.show()