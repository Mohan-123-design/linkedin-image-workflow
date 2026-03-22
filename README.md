# LinkedIn Image Generation Workflow

End-to-end automation for generating LinkedIn post images. Reads post content from Google Sheets, generates AI image prompts via Perplexity, creates images using Google Gemini, and writes results back to the sheet — fully automated via n8n.

## Architecture

```
Google Sheets (post content)
        ↓
Perplexity API (generate image prompt)
        ↓
Google Gemini (generate image)
        ↓
Slack (upload image file)
        ↓
Google Sheets (write back: prompt + image URL + status)
```

## Contents

| Folder | Description |
|--------|-------------|
| `python_scripts/` | Python implementation of the workflow |
| `n8n_workflows/` | n8n JSON workflow files (importable directly) |

## n8n Workflows

| File | Description |
|------|-------------|
| `workflow_prompt_generation.json` | Step 1 — reads content, calls Perplexity, writes prompt back to sheet |
| `workflow_image_generation.json` | Step 2 — reads prompt, generates image via Gemini, uploads to Slack, writes URL |
| `Updated Linkedin Post Image Generation WF.json` | Combined workflow |

### How to Import n8n Workflows

1. Open your n8n instance
2. Go to **Workflows → Import from file**
3. Upload the `.json` file
4. Connect your credentials (Google Sheets, Perplexity, Google Gemini, Slack)
5. Activate the workflow

## Python Scripts Setup

```bash
pip install -r python_scripts/requirements.txt
cp python_scripts/config/.env.example python_scripts/config/.env
# Add your API keys to .env
python python_scripts/scripts/main.py
```

## Google Sheet Structure

| S. No | Content | PROMPT | Status | URLS |
|-------|---------|--------|--------|------|
| 1 | Post text here | (auto-filled) | (auto-filled) | (auto-filled) |

## Features

- Per-row status tracking — partial runs are resumable
- Polls every minute for new unprocessed rows
- Uploads images to Slack and writes back the permalink + private URL
- Supports 1:1 ratio image generation for LinkedIn posts

## Tech Stack

- n8n (workflow orchestration)
- Perplexity API (prompt generation)
- Google Gemini 2.5 Flash Image (image generation)
- Google Sheets API
- Slack API
- Python, google-generativeai
