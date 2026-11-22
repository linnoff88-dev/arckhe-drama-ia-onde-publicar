# 🎬 Where should I publish my AI drama?

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

[![Where should I publish my AI drama?](guia/assets/banner-en.jpg)](https://inematds.github.io/drama-ia-onde-publicar/guia/en/)

📖 User guide: **https://inematds.github.io/drama-ia-onde-publicar/guia/en/**

You’ve made (or are going to make) an AI drama series and don’t know who to show it to or who pays. This kit takes the guesswork out: tell it your route, and it lists the 26 opportunities we know of, with each one’s official source. It puts open opportunities first, flags those that have closed, and writes your pitch email.

## What it is
A checked list (11/19/2026) of 26 platforms and programs, with links to official pages and dates, plus a command-line tool and a skill for Claude Code. It’s for creators of AI-generated vertical dramas. It answers “where do I submit?” and “what should I write?” All you need is Python 3.

## Technical installation
```bash
git clone https://github.com/inematds/drama-ia-onde-publicar && cd drama-ia-onde-publicar
python3 -m drama rotas
python3 -m drama escolher --rota criador
python3 -m drama vencidos
python3 -m drama pitch --titulo "..." --historia "..." --episodios 30 --duracao "90 s" --idioma English --amostra "<link privado>" --canal "<seu canal>" --ferramentas "<ferramentas de IA>"
python3 -m unittest discover -s testes   # 10 testes: 26 linhas, fonte em toda linha, ordem, prazos, pitch
```
The full details (what each one pays, the catch, and the pitch checklist) are in `docs/` and in `drama escolher --detalhe`.
Skill: copy `skill/onde-publicar-meu-drama` to `~/.claude/skills/`.

## The process, from start to finish
1. 🧠 You specify the route (`drama rotas`).
2. ⚙️ `drama escolher --rota X` lists opportunities, with open ones first and closed ones last.
3. 🧠 You open each one’s source and check the country, account, duration, and rights.
4. ⚙️ `drama pitch …` writes the email.
5. 🧠 You send it (the kit never sends it) and save a dated copy.

## Limitations
The “up to US$ X” amounts are maximums, not typical payouts. Some entries are based only on news articles, and are identified as such. Nothing here guarantees earnings.