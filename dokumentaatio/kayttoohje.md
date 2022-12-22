# Käyttöohje

Lataa projektin viimeisimmän releasen lähdekoodi valitsemalla Assets-osion alta Souce code.


## Ohjelman käynnistäminen

Ennen ohjelman ensimmäistä käynnistyskertaa:
- asenna riippuvuudet komennolla 'poetry install'
- Mieti valmiiksi vähintään 3 kirjaimen pituinen käyttäjätunnus

Ohjelman voi käynnistää komennolla:
poetry run invoke start

Käynnistettäessä sovellus tarjoaa valikon, jossa on tarjolla seuraavat vaihtoehdot:
- Create new user account
- Log in as returning user 
- Log in as the admin user
- Close app

Valikosta valitaan vaihtoehto kirjoittamalla halutun vaihtoehdon hakasuluilla [] merkitty kirjain (kirjaimet eivät näy tässä ohjeessa, koska GitHub hämmentyyhakasuluista). Sovellus hyväksyy sekä pienet että suuret kirjaimet.


## Käyttäjätilin luominen

Valitse käynnistysvalikosta C ja anna vähintään kolmen merkin mittainen käyttäjätunnus. Jos tunnus on jo käytössä, sovellus huomauttaa siitä ja kehottaa keksimään uniikimman tunnuksen. Myös salasanan tulee olla vähintään 3 merkkiä pitkä. Sekä tunnus että salasana voivat sisältää kirjainten lisäksi myös numeroita ja erikoismerkkejä.


## Kirjautuminen: jo olemassa oleva käyttäjä

Valitse alkuvalikosta L ja syötä pyydettäessä käyttäjätunnuksesi ja salasanasi. 


## Kirjautuminen: pääkäyttäjä

Valitse sovelluksen alkuvalikosta A ja syötä pyydettäessä käyttäjätunnuksesi ja salasanasi. 


## Toiminnot: peruskäyttäjä

Sisäänkirjautumisen jälkeen sovellus näyttää peruskäyttäjälle valikon, jossa on tarjolla seuraavat toiminnot:

Kun uusi käyttäjä on antanut tarpeeksi pitkän ja uniikin käyttäjätunnuksen, jota muilla apin käyttäjillä ei ole vielä käytössä, tai vanha käyttäjä on kirjautunut sisään aiemmin asettamallaan tunnuksella ja salasanalla, appi kysyy, haluaako käyttäjä äänestää elokuvaa. Kysymykseen vastataan kirjaimella: Y = yes , N = no. Y-valinta näyttää elokuvalistan, jossa on 4 admin-käyttäjän asettamaa elokuvaa. Käyttäjä voi äänestää suosikkiaan antamalla elokuvan numeron (1-4).
