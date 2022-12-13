# Käyttöohje

Lataa projektin viimeisimmän releasen lähdekoodi valitsemalla Assets-osion alta Souce code.


## Ohjelman käynnistäminen

Ennen ohjelman ensimmäistä käynnistyskertaa:
- asenna riippuvuudet komennolla 'poetry install'
- Mieti valmiiksi vähintään 3 kirjaimen pituinen käyttäjätunnus

Ohjelman voi käynnistää komennolla:
poetry run invoke start

## Kirjautuminen: uusi tai palaava käyttäjä

Käynnistettäessä sovellus tarjoaa valikon, jossa on tarjolla seuraavat vaihtoehdot:
  [N] Create new user account
  [L] Log in as returning user 
  [A] Log in as the admin user
  [X] Close app

Valikosta valitaan vaihtoehto kirjoittamalla halutun vaihtoehdon hakasuluilla [] merkitty kirjain. Ohjelma hyväksyy sekä pienet että suuret kirjaimet.

Uusi käyttäjätili luodaan valitsemalla N ja aiemmin tilin luonut käyttäjä valitsee sisäänkirjautumiseen L:n.

Kun uusi käyttäjä on antanut tarpeeksi pitkän ja uniikin käyttäjätunnuksen, jota muilla apin käyttäjillä ei ole vielä käytössä, tai vanha käyttäjä on kirjautunut sisään aiemmin asettamallaan tunnuksella ja salasanalla, appi kysyy, haluaako käyttäjä äänestää elokuvaa. Kysymykseen vastataan kirjaimella: Y = yes , N = no. Y-valinta näyttää elokuvalistan, jossa on 4 admin-käyttäjän asettamaa elokuvaa. Käyttäjä voi äänestää suosikkiaan antamalla elokuvan numeron (1-4).
