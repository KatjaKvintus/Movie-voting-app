# Käyttöohje

Lataa projektin viimeisimmän releasen lähdekoodi valitsemalla Assets-osion alta 'Source code'.



## Ohjelman käynnistäminen

Ennen ohjelman ensimmäistä käynnistyskertaa:
- asenna riippuvuudet komennolla 'poetry install'
- Mieti valmiiksi vähintään 3 kirjaimen pituinen käyttäjätunnus

Ohjelman voi käynnistää komennolla:
poetry run invoke start

Käynnistettäessä sovellus tarjoaa valikon, jossa on tarjolla seuraavat vaihtoehdot (suomenkieliset käännökset suluissa):
- Create new user account (luo uusi käyttäjätili)
- Log in as returning user  (Kirjaudu sisään jo olemassaolevalla käyttäjätunnuksella)
- Log in as the admin user (Kirjaudu sisään pääkäyttäjänä)
- Close app (Sulje sovellus)

Valikosta valitaan vaihtoehto kirjoittamalla halutun vaihtoehdon hakasuluilla [] merkitty kirjain (kirjaimet eivät näy tässä ohjeessa, koska GitHub hämmentyy hakasuluista). Sovellus hyväksyy sekä pienet että suuret kirjaimet.



## Käyttäjätilin luominen

Valitse käynnistysvalikosta C ("Create new user account") ja anna vähintään kolmen merkin mittainen käyttäjätunnus. Jos tunnus on jo käytössä, sovellus huomauttaa siitä ja kehottaa keksimään uniikimman tunnuksen. Myös salasanan tulee olla vähintään 3 merkkiä pitkä. Sekä tunnus että salasana voivat sisältää kirjainten lisäksi myös numeroita ja erikoismerkkejä.

Tiedossa oleva ongelma: käyttäjätilin luomista ei voi keskeyttää muutoin kuin katkaisemalla sovelluksen suorituksen. 


## Kirjautuminen: jo olemassa oleva käyttäjä

Valitse alkuvalikosta L ("Log in as returning user") ja syötä pyydettäessä käyttäjätunnuksesi ja salasanasi. Jos olet unohtanut tunnuksesi tai salasanasi, niiden palauttamiseksi ei toistaiseksi ole olemassa sovelluksen sisäistä toimintoa. 

Tiedossa oleva ongelma: kirjautumistoimintoa ei voi keskeyttää muutoin kuin katkaisemalla sovelluksen suorituksen. 


## Kirjautuminen: pääkäyttäjä

Valitse sovelluksen alkuvalikosta A ("Log in as the admin user") ja syötä pyydettäessä käyttäjätunnuksesi ja salasanasi. 

Tiedossa oleva ongelma: kirjautumistoimintoa ei voi keskeyttää muutoin kuin katkaisemalla sovelluksen suorituksen. 


## Toiminnot: peruskäyttäjä

Sisäänkirjautumisen jälkeen sovellus kertoo käyttäjälle sovelluksen tilan, joka on yksi kolmesta vaihtoehdosta:
- "Voting is open" = äänestys on auki
- "Voting is closed" = äänestys on suljettu, mutta admin ei ole vielä julkaissut äänestyksen voittanutta elokuvaa
- "The voting has ended. Next movie night movie is '{movie_name}'!  = äänestys on suljettu ja voittajaelokuva on julkaistu

Seuraavaksi sovellus näyttää peruskäyttäjälle valikon, jossa on tarjolla seuraavat toiminnot:

- See movie voting list (Näytä elokuvien äänestyslista)
- Vote for a movie (Äänestä elokuvaa)
- Propose a movie for nex weeks vote (Ehdota elokuvaa seuraavan leffaillan äänestykseen)
- Exit app (Sulje sovellus)

Kaksi ensimmäistä vaihtoehtoa näytetään vain, jos äänestys on auki.

