import datetime as dt, unittest
from drama import nucleo as n
H = dt.date(2026, 11, 21)

class T(unittest.TestCase):
    def test_26_plataformas(self):
        self.assertEqual(len(n.carregar()), 26)
    def test_toda_linha_tem_fonte_https(self):
        for p in n.carregar():
            self.assertTrue(p["fonte"].startswith("http"), p["nome"])
    def test_rotas_cobrem_tudo_uma_vez(self):
        tot = sum(len(n.escolher(r, H)) for r in n.ROTAS)
        self.assertEqual(tot, 26)
    def test_encerrado_vai_para_o_fim(self):
        r = n.escolher("criador", H)
        self.assertEqual(r[-1][1], "encerrado")
    def test_prazo_perto_vem_primeiro(self):
        r = n.escolher("criador", H)
        self.assertEqual(r[0][0]["nome"].split()[0], "OiiOii")
        self.assertEqual(r[0][1], "vence-em-breve")
    def test_prazo_passado_vira_vencido(self):
        r = dict((p["nome"], s) for p, s in n.escolher("criador", dt.date(2026, 12, 1)))
        self.assertEqual(r[[k for k in r if k.startswith("OiiOii")][0]], "vencido")
    def test_rota_invalida(self):
        with self.assertRaises(ValueError): n.escolher("x")
    def test_vencidos_lista_o_encerrado(self):
        self.assertIn("Picsart", " ".join(p["nome"] for p, _ in n.vencidos(H)))
    def test_pitch_leva_todos_campos(self):
        t = n.pitch("T", "uma herdeira", "30", "90 s", "English", "link", "@x", "Kling")
        for s in ("T", "uma herdeira", "30 × 90 s", "link", "@x", "Kling", "9:16"): self.assertIn(s, t)

class D(unittest.TestCase):
    def test_toda_linha_tem_o_que_paga(self):
        for p in n.carregar():
            self.assertTrue(p["paga"], p["nome"])
