
from torchvision import transforms
from torch.utils.data import DataLoader

from rank_deduction.data.dataset import ScoreboardDataset

def get_data(path = "data") :
    transform = transforms.ToTensor()
    dataset = ScoreboardDataset(path, transform=transform)

    return dataset