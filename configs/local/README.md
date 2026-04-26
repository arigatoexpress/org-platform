# Local Environment

Preferred setup:

```bash
brew bundle --file configs/local/Brewfile
mise install
cp .env.example .env
direnv allow
./scripts/bootstrap.sh
```

Secrets should come from 1Password CLI or the shell environment. Do not write real tokens to `.env` in a shared branch.

