# Subtitle Ingestion

Supported inputs:

- Subtitles downloaded by `yt-dlp` as VTT or SRT from any supported video site.
- Local transcripts from `transcribe_audio.py` as TSV or Markdown.
- User-provided subtitles copied from a browser or translation extension.

Rules:

- Keep timestamps whenever available.
- Remove repeated auto-caption fragments.
- Preserve bilingual lines when the user provides them; do not translate away the original.
- For tutorial work, group transcript content into steps rather than producing only a summary.
- Mark unclear operations with their timestamp so the user can provide a screenshot or ask for a focused recheck.
- Do not treat subtitles as visual proof. For visual learning, extract or request keyframes for technique checkpoints.
