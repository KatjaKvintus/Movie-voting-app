# Testausdokumentti

Sovellusta on testattu automatisoiduilla unittesteillä ja manuaalisesti.


## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka ja luokat

Testauksesta vastaavat luokat on nimetty testauksen kohteena olevien luokkien mukaisesti. 

| luokka | testiluokka | 
| :----|:-----|
| Admin_User | Test_Admin_User |
| Admin_User_Repository | Test_Admin_User_Repository |
| App_User | Test_App_User |
| App_User_Repository | Test_App_User_Repository |
| Movie | Test_Movie |
| Movie_Repository | Test_Movie_Repository |


### Testauskattavuus

Käyttöliittymäkerrosta lukuunottamatta sovelluksen testauksen haarautumakattavuus on 

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.


### Asennus ja konfigurointi

Sovellus on kirjoitettu laitoksen fuksilaitteella, jonka käyttöjärjestelmänä on Ubuntu 20.04.5 LTS. Testaus on suoritettu samalla järjestelmällä.


### Toiminnallisuudet

Kaikki määrittelydokumentin ja käyttöohjeen listaamat toiminnallisuudet on käyty läpi ja testattu. Kaikkia niitä toiminnallisuuksia, joissa käyttäjältä pyydetään syötettä, on myös testattu virheellisillä syötteillä, kuten tyhjällä syötteellä, virheellisistä arvoista koostuvalla syötteellä sekä erikoismerkeistä koostuvilla syötteillä. 

## Sovellukseen jääneet laatuongelmat

Sovellus antaa käyttäjän kirjautumisen yhteydessä satunnaisesti seuraavan virheilmoituksen:

```bash
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc3 in position 0: invalid continuation byte
```

Virheilmoituksen juurisyytä ei ole pystytty selvittämään. On mahdollista, että virhe johtuu laitteessa käytetystä vanhentuneesta käyttöjätjestelmästä, jota koodari ei taikauskoisesti ole uskaltanut päivittää uudeksi ennen harjoitustyön palautusta. 

