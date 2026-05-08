# Voice-to-Article Pipeline Setup

## What's already done
- [x] Vault folder structure: `~/obsidian-vault/{recordings,transcripts,drafts,archive}`
- [x] Whisper installed in `~/.local/share/whisper-venv/` (medium model, GPU-accelerated)
- [x] Processing script: `~/obsidian-vault/process-recordings.sh`
- [x] Git backup to `git@github.com:TheF1rstPancake/obsidian_vault.git`
- [x] Backup script: `~/obsidian-vault/sync-vault.sh` (auto-commits and pushes)
- [x] Cron jobs installed (process recordings every 5 min, git sync every 30 min)
- [x] rclone + syncthing installed

## Manual steps remaining

### 1. Expose Syncthing UI via Tailscale (needs sudo)
```bash
sudo tailscale serve --bg --https 8385 http://127.0.0.1:8384
```
Then open `https://<your-tailscale-host>:8385` (find your host with `tailscale status`).

### 2. Start Syncthing and pair phone
```bash
syncthing
```
- Open `https://<your-tailscale-host>:8385` from any device on tailnet
- Add your phone as a device (scan QR code)
- Share `~/obsidian-vault/recordings/` folder with your phone
- On phone: install Syncthing, connect over Tailscale

### 3. Install Obsidian
Download from https://obsidian.md/ (AppImage or Snap)
```bash
sudo snap install obsidian
```
Open Obsidian → "Open folder as vault" → select `~/obsidian-vault/`

## Services & URLs

| Service    | URL / Location                                    |
|------------|---------------------------------------------------|
| Syncthing  | `https://<your-tailscale-host>:8385`              |
| GitHub     | `github.com/TheF1rstPancake/obsidian_vault`       |
| Vault path | `~/obsidian-vault/`                               |

## Cron jobs (installed)
```cron
# Process new recordings every 5 minutes
*/5 * * * * /home/giovanni/obsidian-vault/process-recordings.sh >> /tmp/process-recordings.log 2>&1

# Sync vault to GitHub every 30 minutes
*/30 * * * * /home/giovanni/obsidian-vault/sync-vault.sh >> /tmp/vault-sync.log 2>&1
```

## How it works

1. Record voice memo on phone → saved to phone's Syncthing folder
2. Syncthing syncs to `~/obsidian-vault/recordings/` over Tailscale
3. Cron runs `process-recordings.sh` every 5 min:
   - Whisper transcribes audio → `transcripts/`
   - Claude matches transcript to existing draft or creates new one → `drafts/`
   - Audio moved to `archive/`
4. Open Obsidian, refine drafts
5. Cron syncs vault to GitHub every 30 min

## File naming for multi-recording grouping
Claude auto-detects topic matches, but you can also help it by prefixing recordings:
- `startup-idea-001.m4a`, `startup-idea-002.m4a` → same article
- `random-thought.m4a` → new article
