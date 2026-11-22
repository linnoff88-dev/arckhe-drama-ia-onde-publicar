import csv, datetime as dt, os

ARQ = os.path.join(os.path.dirname(__file__), "plataformas.csv")
ROTAS = {
    "pitch": ("app",),                         # quero propor a série a um app de drama
    "criador": ("aberta", "ferramenta", "afiliado"),  # já posto em rede social
    "piloto": ("nova",),                       # quero enviar um piloto a plataforma nova
}


def carregar(arq=ARQ):
    with open(arq, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def situacao(p, hoje=None):
    """'encerrado' | 'vencido' | 'vence-em-breve' | 'sem-prazo' | 'aberto'."""
    hoje = hoje or dt.date.today()
    if p["encerrado"]:
        return "encerrado"
    if p["prazo"]:
        dias = (dt.date.fromisoformat(p["prazo"]) - hoje).days
        return "vencido" if dias < 0 else "vence-em-breve" if dias <= 14 else "aberto"
    return "sem-prazo"


_ORDEM = {"vence-em-breve": 0, "aberto": 1, "sem-prazo": 2, "vencido": 3, "encerrado": 4}


def escolher(rota, hoje=None, dados=None):
    if rota not in ROTAS:
        raise ValueError(f"rota desconhecida: {rota} (use {', '.join(ROTAS)})")
    dados = dados if dados is not None else carregar()
    achados = [p for p in dados if p["porta"] in ROTAS[rota]]
    achados.sort(key=lambda p: (_ORDEM[situacao(p, hoje)], int(p["id"])))
    return [(p, situacao(p, hoje)) for p in achados]


def vencidos(hoje=None, dados=None):
    dados = dados if dados is not None else carregar()
    return [(p, s) for p in dados if (s := situacao(p, hoje)) in ("vencido", "encerrado")]


def pitch(titulo, historia, episodios, duracao, idioma, amostra, canal, ferramentas, app="[APP]", nome="[SEU NOME]"):
    return (
        f"Subject: AI drama pitch: {titulo} ({episodios} episodes × {duracao})\n\n"
        f"Hi {app} team,\n\n"
        f"I make vertical AI dramas. {titulo} is about {historia}.\n\n"
        f"- Episodes: {episodios} × {duracao}, vertical 9:16, {idioma}\n"
        f"- Sample episodes: {amostra}\n"
        f"- My channel: {canal}\n"
        f"- Rights: I own the story, the characters and the music. Made with {ferramentas}.\n\n"
        "Could you tell me what you need from a content provider to consider it?\n\n"
        f"Thanks,\n{nome}\n"
    )
