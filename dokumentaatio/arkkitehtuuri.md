# Arkkitehtuurikuvaus

## Rakenne

### Koodin pakkausrakenne

Koodin pakkausrakenne on seuraava:


![](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/Kuvat/pakkausrakenne.jpg)


Pakkaus repositories vastaa tiedon hakemisesta ja tallennuksesta, entities käyttäjä- ja elokuvaobjektien toiminnallisuudesta ja services elokuva-luokan palveluista.


### Luokkakaavio:

![](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/Kuvat/luokkakaavio.jpg)

Ohjelman suoritys käynnistyy hakemiston juuressa olevasta tiedostosta index.py. Muu koodi on jaettu seuraaviin kokonaisuuksiin:
- entities (luokat App_User, Admin_User ja Movie: uusien olioiden luominen ja niihin liittyvät toiminnallisuudet)
- services (luokka Movieservice: sisältää sovelluksen perustoiminnallisuudet, jotka keskittyvät elokuvaäänestyksen ympärille)
- repositories (App_User_Repository, Admin_User_Repository, Movie_Repository: tiedon pysyväistallennus ja hakeminen)


## Käyttöliittymä

[Alkuperäiset suunnitelmat graafisesta käyttöliittymästä](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/Kuvat/K%C3%A4ytt%C3%B6liittym%C3%A4_alustava%20suunnitelma.JPG) kaatuivat koodarin taitotasoon. Alla oleva kaavio pyrkii esittämään sovelluksen päätoiminnallisuudet tekstikäyttöliittymänä:

![](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/Kuvat/K%C3%A4ytt%C3%B6liittym%C3%A4_final.JPG)


Luokkia on 7:
-	App_User (käsittelee käyttäjätilien toiminnot)
-	Admin_user (käsittelee pääkäyttäjätileihin liittyvät toiminnot)
-	Movie (käsittelee leffoihin liittyvät toiminnot)
-	Movie_Services  (elokuvatoimintojen toiminnot)
- App_User_Repository (käyttäjiin liittyvän tiedon pysyväistallennus)
- Admin_User_Repository (admin-käyttäjiin liittyvän tiedon pysyväistallennus)
- Movie_Repository (elokuviin liittyvän tiedon pysyväistallennus)

Kun käyttäjä avaa sovelluksen, hänellä on kolme vaihtoehtoa:
-	Luo uusi käyttäjätili (”Create new user account”)
-	Kirjaudu sisään olemassa olevana käyttäjänä (”Log in as returning user”)
-	Kirjaudu sisään admin-käyttäjänä (”Log in as admin user”)
-	sulje sovellus (”Close app”)

Kun uusi käyttäjä on luonut käyttäjätilin (uniikki käyttäjätunnus, kelvollinen salasana) tai vanha käyttäjä on kirjautunut sisään (käyttäjätunnus löytyy, salasana mätsää käyttäjätunnukseen), sovellus kertoo käyttäjälle äänestysstatuksen, joka on yksi seuraavista:
-	Äänestys on auki ja voit äänestää – tässä leffalista
-	Äänestys on suljettu, mutta valittua elokuvaa ei ole vielä julkaistu
-	Äänestys on suljettu ja seuraava leffaillan leffa on {elokuvan_nimi}

Ylläolevista vaihtoehdoista riippuen käyttäjällä on käytössä seuraavat toiminnot:
-	Äänestä elokuvaa (”Vote for a movie”)
-	Ehdota elokuvaa seuraavaan äänestykseen (”Suggest a movie for next weeks vote”)
-	sulje sovellus (”Close app”)

Jos käyttäjä kirjautuu sovellukseen admin-käyttäjänä, hänellä on käytössään seuraavat vaihtoehdot:
-	Näytä auki olevan äänestyksen elokuvalista (”Print current voting list”)
-	Tyhjennä äänestyslista (”Clear voting list”)
-	Katso seuraavaan äänestykseen ehdotetut elokuvat (”Read suggestions for next weeks movie voting”)
-	Aseta äänestyslista uutta äänestystä varten (”Set up a new votings list”)
-	Tarkista, mikä elokuva johtaa äänestystä ("Check voting status ")
-	Luo uusi admin-käyttäjätili (“Make new admin user account”)
-	Poistu admin-työkaluista (”Exit admin tools”)


## Sovelluslogiikka

Luokat App_User ja Admin_User kuvaavat käyttäjiä (tavallinen käyttjä, pääkäyttäjä) ja käyttäjien toimintoja. Movie-luokka käsittelee elokuvien äänestyksen, äänestyslistojen luomisen ja uuden elokuvan ehdottamisen. MovieS_ervices-luokka sisältää ne toiminnallisuudet, jotka keskittyvät elokuvaäänestyksen ympärille. Repositories-kokonaisuus vastaa tiedon pysyväistallennuksesta ja tiedon hakemisesta.


## Tietojen pysyväistallennus

### Tiedostot

Repositories-kokonaisuus vastaa tiedon pysyväistallennuksesta ja tiedon hakemisesta. Tiedot tallennetaan txt-tiedostoihin, joita sovellus lukee ja kirjoittaa. Jatkossa sovellusta voisi kehittää niin, että tietojen tallennus siirtyy pilvessa oleviin tietokantatauluihin.


## Päätoiminnallisuudet

### Uuden käyttäjän luominen

