# AI Uses for Video Generation Tool

## Core AI goals
- Generate short-form video content for Instagram Reels and YouTube Shorts.
- Produce daily unique scripts, narration, visuals, and captions.
- Keep the system adaptable so free models can be replaced by premium models later.

## Free-tier AI options
1. Text / script generation
   - OpenAI GPT-3.5 Turbo (free-tier via API credits / limited volume)
   - Hugging Face hosted models: `gpt2-medium`, `mistral-small`, `flan-t5-base`
   - Local LLMs (if needed): `llama.cpp` / `ggml` variants for offline script drafts

2. Voice / narration generation
   - Coqui TTS community models
   - Open-source TTS via Hugging Face: `espnet`, `tts_models/en/ljspeech/tacotron2-DDC`
   - Mozilla TTS or `Tortoise` for simple voice audio

3. Image / visual generation
   - Stable Diffusion variants on Hugging Face or local `Stable Diffusion 1.5`
   - `DALL·E mini` / `Craiyon` style open tools for thumbnail or scene art
   - ControlNet + SD for simple motion or background frames

4. Video assembly and editing
   - FFmpeg for templated video editing, audio mixing, caption overlay.
   - Open-source Python libraries: `moviepy`, `manim` for simple dynamic visuals.

## Premium-tier AI options
1. Premium text generation
   - OpenAI GPT-4.1 / GPT-4.1 Mini
   - Anthropic Claude 3 / Claude 3.5
   - Google Vertex AI PaLM 2

2. Premium voice generation
   - ElevenLabs
   - Murf.ai
   - Play.ht
   - Azure Speech Service neural voices

3. Premium image/video generation
   - OpenAI `gpt-image-1` or `gpt-video-1`
   - Runway Gen-2
   - Sora / Pika Labs / Google Imagen Video
   - Midjourney for high-quality visuals

4. Premium automation and optimization
   - Social media analytics AI for best posting time
   - AI caption/title optimization services
   - Workflow orchestration with paid platforms like Zapier or n8n cloud

## Model compatibility strategy
- Encapsulate AI tasks behind a service interface.
- Allow script generation, TTS, visuals, and editing to swap providers with minimal code changes.
- Prefer configuration-driven provider selection.
- Start with open-source/free providers and later switch to paid APIs by changing provider settings only.
