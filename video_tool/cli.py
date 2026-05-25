import argparse

from .config import GenerationConfig
from .generator import generate_video


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a short-form video for Instagram Reels and YouTube Shorts.")
    parser.add_argument("--topic", required=True, help="Topic or prompt for the video")
    parser.add_argument("--output", help="Optional output filename without extension")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = GenerationConfig()
    output_name = f"{args.output}.mp4" if args.output else None
    output_path = generate_video(args.topic, config=config, output_name=output_name)
    print(f"Video generated: {output_path}")
