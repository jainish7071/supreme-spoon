# Supreme Spoon - Development Plan

## Goal
Build the first working iteration of the AI video generation tool for Instagram Reels and YouTube Shorts.

## Phase 1: Video Generation Tool
1. Create a Python package for video generation.
2. Add a simple generator that can produce a 9:16 short-form video.
3. Provide a command-line entrypoint for local testing.
4. Use free, local fallback generation for the first iteration.
5. Keep AI model exchangeable for later upgrades.

## Deliverables for this step
- `plan.md`
- `requirements.txt`
- `video_tool/` Python package
- `github-copilot.instruction.md` updated with progress notes

## How to test this first implementation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the generator:
   ```bash
   python -m video_tool --topic "AI daily news"
   ```
3. Confirm that `output/ai-daily-news.mp4` is created.

## Next step after testing
- Replace the fallback script generator with a free AI text-generation model.
- Add Telegram bot notification and approval flow.
- Add scheduler support for daily automation at 10 AM.

## Notes
This iteration focuses on structure and a working local proof of concept. The file `video_tool/generator.py` is intentionally built to be replaced with real AI model calls later.
