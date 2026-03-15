# Voice-to-Article Pipeline Setup

## What's already done
- [x] Vault folder structure: `~/obsidian-vault/{recordings,transcripts,drafts,archive}`
- [x] Whisper installed in `~/.local/share/whisper-venv/` (medium model, GPU-accelerated)
- [x] Processing script: `~/obsidian-vault/process-recordings.sh`
- [x] GDrive sync script: `~/obsidian-vault/sync-to-gdrive.sh`

## Manual steps remaining

### 1. Install packages (needs sudo)
```bash
sudo apt install -y rclone syncthing
```

### 2. Reboot (fixes NVIDIA driver/library mismatch)
```bash
sudo reboot
```

### 3. Set up rclone for Google Drive
```bash
rclone config
# Choose: n (new remote)
# Name: gdrive
# Type: drive (Google Drive)
# Follow the OAuth prompts in your browser
# Done
```

Test it:
```bash
~/obsidian-vault/sync-to-gdrive.sh
```

### 4. Set up Syncthing
```bash
# Start syncthing
syncthing

# Open http://localhost:8384 in browser
# Add your phone as a device (scan QR code)
# Share ~/obsidian-vault/recordings/ folder with your phone
# On phone: install Syncthing, connect to this machine over Tailscale
```

### 5. Install Obsidian
Download from https://obsidian.md/ (AppImage or Snap)
```bash
# Or via snap:
sudo snap install obsidian
```
Open Obsidian → "Open folder as vault" → select `~/obsidian-vault/`

### 6. Set up cron jobs
```bash
crontab -e
```
Add:
```cron
# Process new recordings every 5 minutes
*/5 * * * * /home/giovanni/obsidian-vault/process-recordings.sh >> /tmp/process-recordings.log 2>&1

# Sync to GDrive every 30 minutes
*/30 * * * * /home/giovanni/obsidian-vault/sync-to-gdrive.sh >> /tmp/gdrive-sync.log 2>&1
```

## How it works

1. Record voice memo on phone → saved to phone's Syncthing folder
2. Syncthing syncs to `~/obsidian-vault/recordings/` over Tailscale
3. Cron runs `process-recordings.sh` every 5 min:
   - Whisper transcribes audio → `transcripts/`
   - Claude matches transcript to existing draft or creates new one → `drafts/`
   - Audio moved to `archive/`
4. Open Obsidian, refine drafts
5. Cron syncs vault to GDrive every 30 min

## File naming for multi-recording grouping
Claude auto-detects topic matches, but you can also help it by prefixing recordings:
- `startup-idea-001.m4a`, `startup-idea-002.m4a` → same article
- `random-thought.m4a` → new article
