from pathlib import Path
from typing import Any, Dict, List

from .base_dataset import BaseClimbingDataset, DatasetSample


class PlaceholderDatasetAdapter(BaseClimbingDataset):
    """Replace this with the real dataset adapter after inspecting ml/data/."""

    def inspect(self) -> Dict[str, Any]:
        return {
            "root_exists": self.root.exists(),
            "children": sorted([p.name for p in self.root.glob("*")]),
            "note": "Implement actual inspection after real data is added."
        }

    def samples(self, split: str) -> List[DatasetSample]:
        split_dir = self.root / split
        if not split_dir.exists():
            return []
        image_paths = list(split_dir.rglob("*.jpg")) + list(split_dir.rglob("*.png"))
        return [
            DatasetSample(image_path=p, annotation_path=None, metadata={"split": split})
            for p in image_paths
        ]
