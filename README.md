# Movie voting app - leffaillan leffan äänestysappi
Ohjelmistotekniikka, harjoitustyö

Tällä sovelluksella voi ehdottaa elokuvaa ja äänestää valitusta listasta elokuvaa viikoittaista leffailtaa varten. Apin käyttöä varten tulee luoda käyttäjätili. Peruskäyttäjä voi äänestää elokuvaa valmiista listasta ja ehdottaa haluamaansa elokuvaa seuraavaa äänestystä varten. Yksi tai useampi käyttäjä voi olla pääkäyttäjä, jolla on oikeus asettaa äänestettävät elokuvat ja sulkea äänestys. 

HUOM: Viimeisimpien korjausyritysten jälkeen sovellus _ei toimi_: se ei tallenna tietoja eikä päästä käyttäjää eteenpäin login-ikkunasta. 


### Dokumentaatio

[Tuntikirjanpito](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
[Vaatimusmäärittely](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
[Changelog](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
[Arkkitehtuuri](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
[Release](https://github.com/KatjaKvintus/ot-harjoitustyo/releases/tag/viikko5)


## Komentorivitoiminnot

### Ohjelman suoritus

Ohjelman voi käynnistää kommennolla 

```bash
poetry run invoke start
```


### Testaus

Testit voi ajaa toiminnolla 

```bash
poetry run invoke start
```


### Testikattavuus

Testikattavuusraportin ajaminen:

```bash
poetry run invoke coverage-report
```


### Pylint

Tiedoston .pylintrc määrittelemät tarkastukset voi suorittaa komennolla.

```bash
poetry run invoke link
```
