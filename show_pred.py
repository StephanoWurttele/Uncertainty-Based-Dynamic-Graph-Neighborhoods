from PIL import Image
import numpy as np

input = "./our_pancreas_ct/pancreas_npy_3d/test/IMG-0013/IMG-0013.npy"
input_jpg = './Almenara/Pred_npys/input-aquije-13-CT.png'

input_generate_pred = "Almenara\Pred_npys\ejemplo0013-aquije.npy"
input_generate_jpg_pred = 'Almenara\Pred_npys\ejemplo0013-aquije.png'

bw_to_segment = "./Almenara/Pred_npys/results/119.npy"
save_color_segmentation = "./Almenara/Pred_npys/119.png"

outlined_segment = "./Almenara/Pred_npys/results-outline/119.npy"
save_outlined_segment = "./Almenara/Pred_npys/results-outline-img/119.png"

data = np.load(outlined_segment)
if(len(data.shape) == 4):
    img = Image.fromarray((data[0][120] * 255).astype('uint8') , 'L')
elif(len(data.shape) == 3):
    data = np.moveaxis(data, 0, -1)
    data = np.moveaxis(data, 0, -1)
    img = Image.fromarray((data[120] * 255).astype('uint8') , 'L')
else:
    img = Image.fromarray((data * 255).astype('uint8') , 'L')
img.save(save_outlined_segment)
img.show()