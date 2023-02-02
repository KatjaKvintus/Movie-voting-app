# Movie voting app - leffaillan leffan äänestysappi
_TKT20002 Ohjelmistotekniikka, harjoitustyö (Helsingin yliopisto, tietojenkäsittelytieteen laitos, syksy 2022)_

Sovelluksen käyttöä varten tulee luoda käyttäjätili. Peruskäyttäjä voi katsoa elokuvalistan, äänestää elokuvaa ja ehdottaa haluamaansa elokuvaa seuraavaa äänestystä varten. Yksi tai useampi käyttäjä voi olla pääkäyttäjä, jolla on oikeus asettaa äänestettävät elokuvat, luoda uusia admin-käyttäjiä ja sulkea äänestys. 


## Huomioita sovelluksesta

Tämä on ensimmäinen tekemäni harjoitustyö ja siinä on useita perustavanlaatuisia ongelmia:
- Tiedot tallennetaan paikallisesti, eli sovellusta käyttävä ryhmä joutuu käyttämään sitä yhdeltä tietokoneelta
- Sovelluksesta puuttuu toiminto, jolla luodaan admin-käyttäjä. Ensimmäinen pääkäyttäjä joutuu aloittamaan käytön valmiiksi luoduilla tunnuksilla (käyttäjätunnus: admin, salasana: supersecretpassword).
- Koodissa on liikaa toisteisuutta (mm. useita eri funktioita tiedon tallentamiseen tiedostoon, kun järkevämpää olisi yksi funktio, joka saisi parametreina tiedoston johon kirjoitetaan, kirjoitettavan datan sekä tiedon siitä, ylikirjoitetaanko data vai lisätäänkö tiedostossa jo olevan datan jatkeeksi). 
- Sovellukselle kirjoitetut testit ovat puutteellisia ja kattavat vain 23 % tämänhetkisestä koodista


## Python-versio

Sovellus on kirjoitettu Python-ohjelmointikielellä ja sen toiminta on testattu Python-versiolla 3.8.10. Vanhempien tai uudempien versioiden kanssa saattaa ilmetä yllättäviä ongelmia.

Python-version voi tarkistaa seuraavalla komennolla:

```bash
python3 --version
``` 


### Dokumentaatio

- [Käyttöohje](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Changelog](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)
- [Tuntikirjanpito](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)


### Release

[Final release](https://github.com/KatjaKvintus/movie-voting-app/releases/tag/viikko7)


Aiemmat:
- [Release 1](https://github.com/KatjaKvintus/ot-harjoitustyo/releases/tag/viikko5)
- [Release 2](https://github.com/KatjaKvintus/ot-harjoitustyo/releases/tag/viikko6)


### Asennus

1. Asenna riippuvuudet komennolla
```bash
poetry install
```

## Komentorivitoiminnot

### Ohjelman suoritus

Ohjelman voi käynnistää kommennolla 

```bash
poetry run invoke start
```


### Testaus

Testit voi ajaa toiminnolla 

```bash
poetry run invoke test
```


### Testikattavuus

Testikattavuusraportin ajaminen:

```bash
poetry run invoke coverage-report
```


### Pylint

Tiedoston .pylintrc määrittelemät tarkastukset voi suorittaa komennolla

```bash
poetry run invoke link
```
