import numpy as np
import easyocr

reader = easyocr.Reader(['en'])

def ocr_image(img):
    img_np = img.permute(1, 2, 0).cpu().numpy()
    img_np = (img_np * 255).astype(np.uint8)
    return reader.readtext(img_np, detail=0)

def tensor_to_uint8(img_tensor):
    img = img_tensor.squeeze(0).cpu().numpy()

    if img.max() <= 1.0:
        img = (img * 255).astype("uint8")
    else:
        img = img.astype("uint8")

    return img


def ocr_region(img_tensor):
    img = tensor_to_uint8(img_tensor)
    return reader.readtext(img, detail=0)