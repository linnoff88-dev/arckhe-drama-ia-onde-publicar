# ðŸŽ¬ Onde publicar meu drama de IA

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


**ðŸ‡§ðŸ‡· [PortuguÃªs](README.md) Â· ðŸ‡ºðŸ‡¸ [English](README.en.md) Â· ðŸ‡ªðŸ‡¸ [EspaÃ±ol](README.es.md)**

[![Onde publicar meu drama de IA](guia/assets/banner.jpg)](https://linnoff88-dev.github.io/

ðŸ“– Guia de uso: **https://linnoff88-dev.github.io/

VocÃª fez (ou vai fazer) uma sÃ©rie de drama com IA e nÃ£o sabe a quem mostrar nem quem paga. Este kit tira o chute: vocÃª diz sua rota, ele lista as 26 portas que conhecemos com a fonte oficial de cada uma, pÃµe as abertas na frente, avisa as que jÃ¡ fecharam e escreve o e-mail de pitch.

## O que Ã©
Uma lista conferida (19/11/2026) de 26 plataformas e programas, com link da pÃ¡gina oficial e data, mais uma ferramenta de linha de comando e uma skill para o Claude Code. Serve a quem cria dramas verticais com IA. Resolve "para onde mando" e "o que escrevo". Precisa sÃ³ de Python 3.

## InstalaÃ§Ã£o tÃ©cnica
```bash
git clone https://github.com/linnoff88-dev/drama-ia-onde-publicar && cd drama-ia-onde-publicar
python3 -m drama rotas
python3 -m drama escolher --rota criador
python3 -m drama vencidos
python3 -m drama pitch --titulo "..." --historia "..." --episodios 30 --duracao "90 s" --idioma English --amostra "<link privado>" --canal "<seu canal>" --ferramentas "<ferramentas de IA>"
python3 -m unittest discover -s testes   # 10 testes: 26 linhas, fonte em toda linha, ordem, prazos, pitch
```
Os textos completos (o que cada uma paga, a pegadinha, e o checklist de pitch) estÃ£o em `docs/` e em `drama escolher --detalhe`.
Skill: copie `skill/onde-publicar-meu-drama` para `~/.claude/skills/`.

## O processo, do inÃ­cio ao fim
1. ðŸ§  VocÃª diz a rota (`drama rotas`).
2. âš™ï¸ `drama escolher --rota X` lista, abertas primeiro, encerradas por Ãºltimo.
3. ðŸ§  VocÃª abre a fonte de cada uma e confere paÃ­s, conta, duraÃ§Ã£o, direitos.
4. âš™ï¸ `drama pitch â€¦` escreve o e-mail.
5. ðŸ§  VocÃª envia (o kit nunca envia) e guarda a cÃ³pia com a data.

## Limites
Os valores "atÃ© US$ X" sÃ£o o teto, nÃ£o o comum. Algumas linhas vÃªm sÃ³ de notÃ­cia e dizem isso. Nada aqui Ã© promessa de ganho.

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>