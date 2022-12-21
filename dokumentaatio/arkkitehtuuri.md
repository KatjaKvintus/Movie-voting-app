# Arkkitehtuurikuvaus

## Rakenne

### Koodin pakkausrakenne:

![](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/pakkausrakenne.jpg)



### Luokkakaavio:

![](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/luokkakaavio.jpg)

Ohjelman suoritys käynnistyy hakemiston juuressa olevasta tiedostosta index.py. Muu koodi on jaettu seuraaviin kokonaisuuksiin:
- entities (luokat AppUser, AdminUser ja Movie: uusien olioiden luominen)
- functionalities (luokka Movieservice: sisältää sovelluksen perustoiminnallisuudet, jotka keskittyvät elokuvaäänestyksen ympärille)
- repositories (AppUserRepository, AdminUserRepository, MovieRepository: tiedon pysyväistallennus ja hakeminen)


## Käyttöliittymä

Sovelluksessa on tekstikäyttöliittymä. Luokkia on 5:
-	AppUser (käsittelee käyttäjätilien toiminnot)
-	Movie (käsittelee leffoihin liittyvät toiminnot)
-	AppUserServices (käyttäjätilen oheismetodit)
-	MovieServices  (elokuvatoimintojen toiminnot)
-	AdminUserServices (admin-käyttäjien oheistoiminnot)
- AppUserRepository (käyttäjiin liittyvän tiedon pysyväistallennus)
- AdminUserRepository (admin-käyttäjiin liittyvän tiedon pysyväistallennus)
- MovieRepository (elokuviin liittyvän tiedon pysyväistallennus)

Kun käyttäjä avaa sovelluksen, hänellä on kolme vaihtoehtoa:
-	Luo uusi käyttäjätili (”Create new user account”)
-	Kirjaudu sisään olemassa olevana käyttäjänä (”Log in as returning user”)
-	Kirjaudu sisään admin-käyttäjänä (”Log in as admin user”)
-	sulje sovellus (”Close app”)

Kun uusi käyttäjä on luonut käyttäjätilin (uniikki käyttäjätunnus, kelvollinen salasana) tai vanha käyttäjä on kirjautunut sisään (käyttäjätunnus löytyy, salasana mätsää käyttäjätunnukseen), sovellus kertoo käyttäjälle äänestysstatuksen, joka on yksi seuraavista:
-	Äänestys on auki ja voit äänestää – tässä leffalista ja tämänhetkinen äänestystilanne
-	Äänestys on auki, mutta olet jo äänestänyt – tässä äänestystilanne
-	Äänestys on suljettu, mutta valittua elokuvaa ei ole vielä julkaistu
-	Äänestys on suljettu ja seuraava leffailta on xx.xx. klo xx ja leffana on xxx

Ylläolevista vaihtoehdoista riippuen käyttäjällä on käytössä seuraavat toiminnot:
-	Äänestä elokuvaa (”Vote for a movie”)
-	Ehdota elokuvaa seuraavaan äänestykseen (”Suggest a movie for next weeks vote”)
-	sulje sovellus (”Close app”)

Jos käyttäjä kirjautuu sovellukseen admin-käyttäjänä, hänellä on käytössään seuraavat vaihtoehdot:
-	(Näytä auki olevan äänestyksen elokuvalista (”Print current voting list”)
-	Tyhjennä äänestyslista (”Clear voting list”)
-	Katso seuraavaan äänestykseen ehdotetut elokuvat (”Read suggestions for next weeks movie voting”)
-	Aseta äänestyslista uutta äänestystä varten (”Set up a new votings list”)
-	Luo uusi admin-käyttäjätili (“Make new admin user account”)
-	Sulje äänestys (”Close voting”)
-	Julkaise voittajaelokuva (”Publish winner movie”)
-	Poistu admin-työkaluista (”Exit admin tools”)


## Sovelluslogiikka

Luokat AppUser ja AdminUser kuvaavat käyttäjiä ja käyttäjien toimintoja. Movie-luokka käsittelee elokuvien äänestyksen, äänestyslistojen luomisen ja uuden elokuvan ehdottamisen. MovieServices-luokka sisältää ne toiminnallisuudet, jotka keskittyvät elokuvaäänestyksen ympärille. Repositories-kokonaisuus vastaa tiedon pysyväistallennuksesta ja tiedon hakemisesta.


## Tietojen pysyväistallennus

### Tiedostot

Repositories-kokonaisuus vastaa tiedon pysyväistallennuksesta ja tiedon hakemisesta. Tiedot tallennetaan txt-tiedostoihin, joita sovellus lukee ja kirjoittaa. Jatkossa sovellusta voisi kehittää niin, että tietojen tallennus siirtyy pilvessa oleviin tietokantatauluihin.


## Päätoiminnallisuudet

### Uuden käyttäjän luominen

![](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/sekvenssikaavio_Creating%20new%20user%20account.jpg)


### Käyttäjän kirjautuminen

![](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/sekvenssikaavio_Existing%20user%20log%20in.jpg)


### Admin-käyttäjän kirjautuminen

![](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/sekvenssikaavio_Admin%20user%20log%20in.jpg)

### Uuden admin-käyttäjän luominen

![](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/sekvenssikaavio_Creating%20new%20admin%20user%20account.jpg)


### Elokuvan äänestäminen

![](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/sekvenssikaavio_Voting%20for%20a%20movie.jpg)

### Elokuvan ehdottaminen seuraavaa äänestystä varten

![](https://github.com/KatjaKvintus/ot-harjoitustyo/blob/master/dokumentaatio/sekvenssikaavio_Suggesting%20a%20movie.jpg)


