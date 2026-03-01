# agent-hicks-marketplace

| | Plugin | Description | Commands |
|---|--------|-------------|----------|
| <img src="assets/kitt-logo.jpg" width="60"> | **kitt** | Enable Claude Code to speak ultra concise summaries via Kokoro TTS (mlx-audio). | `/kitt:speak-enable` `/kitt:speak-disable` `/kitt:whats-going-on` `/kitt:plot-course-to` |
| | **hts** | Create presentations following Patrick Winston's how-to-speak methodology. | `/hts:start` `/hts:brain-dump` `/hts:shape` `/hts:outline` `/hts:author` `/hts:chalkboard` |

## Install

```
/plugin marketplace add jrhicks/agent-hicks-marketplace
/plugin install kitt@agent-hicks-marketplace
/plugin install hts@agent-hicks-marketplace
```

## Local Dev

```bash
claude --plugin-dir ./plugins/kitt
```
