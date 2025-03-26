import os
import torch
import numpy as np
import torchvision.transforms as T
from torch.utils.data import Dataset
from PIL import Image
import json

class CustomDataset(Dataset):
    def __init__(self, root, annotation_file, transforms=None):
        self.root = root
        self.transforms = transforms
        with open(annotation_file) as f:
            self.annotations = json.load(f)

    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, idx):
        data = self.annotations[idx]
        img_path = os.path.join(self.root, data["file_name"])
        image = Image.open(img_path).convert("RGB")

        boxes = torch.tensor(data["boxes"], dtype=torch.float32)
        labels = torch.tensor(data["labels"], dtype=torch.int64)

        target = {"boxes": boxes, "labels": labels}
        if self.transforms:
            image = self.transforms(image)

        return image, target

# 데이터 변환 설정
transform = T.Compose([
    T.ToTensor()
])

# 데이터셋 로드
dataset = CustomDataset("data/images", "data/annotations.json", transform)
dataloader = torch.utils.data.DataLoader(dataset, batch_size=2, shuffle=True)

import torch.optim as optim

# 모델 불러오기
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
num_classes = 10  # 클래스 개수 설정 (배경 포함)

# 분류기 헤드 수정
in_features = model.roi_heads.box_predictor.cls_score.in_features
model.roi_heads.box_predictor = torchvision.models.detection.faster_rcnn.FastRCNNPredictor(in_features, num_classes)

# 학습 설정
optimizer = optim.Adam(model.parameters(), lr=0.0001)
criterion = torch.nn.CrossEntropyLoss()

# 학습 루프
for epoch in range(5):
    for images, targets in dataloader:
        optimizer.zero_grad()
        loss_dict = model(images, targets)
        loss = sum(loss for loss in loss_dict.values())
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item()}")