Käyttäjä voi katsoa äänestyslistan valitsemalla ensin valikosta "See movie voting list". Sovellus tulostaa listan näytölle ja antaa sitten valikon uudestaan, jonka jälkeen käyttäjä voi päättää, haluaako hän äänestää elokuvaa tai ehdottaa elokuvaa seuraavaan äänestykseen.

Käyttäjä voi äänestää elokuvaa valitsemalla ensin "Vote for a movie" valikosta, ja syöttämällä sitten elokuvan numeron sovelluksen näyttämästä listasta.

Käyttäjä voi ehdottaa elokuvaa valitsemalla ensin "Propose a movie for nex weeks vote" valikosta ja antamalla syötteenä haluamansa elokuvan nimen ja ilmestymisvuoden.

"Close app" -toiminnon valitsemalla sovellus suljetaan.


## Toiminnot: pääkäyttäjä (admin)

Sisäänkirjautumisen jälkeen sovellus näyttää käyttäjälle valikon, jossa on seuraavat vaihtoehdot:
- Print current voting list (tulosta tämänhetkisen äänestyksen elokuvalista)
- Clear voting list (tyhjennä elokuvalista)
- Read suggestions for next weeks movie voting (lue ehdotukset seuraavaa äänestystä varten)
- Set up a new votings list (Luo uusi äänestys)
- Check voting status (Tarkista äänestyksen tilanne)
- Make new admin user account (Luo uusi pääjäyttäjätili)
- Exit admin tools (poistu pääkäyttäjätyökaluista)

Pääkäyttäjälla voi valita toiminnon yllä olevasta valikosta syöttämällä haluaamansa vaihtoehtoa vastaavan kirjaimen. 

"Print current voting list" tulostaa näytölle tämänhetkisen äänestettävien elokuvien listan, jos äänestys on auki. Jos ei ole, sovellus kertoo sen.

"Clear voting list" -toiminto sulkee äänestyksen, tyhjentää äänestettävien elokuvien listan, asettaa äänestyksen statuksesi "closed" ja poistaa tähän äänestykseen liittyvät äänet.

"Read suggestions for next weeks movie voting" -toiminto näyttää käyttäjien syöttämät elokuvaehdotukset. 

"Set up a new votings list" -toiminto tarkistaa ensin, onko ehdotukset-listalla ehdotuksia, ja jos on, kysyy pääkäyttäjältä, haluaako hän nähdä ne ensin ennen uuden äänestyslistan asetusta. Jos pääkäyttäjä katsoo listan, sovellus kysyy listan tuloksen jälkeen, haluaako pääkäyttäjä lisätä listalta ehdotuksia suoraan äänestettävien elokuvien listaan. Tämän jälkeen pääkäyttäjä voi lisätä äänestyslistaan uusia elokuvia niin, että elokuvia on tasan neljä.

"Check voting status" -toiminto kertoo pääkäyttäjälle, mikä elokuva on tällä hetkellä saanut eniten ääniä, ja kysyy, haluaako pääkäyttäjä sulkea äänestyksen ja julistaa voittajan. Jos pääkäyttäjä vastaa "yes" (kyllä), sovellus asettaa äänestyksen statukseksi "The voting has ended. Next movie night movie is '{movie_name}'!", tyhjentää annettujen äänien listan ja tyhjentää äänestettävien elokuvien listan.

Jos ääniä ei ole vielä annettu, sovellus kertoo tämän.

"Make new admin user account" -toiminnolla pääkäyttäjä voi luoda toisen pääkäyttäjän. Jos annettu tunnus on jo käytössä, sovellus huomauttaa siitä ja kehottaa keksimään uniikimman tunnuksen. Myös salasanan tulee olla vähintään 3 merkkiä pitkä. Sekä tunnus että salasana voivat sisältää kirjainten lisäksi myös numeroita ja erikoismerkkejä.

"Exit admin tools" -toiminto palauttaa pääkäyttäjän takaisin sovelluksen alkuvalikkoon. 
