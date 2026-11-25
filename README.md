# ê°Å¸Å½Â¬ Onde publicar meu drama de IA

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


**ê°Å¸â¡Â§ê°Å¸â¡Â· [PortuguêÂªs](README.md) êÂ· ê°Å¸â¡Âºê°Å¸â¡Â¸ [English](README.en.md) êÂ· ê°Å¸â¡Âªê°Å¸â¡Â¸ [EspaêÂ±ol](README.es.md)**

[![Onde publicar meu drama de IA](guia/assets/banner.jpg)](https://linnoff88-dev.github.io/

ê°Å¸ââ Guia de uso: **https://linnoff88-dev.github.io/

VocêÂª fez (ou vai fazer) uma sêÂ©rie de drama com IA e nêÂ£o sabe a quem mostrar nem quem paga. Este kit tira o chute: vocêÂª diz sua rota, ele lista as 26 portas que conhecemos com a fonte oficial de cada uma, pêÂµe as abertas na frente, avisa as que jêÂ¡ fecharam e escreve o e-mail de pitch.

## O que êÂ©
Uma lista conferida (19/11/2026) de 26 plataformas e programas, com link da pêÂ¡gina oficial e data, mais uma ferramenta de linha de comando e uma skill para o Claude Code. Serve a quem cria dramas verticais com IA. Resolve "para onde mando" e "o que escrevo". Precisa sêÂ³ de Python 3.

## InstalaêÂ§êÂ£o têÂ©cnica
```bash
git clone https://github.com/linnoff88-dev/drama-ia-onde-publicar && cd drama-ia-onde-publicar
python3 -m drama rotas
python3 -m drama escolher --rota criador
python3 -m drama vencidos
python3 -m drama pitch --titulo "..." --historia "..." --episodios 30 --duracao "90 s" --idioma English --amostra "<link privado>" --canal "<seu canal>" --ferramentas "<ferramentas de IA>"
python3 -m unittest discover -s testes   # 10 testes: 26 linhas, fonte em toda linha, ordem, prazos, pitch
```
Os textos completos (o que cada uma paga, a pegadinha, e o checklist de pitch) estêÂ£o em `docs/` e em `drama escolher --detalhe`.
Skill: copie `skill/onde-publicar-meu-drama` para `~/.claude/skills/`.

## O processo, do inêÂ­cio ao fim
1. ê°Å¸Â§Â  VocêÂª diz a rota (`drama rotas`).
2. ê¢Å¡â¢ê¯Â¸Â `drama escolher --rota X` lista, abertas primeiro, encerradas por êÂºltimo.
3. ê°Å¸Â§Â  VocêÂª abre a fonte de cada uma e confere paêÂ­s, conta, duraêÂ§êÂ£o, direitos.
4. ê¢Å¡â¢ê¯Â¸Â `drama pitch ê¢â¬Â¦` escreve o e-mail.
5. ê°Å¸Â§Â  VocêÂª envia (o kit nunca envia) e guarda a cêÂ³pia com a data.

## Limites
Os valores "atêÂ© US$ X" sêÂ£o o teto, nêÂ£o o comum. Algumas linhas vêÂªm sêÂ³ de notêÂ­cia e dizem isso. Nada aqui êÂ© promessa de ganho.

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>