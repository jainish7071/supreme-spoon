from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

@dataclass
class GenerationConfig:
    output_dir: Path = Path("output")
    duration_seconds: int = 15
    fps: int = 24
    resolution: Tuple[int, int] = (720, 1280)
    background_color: str = "#111111"
    text_color: str = "white"
    font_size: int = 52
    card_count: int = 3
