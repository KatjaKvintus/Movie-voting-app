import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):

    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    # Kortin saldo alussa oikein
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    # Rahan lataaminen kasvattaa saldoa oikein
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")

    # Saldo vähenee oikein, jos rahaa on tarpeeksi 
    def test_saldo_vahenee_oikein_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(300)
        self.assertEqual(str(self.maksukortti),  "Kortilla on rahaa 7.00 euroa")

    # Saldo ei muutu, jos rahaa ei ole tarpeeksi
    def test_saldo_ei_muutu_jos_rahat_ei_riitä(self):
        self.maksukortti.ota_rahaa(1700)
        self.assertEqual(str(self.maksukortti),  "Kortilla on rahaa 10.00 euroa")

    # Rahan ottaminen -metodi palauttaa True, jos rahat riittivät
    def test_rahan_ottaminen_palauttaa_True_jos_rahat_riittavat(self):
        result = self.maksukortti.ota_rahaa(700)
        self.assertTrue(result)

    # Rahan ottaminen -metodi palauttaa True False, jos rahat eivät riitä
    def test_rahan_ottaminen_palauttaa_False_jos_rahat_ei_riita(self):
        result = self.maksukortti.ota_rahaa(1100)
        self.assertFalse(result)
    
