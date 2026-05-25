import textwrap
from pathlib import Path
from typing import Optional

import numpy as np
from PIL import Image, ImageDraw, ImageFont

from .config import GenerationConfig

try:
    from moviepy.video.VideoClip import ImageClip
    from moviepy.video.compositing.CompositeVideoClip import concatenate_videoclips
except ImportError as exc:
    raise ImportError(
        "The moviepy package is required to generate videos. "
        "Please install dependencies with `pip install -r requirements.txt`."
    ) from exc

def generate_script(topic: str) -> str:
    """Create a placeholder script for the video. Replace this with a free AI model later."""
    return (
        f"AI Daily News: {topic}\n\n"
        "Welcome to your daily short. This short video highlights the top points for today. "
        "Follow for daily updates and insights."
    )


def _clean_filename(text: str) -> str:
    safe = text.lower().strip().replace(" ", "-")
    return "".join(ch for ch in safe if ch.isalnum() or ch == "-")


def _build_text_image(text: str, config: GenerationConfig) -> np.ndarray:
    width, height = config.resolution
    image = Image.new("RGB", (width, height), config.background_color)
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("arial.ttf", config.font_size)
    except Exception:
        font = ImageFont.load_default()

    margin = 60
    wrapped = textwrap.wrap(text, width=28)
    y = margin
    for line in wrapped:
        try:
            bbox = draw.textbbox((0, 0), line, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
        except AttributeError:
            text_width, text_height = draw.textsize(line, font=font)
        x = (width - text_width) / 2
        draw.text((x, y), line, font=font, fill=config.text_color)
        y += text_height + 16

    return np.array(image)


def _build_card_clip(text: str, config: GenerationConfig, duration: float) -> ImageClip:
    image = _build_text_image(text, config)
    clip = ImageClip(image).with_duration(duration).with_fps(config.fps)
    return clip


def _split_script(script: str, count: int) -> list[str]:
    paragraphs = [p.strip() for p in script.split("\n\n") if p.strip()]
    if len(paragraphs) >= count:
        return paragraphs[:count]

    words = script.split()
    chunk_size = max(1, len(words) // count)
    return [" ".join(words[i : i + chunk_size]) for i in range(0, len(words), chunk_size)][:count]


def generate_video(topic: str, config: Optional[GenerationConfig] = None, output_name: Optional[str] = None) -> Path:
    config = config or GenerationConfig()
    script = generate_script(topic)
    cards = _split_script(script, config.card_count)
    card_duration = config.duration_seconds / len(cards)
    clips = [_build_card_clip(card, config, card_duration) for card in cards]
    video = concatenate_videoclips(clips, method="compose")

    config.output_dir.mkdir(parents=True, exist_ok=True)
    output_filename = output_name or f"{_clean_filename(topic)}.mp4"
    output_path = config.output_dir / output_filename

    video.write_videofile(
        str(output_path),
        fps=config.fps,
        codec="libx264",
        audio=False,
        logger=None,
    )

    return output_path