Sovelluksen aloitusvalikosta valitaan "Create new user account", jonka jälkeen käyttäjä antaa syötteenä halutun käyttäjätunnuksen ja salasanan. Sovellus tarkistaa, ettei käyttäjätunnus ole jo käytössä, ja että sekä käyttäjätunnus että salasana ovat vähintään 3 merkin mittaisia. Tämän jälkeen sovellus näyttää käyttäjälle toimintovalikon (movie menu). 

![](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/Kuvat/sekvenssikaavio_Creating%20new%20user%20account.jpg)


### Käyttäjän kirjautuminen

Sovelluksen aloitusvalikosta valitaan "Log in as returning user", jonka jälkeen käyttäjä antaa käyttäjätunnuksen ja salasanan. Sovellus tarkistaa, että käyttäjätunnus on varmasti jo rekisteröity, ja että käyttäjätunnus ja salasana vastaavat sovelluksen muistissa olevia. Tämän jälkeen sovellus näyttää käyttäjälle toimintovalikon (movie menu). 

![](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/Kuvat/sekvenssikaavio_Existing%20user%20log%20in.jpg)


### Admin-käyttäjän kirjautuminen

Sovelluksen aloitusvalikosta valitaan Log in as the admin user, jonka jälkeen käyttäjä antaa käyttäjätunnuksen ja salasanan. Sovellus tarkistaa, että käyttäjätunnus on varmasti jo rekisteröity, ja että käyttäjätunnus ja salasana vastaavat sovelluksen muistissa olevia. Tämän jälkeen sovellus näyttää käyttäjälle pääkäyttäjän toimintovalikon (admin menu). 

![](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/Kuvat/sekvenssikaavio_Admin%20user%20log%20in.jpg)


### Uuden admin-käyttäjän luominen

Pääkäyttäjä kirjautuu sovelluksen aloitustavalikosta pääkäyttäjänä (ks. ed. kohta) ja valitsee admin-valikosta "Create new admin user". Sen jälkeen käyttäjä antaa syötteenä halutun admin-käyttäjätunnuksen ja admin-salasanan. Sovellus tarkistaa, ettei käyttäjätunnus ole jo käytössä, ja että sekä käyttäjätunnus että salasana ovat vähintään 3 merkin mittaisia. Tämän jälkeen sovellus näyttää käyttäjälle taas pääkäyttäjän toimintovalikon (admin menu).

![](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/Kuvat/sekvenssikaavio_Creating%20new%20admin%20user%20account.jpg)


### Elokuvan äänestäminen

Käyttäjä saapuu toimintovalikkoon (movie menu) ja jos äänestys on auki, sovellus tarjoaa mahdollisuutta äänestää. Käyttäjä valitsee toimintovalikosta toiminnon "Vote for a movie", jonka jälkeen sovellus näyttää numeroidun listanelokuvista. Käyttäjä valitsee haluamansa elokuvan antamalla syötteenä elokuvan numeron. Sovellus tallentaa äänen tiedostoon.

![](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/Kuvat/sekvenssikaavio_Voting%20for%20a%20movie.jpg)


### Elokuvan ehdottaminen seuraavaa äänestystä varten

Käyttäjä saapuu toimintovalikkoon (movie menu) ja valitsee toimintovalikosta toiminnon "Suggest a movie", jonka jälkeen sovellus pyytää syötteenä elokuvan nimen ja julkaisuvuoden. Sovellus tallentaa ehdotuksen tiedostoon.

![](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/Kuvat/sekvenssikaavio_Suggesting%20a%20movie.jpg)


## Ohjelman rakenteeseen jääneet heikkoudet


### Käyttöliittymä

Sovelluksen käytettävyys parantuisi heti, jos sen päivittäisi graafiseen käyttöliittymään. Tämä tulisikin pyrkiä tekemään versioon 2.0.

Sovelluksesta puuttuu myös funktio, joka laskisi kunkin elokuvan saamat äänet ja esittäisi äänestystilanteen listana, josta näkisi äänten prosentuaalisen jakauman.



### Tietojen tallennus

Tiedot tallennetaan tällä hetkellä paikallisesti tekstitiedostoon, jonka seurauksena yksi äänestävä ryhmä voi äänestää vain yhdellä laitteella vuorotellen. Versioon 2.0. Tietojen tallennus tulisi siirtä pilveen ja siirtyä tekstitiedostoista tietokantatauluihin.

Sovellus ei myöskään tallenna elokuvan äänestämisen yhteydessä äänestäjän käyttäjätunnusta, jonka seurauksena yksittäinen käyttäjä voi halutessaan äänestää monta kertaa.


### Koodi

Tämän ensimmäisen version koodissa on paljon turhaa toistoa. Sen sijaan, että jokaiselle luettavalle ja muokattavalle txt-tiedostolle on omat funktionsa päivitystä ja tyhjennystä varten, olisi järkevää tehdä kolme funktiota: yksi tiedoston lukemiseen, toinen tiedon lisäämiseen tiedoston loppuun ja kolmas päällekirjoittamiseen. Kukin funktio saisi parametrina muokkauksen kohteen ja tarvittaessa myös lisättävän/päällekirjoitettavan tiedon.

Koodia kirjoitettaessa ei ole myöskään kiinnitetty huomiota funktioiden ja datan hakemisen nopeuteen, joka voisi nousta ongelmaksi jos äänestävä ryhmä on iso.

Pylint antaa koodille varsin heikon arvosanan 5.12/10, joten parannettavaa löytyy. 
