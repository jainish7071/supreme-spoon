# Tech Stack for AI Reel & Shorts Automation

## Project structure
1. `scheduler-service`
   - Runs the daily 10 AM job.
   - Triggers generation, review delivery, and publish workflows.

2. `video-generation-service`
   - Builds scripts, voiceovers, visuals, edits to create the final video.
   - Supports free AI providers with plugin-style connectors.

3. `telegram-bot-service`
   - Sends preview messages and options.
   - Receives approve/retry/skip commands.

4. `publish-service`
   - Uploads approved videos to Instagram and YouTube.
   - Uses scheduling or best-time selection.

5. `config + orchestration`
   - Shared configuration for AI providers, Telegram credentials, upload settings.
   - Simple state storage to track pending approvals and skipped days.

## Recommended stack
- Language: `Python 3.12+`
- Scheduler: `APScheduler` or cloud cron on hosted environment
- Telegram bot: `python-telegram-bot`
- HTTP/webhook optionally: `FastAPI`
- Video editing: `FFmpeg`, `moviepy`
- AI calls: `OpenAI` Python SDK, `transformers`, `diffusers`, `coqui-ai-tts`
- Configuration: `.env`, `pydantic`, `dynaconf`
- Persistence: lightweight DB file such as `SQLite` or JSON state store
- Logging: `loguru` or standard `logging`

## Deployment options
- Local / self-hosted: Python app on a server or Raspberry Pi
- VPS / cloud: AWS EC2, Azure VM, DigitalOcean droplet
- Containerized: `Docker` for portability
- Cloud scheduler: GitHub Actions, AWS EventBridge, Azure Functions Timer, or cron job

## Integration layers
- Telegram: bot command processing and file delivery
- AI: provider abstraction for free/premium model selection
- Video editing: assemble final reels and shorts type outputs
- Social upload: Instagram + YouTube APIs or approved automation tools

## Future expansions
- Add analytics storage for best-time predictions.
- Add a web dashboard to preview generated content and manage schedules.
- Add a user prompt interface for daily theme/context.
- Add payment-ready model switching for premium AI services.
