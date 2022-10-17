import cv2

outlined_segment_path = "./Almenara/Pred_npys/results-outline-img/119.png"
colored_segment = cv2.imread(outlined_segment_path)

def color_border():
    for i in range(512):
        for j in range(512):
            if(colored_segment[i][j][0] == 1):
                colored_segment[i][j][2] = 255

color_border()
cv2.imshow('Original image',colored_segment)
cv2.imwrite('./Almenara/Pred_npys/results-outline-img/redOutline.png',colored_segment)
cv2.waitKey(0)