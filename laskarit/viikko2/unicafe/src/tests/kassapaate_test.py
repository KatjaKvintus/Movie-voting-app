import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()
    
    # Luodun kassapäätteen rahamäärä ja myytyjen lounaiden määrä on oikea 
    # (rahaa 1000 euroa, lounaita myyty 0)
    def test_kassapaatteen_rahamaara_oikea(self):
        kassan_saldo = self.kassapaate.kassassa_rahaa
        edulliset = self.kassapaate.edulliset
        maukkaat = self.kassapaate.maukkaat
        self.assertEqual(kassan_saldo, 100000)
        self.assertEqual(edulliset, 0)
        self.assertEqual(maukkaat, 0)
    
    # Käteisosto toimii edullisten lounaiden osalta
    def test_kateisosto_toimii_molemmilla_lounastyypeilla(self):

        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(400)
        self.assertEqual(160, vaihtoraha)

        kassan_saldo = self.kassapaate.kassassa_rahaa
        self.assertEqual(kassan_saldo, 100240)
    
    # Käteisosto toimii maukkaiden lounaiden osalta
    def test_kateisosto_toimii_molemmilla_lounastyypeilla(self):

        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(100, vaihtoraha)

        kassan_saldo = self.kassapaate.kassassa_rahaa
        self.assertEqual(kassan_saldo, 100400)
    
    # Jos maksu riittävä: kassassa oleva rahamäärä kasvaa lounaan hinnalla
    def test_riittava_maksu_nostaa_kassan_saldoa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.kassapaate.syo_maukkaasti_kateisella(400)
        kassan_saldo = self.kassapaate.kassassa_rahaa
        self.assertEqual(kassan_saldo, 100640)

    # Jos maksu riittävä: vaihtorahan suuruus on oikea
    def test_vaihtorahana_suuruus_on_oikea_jos_maksu_riittaa(self):
        vaihtoraha_maukas = self.kassapaate.syo_maukkaasti_kateisella(500)
        vaihtoraha_edullinen = self.kassapaate.syo_edullisesti_kateisella(400)
        self.assertEqual(100, vaihtoraha_maukas)
        self.assertEqual(160, vaihtoraha_edullinen)

    # Jos maksu on riittävä: myytyjen lounaiden määrä kasvaa
    def test_myytyjen_lounaiden_maara_kasvaa_jos_maksu_riittava(self):
        self.kassapaate.__init__()
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.kassapaate.syo_maukkaasti_kateisella(400)
        edulliset = self.kassapaate.edulliset
        maukkaat = self.kassapaate.maukkaat
        self.assertEqual(edulliset, 3)
        self.assertEqual(maukkaat, 1)

    # Jos maksu ei ole riittävä: kassassa oleva rahamäärä ei muutu
    def test_jos_maksu_ei_riita_kassan_saldo_ei_muutu(self):
        self.kassapaate.__init__()
        self.kassapaate.syo_edullisesti_kateisella(140)
        self.kassapaate.syo_maukkaasti_kateisella(20)
        kassan_saldo = self.kassapaate.kassassa_rahaa
        self.assertEqual(kassan_saldo, 100000)
    
    # Jos maksu ei ole riittävä: kaikki rahat palautetaan vaihtorahana 
    def test_jos_maksu_ei_riita_kaikki_rahat_palautetaan_vaihtorahana(self):
        vaihtoraha1 = self.kassapaate.syo_maukkaasti_kateisella(100)
        vaihtoraha2 = self.kassapaate.syo_edullisesti_kateisella(5)
        self.assertEqual(100, vaihtoraha1)
        self.assertEqual(5, vaihtoraha2)

    # Jos maksu ei ole riittävä: myytyjen lounaiden määrässä ei muutosta
    def test_jos_maksu_ei_riita_vaihtoraha_oikein_ja_myytyjen_maara_ei_muutu(self):
        self.kassapaate.__init__()
        self.kassapaate.syo_edullisesti_kateisella(140)
        self.kassapaate.syo_maukkaasti_kateisella(20)
        edulliset = self.kassapaate.edulliset
        maukkaat = self.kassapaate.maukkaat
        self.assertEqual(edulliset, 0)
        self.assertEqual(maukkaat, 0)

    # Korttiosto toimii edullisten lounaiden osalta
    # Jos kortilla on tarpeeksi rahaa, veloitetaan summa kortilta ja palautetaan True
    # Jos kortilla on tarpeeksi rahaa, myytyjen lounaiden määrä kasvaa
    def test_edullisen_korttiosto_toimii_kun_kortilla_on_tarpeeksi_rahaa(self):
        self.kassapaate.__init__()
        self.maksukortti = Maksukortti(1000)        
        osto_onnistuu = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        kortin_saldo = self.maksukortti.saldo
        self.maksukortti.ota_rahaa(240)
        edulliset = self.kassapaate.edulliset        
        self.assertTrue(osto_onnistuu)
        self.assertEqual(edulliset, 1)
        self.assertEqual(kortin_saldo, 760)

    # Korttiosto toimii edullisten lounaiden osalta
    # Jos kortilla ei ole tarpeeksi rahaa, kortin rahamäärä ei muutu, myytyjen lounaiden määrä muuttumaton ja palautetaan False
    # Kassassa oleva rahamäärä ei muutu kortilla ostettaessa
    def test_edullisen_korttiosto_ei_onnistu_kun_kortilla_ei_ole_tarpeeksi_rahaa(self):
        self.kassapaate.__init__()
        self.maksukortti = Maksukortti(100)        
        osto_onnistuu = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        kortin_saldo = self.maksukortti.saldo
        self.maksukortti.ota_rahaa(240)
        edulliset = self.kassapaate.edulliset        
        self.assertFalse(osto_onnistuu)
        self.assertEqual(edulliset, 0)
        self.assertEqual(kortin_saldo, 100)

    # Korttiosto toimii maukkaiden lounaiden osalta
    # Jos kortilla on tarpeeksi rahaa, veloitetaan summa kortilta ja palautetaan True
    # Jos kortilla on tarpeeksi rahaa, myytyjen lounaiden määrä kasvaa
    def test_maukkaan_korttiosto_toimii_kun_kortilla_on_tarpeeksi_rahaa(self):
        self.kassapaate.__init__()
        self.maksukortti = Maksukortti(1000)        
        osto_onnistuu = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        kortin_saldo = self.maksukortti.saldo
        self.maksukortti.ota_rahaa(400)
        maukkaat = self.kassapaate.maukkaat        
        self.assertTrue(osto_onnistuu)
        self.assertEqual(maukkaat, 1)
        self.assertEqual(kortin_saldo, 600)

    # Korttiosto toimii maukkaiden lounaiden osalta
    # Jos kortilla ei ole tarpeeksi rahaa, kortin rahamäärä ei muutu, myytyjen lounaiden määrä muuttumaton ja palautetaan False
    # Kassassa oleva rahamäärä ei muutu kortilla ostettaessa
    def test_maukkaan_korttiosto_ei_onnistu_kun_kortilla_ei_ole_tarpeeksi_rahaa(self):
        self.kassapaate.__init__()
        self.maksukortti = Maksukortti(100)        
        osto_onnistuu = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        kortin_saldo = self.maksukortti.saldo
        self.maksukortti.ota_rahaa(240)
        maukkaat = self.kassapaate.maukkaat        
        self.assertFalse(osto_onnistuu)
        self.assertEqual(maukkaat, 0)
        self.assertEqual(kortin_saldo, 100)

    # Kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä kasvaa ladatulla summalla
    def test_kortin_lataaminen_muuttaa_kortin_saldoa_ja_kassan_saldoa(self):
        self.kassapaate.__init__()
        self.maksukortti = Maksukortti(100)        
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        kassan_uusi_saldo = self.kassapaate.kassassa_rahaa
        kortin_uusi_saldo = self.maksukortti.saldo
        self.assertEqual(kassan_uusi_saldo, 100100)
        self.assertEqual(kortin_uusi_saldo, 200)

    # Jos kortille yrittää ladata negatiivista summaa, kortin saldo ei muutu eikä kassan rahamäärä muutu
    def test_kortin_latausyritys_negat_summalla_ei_muuta_kortin_saldoa_eika_kassan_saldoa(self):
        self.kassapaate.__init__()
        self.maksukortti = Maksukortti(100)        
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        kassan_uusi_saldo = self.kassapaate.kassassa_rahaa
        kortin_uusi_saldo = self.maksukortti.saldo
        self.assertEqual(kassan_uusi_saldo, 100000)
        self.assertEqual(kortin_uusi_saldo, 100)