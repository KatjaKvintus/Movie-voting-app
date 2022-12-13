# Movie voting app - leffaillan leffan äänestysappi
Ohjelmistotekniikka, harjoitustyö

Tällä sovelluksella voi ehdottaa elokuvaa ja äänestää valitusta listasta elokuvaa viikoittaista leffailtaa varten. Apin käyttöä varten tulee luoda käyttäjätili. Peruskäyttäjä voi äänestää elokuvaa valmiista listasta ja ehdottaa haluamaansa elokuvaa seuraavaa äänestystä varten. Yksi tai useampi käyttäjä voi olla pääkäyttäjä, jolla on oikeus asettaa äänestettävät elokuvat ja sulkea äänestys. 


### Dokumentaatio

[Tuntikirjanpito](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Vaatimusmäärittely](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Changelog](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Release](https://github.com/KatjaKvintus/ot-harjoitustyo/releases/tag/viikko6)

[Käyttöohje](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)


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
