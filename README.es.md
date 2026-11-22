# 🎬 Dónde publicar mi drama de IA

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

[![Dónde publicar mi drama de IA](guia/assets/banner-es.jpg)](https://inematds.github.io/drama-ia-onde-publicar/guia/es/)

📖 Guía de uso: **https://inematds.github.io/drama-ia-onde-publicar/guia/es/**

Creaste (o vas a crear) una serie de drama con IA y no sabes a quién mostrársela ni quién paga. Este kit elimina las conjeturas: indicas tu ruta, te muestra las 26 puertas que conocemos con la fuente oficial de cada una, pone las abiertas primero, avisa cuáles ya cerraron y redacta el correo de presentación.

## Qué es
Una lista verificada (19/11/2026) de 26 plataformas y programas, con el enlace a la página oficial y la fecha, además de una herramienta de línea de comandos y una skill para Claude Code. Está pensada para quienes crean dramas verticales con IA. Resuelve «adónde lo envío» y «qué escribo». Solo necesita Python 3.

## Instalación técnica
```bash
git clone https://github.com/inematds/drama-ia-onde-publicar && cd drama-ia-onde-publicar
python3 -m drama rotas
python3 -m drama escolher --rota criador
python3 -m drama vencidos
python3 -m drama pitch --titulo "..." --historia "..." --episodios 30 --duracao "90 s" --idioma English --amostra "<link privado>" --canal "<seu canal>" --ferramentas "<ferramentas de IA>"
python3 -m unittest discover -s testes   # 10 testes: 26 linhas, fonte em toda linha, ordem, prazos, pitch
```
Los textos completos (lo que paga cada una, la trampa y la lista de verificación del pitch) están en `docs/` y en `drama escolher --detalhe`.
Skill: copia `skill/onde-publicar-meu-drama` a `~/.claude/skills/`.

## El proceso, de principio a fin
1. 🧠 Indicas la ruta (`drama rotas`).
2. ⚙️ `drama escolher --rota X` muestra las opciones, primero las abiertas y al final las cerradas.
3. 🧠 Abres la fuente de cada una y verificas el país, la cuenta, la duración y los derechos.
4. ⚙️ `drama pitch …` redacta el correo.
5. 🧠 Lo envías (el kit nunca lo envía) y guardas una copia con la fecha.

## Límites
Los valores «hasta US$ X» son el máximo, no lo habitual. Algunas entradas proceden solo de noticias y lo indican. Nada de esto promete ganancias.