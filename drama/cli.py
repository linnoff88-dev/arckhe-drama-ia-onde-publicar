import argparse, datetime as dt
from . import nucleo as n

AVISO = "Confira a regra do dia na fonte antes de agir (programas mudam e rodadas acabam)."


def _linha(p, s):
    return f"{p['id']:>2}. {p['nome']} — {p['topo']} — {p['status']} [{s}]\n    fonte: {p['fonte']} ({p['fonte_data']}; checado {p['checado']})"


def main(argv=None):
    ap = argparse.ArgumentParser(prog="drama", description="Onde publicar seu drama de IA")
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("escolher", help="plataformas da sua rota, abertas primeiro")
    e.add_argument("--rota", required=True, choices=list(n.ROTAS))
    e.add_argument("--hoje", help="AAAA-MM-DD (teste)")
    e.add_argument("--detalhe", action="store_true", help="mostra o que paga e a pegadinha de cada uma")
    v = sub.add_parser("vencidos", help="rodadas encerradas ou vencidas na lista")
    v.add_argument("--hoje")
    sub.add_parser("rotas", help="explica as 3 rotas")
    p = sub.add_parser("pitch", help="e-mail de pitch pronto")
    for k in ("titulo", "historia", "episodios", "duracao", "idioma", "amostra", "canal", "ferramentas"):
        p.add_argument("--" + k, required=True)
    p.add_argument("--app", default="[APP]")
    p.add_argument("--nome", default="[SEU NOME]")
    a = ap.parse_args(argv)
    hoje = dt.date.fromisoformat(a.hoje) if getattr(a, "hoje", None) else None
    if a.cmd == "rotas":
        print("pitch   : app de drama (você propõe, não há botão de enviar)\n"
              "criador : programa de criador / ferramenta que paga (você já posta em rede social)\n"
              "piloto  : plataforma nova de drama (você envia um piloto)")
    elif a.cmd == "escolher":
        for pl, s in n.escolher(a.rota, hoje):
            print(_linha(pl, s))
            if a.detalhe:
                print(f"    paga: {pl['paga']}\n    pegadinha: {pl['pegadinha']}")
        print("\n" + AVISO)
    elif a.cmd == "vencidos":
        for pl, s in n.vencidos(hoje):
            print(_linha(pl, s))
    else:
        print(n.pitch(a.titulo, a.historia, a.episodios, a.duracao, a.idioma, a.amostra, a.canal, a.ferramentas, a.app, a.nome))
    return 0
