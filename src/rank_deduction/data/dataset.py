import os
import json

import cv2
import numpy as np
from PIL import Image
import torch
from torchvision import transforms
from torch.utils.data import Dataset


class ScoreboardDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.images_dir = os.path.join(root_dir, "images/train")
        self.labels_dir = os.path.join(root_dir, "labels/train")
        self.transform = transform

        self.image_files = sorted(os.listdir(self.images_dir))

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        img_name = self.image_files[idx]
        img_path = os.path.join(self.images_dir, img_name)
    
        label_path = os.path.join(
            self.labels_dir,
            img_name.replace(".jpg", ".json")
        )
    
        image = Image.open(img_path).convert("RGB")
    
        if self.transform:
            image = self.transform(image)
        else:
            image = transforms.ToTensor()(image)
    
        with open(label_path) as f:
            rank = json.load(f)["rank"].lower()
    
        C, H, W = image.shape
    
        crop = image.permute(1, 2, 0).numpy()

        #crop pour garder uniquement la zone des scores
        crop = crop[:32, W - 400:]

        crop = cv2.cvtColor(crop, cv2.COLOR_RGB2GRAY)
    
        crop = (crop * 255).astype(np.uint8)
    
        crop = cv2.resize(
            crop,
            (6000, 500),
            interpolation=cv2.INTER_CUBIC
        )
    
        H, W = crop.shape
    
        teams_score = crop[:, int(0.05 * W):int(0.30 * W)]
        kda = crop[:, int(0.36 * W):int(0.52 * W)]
        cs = crop[:, int(0.64 * W):int(0.78 * W)]
        time = crop[:, int(0.84 * W):]
    
        return {
            "crop_score": torch.from_numpy(teams_score).unsqueeze(0).float(),
            "crop_kda": torch.from_numpy(kda).unsqueeze(0).float(),
            "crop_cs": torch.from_numpy(cs).unsqueeze(0).float(),
            "crop_time": torch.from_numpy(time).unsqueeze(0).float(),
            "rank": rank,
            "filename": img_name
        }