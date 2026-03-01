# agent-hicks-marketplace

| | Plugin | Description | Commands |
|---|--------|-------------|----------|
| <img src="assets/kitt-logo.jpg" width="60"> | **kitt** | Enable Claude Code to speak ultra concise summaries via Kokoro TTS (mlx-audio). | `/kitt:speak-enable` `/kitt:speak-disable` `/kitt:whats-going-on` `/kitt:plot-course-to` |
| | **presentation** | Create presentations following Patrick Winston's how-to-speak methodology. Folder-as-presentation model with JS-as-spec authoring and slug-ID slide references. | `/presentation:start` `/presentation:brain-dump` `/presentation:shape` `/presentation:outline` `/presentation:author` |

## Install

```
/plugin marketplace add jrhicks/agent-hicks-marketplace
/plugin install kitt@agent-hicks-marketplace
/plugin install presentation@agent-hicks-marketplace
```

## Local Dev

```bash
claude --plugin-dir ./plugins/kitt
```
