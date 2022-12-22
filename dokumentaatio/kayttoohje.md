# Käyttöohje

Lataa projektin viimeisimmän releasen lähdekoodi valitsemalla Assets-osion alta Souce code.


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

Valikosta valitaan vaihtoehto kirjoittamalla halutun vaihtoehdon hakasuluilla [] merkitty kirjain (kirjaimet eivät näy tässä ohjeessa, koska GitHub hämmentyyhakasuluista). Sovellus hyväksyy sekä pienet että suuret kirjaimet.


## Käyttäjätilin luominen

Valitse käynnistysvalikosta C (Create new user account) ja anna vähintään kolmen merkin mittainen käyttäjätunnus. Jos tunnus on jo käytössä, sovellus huomauttaa siitä ja kehottaa keksimään uniikimman tunnuksen. Myös salasanan tulee olla vähintään 3 merkkiä pitkä. Sekä tunnus että salasana voivat sisältää kirjainten lisäksi myös numeroita ja erikoismerkkejä.


## Kirjautuminen: jo olemassa oleva käyttäjä

Valitse alkuvalikosta L (Log in as returning user) ja syötä pyydettäessä käyttäjätunnuksesi ja salasanasi. Jos olet unohtanut tunnuksesi tai salasanasi, niiden palauttamiseksi ei toistaiseksi ole olemassa sovelluksen sisäistä toimintoa. 


## Kirjautuminen: pääkäyttäjä

Valitse sovelluksen alkuvalikosta A (Log in as the admin user) ja syötä pyydettäessä käyttäjätunnuksesi ja salasanasi. 


## Toiminnot: peruskäyttäjä

Sisäänkirjautumisen jälkeen sovellus näyttää peruskäyttäjälle valikon, jossa on tarjolla seuraavat toiminnot:

- See movie voting list (Näytä elokuvien äänestyslista)
- Vote for a movie (Äänestä elokuvaa)
- Propose a movie for nex weeks vote (Ehdota elokuvaa seuraavan leffaillan äänestykseen)
- Exit app (Sulje sovellus)


