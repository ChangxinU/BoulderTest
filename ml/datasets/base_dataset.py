from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List


@dataclass
class DatasetSample:
    image_path: Path
    annotation_path: Path | None
    metadata: Dict[str, Any]


class BaseClimbingDataset:
    """Base dataset interface for climbing hold data."""

    def __init__(self, root: str) -> None:
        self.root = Path(root)

    def inspect(self) -> Dict[str, Any]:
        raise NotImplementedError

    def samples(self, split: str) -> List[DatasetSample]:
        raise NotImplementedError
