# API Uses for Daily AI Video Publishing

## Core APIs required
1. Telegram Bot API
   - Send notifications with video preview or short clips.
   - Receive user commands for `approve`, `retry`, `skip`.
   - Use `sendVideo`, `sendMessage`, `answerCallbackQuery`.

2. YouTube Data API v3
   - Upload short-form videos.
   - Set metadata: title, description, tags, privacy.
   - Optionally schedule publish time.
   - Use OAuth 2.0 for account authentication.

3. Instagram Graph API / Instagram Basic Display API
   - Upload reels or feed videos.
   - Use Facebook App with `instagram_content_publish` permission.
   - Manage media creation and publish flow.

## AI provider APIs
### Free or open-source providers
- OpenAI API for GPT-3.5 and chat-based scripting with a free tier trial.
- Hugging Face Inference API for text, image, and audio models.
- Coqui TTS inference endpoints for voice generation.
- Stable Diffusion via Hugging Face or local runtime.

### Premium provider APIs (future upgrade)
- OpenAI GPT-4.1 and image/video endpoints.
- ElevenLabs for premium voice.
- Runway, Pika Labs, or Sora for video generation.
- Premium social analytics APIs for best-time recommendations.

## Optional supporting APIs
1. Best publish time / analytics
   - Use heuristic or simple analytics service.
   - Could integrate `Hootsuite`, `Buffer`, or social analytics vendor for peak time data.

2. URL shortening / tracking
   - Optional if you want tracking links or CTA performance.

3. Cloud storage / file hosting
   - AWS S3, Google Cloud Storage, or similar to store generated videos before upload.

## Notes on API usage
- Start with Telegram first: it is the direct review/approval channel.
- Use local or lightweight free AI providers initially to reduce costs.
- Instagram API requires app review and business account access, so plan that integration carefully.
- YouTube upload is easier for creators using OAuth 2.0 and a channel with upload privileges.
