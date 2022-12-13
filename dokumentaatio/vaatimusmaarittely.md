# Vaatimusmäärittely

## Sovelluksen tarkoitus

Tällä sovelluksella voi ehdottaa elokuvaa ja äänestää valitusta listasta elokuvaa viikoittaista leffailtaa varten. 

## Käyttäjät

Sovelluksella on kahdenlaisia käyttäjiä: 
Peruskäyttäjä: 
- voi ehdottaa elokuvaa seuraavaan äänestykseen - TEHTY
- voi äänestää yhtä listan elokuvista - TEHTY
- voi katsoa äänestyksen tilanteen
Pääkäyttäjä
- hyväksyy tai hylkää seuraavaan äänestykseen ehdotetun elokuvan 
- julkaisee listan jolta voi äänestää leffoja
- sulkee äänestyksen ja julkaisee valitun elokuvan

## Käyttöliittymäluonnos

![](kayttoliittyma-luonnos-versio-1.png)

Kuvasta poiketen sovellus toimii tekstikäyttäliittymällä, ei graafisella. Kuva kuitenkin havainnollistaa sovelluksen ominaisuuksia.

Sovelluksen käynnistyessä käyttäjällä on meljä vaihtoehtoa:
  [N] Create new user account 
  [L] Log in as returning user 
  [A] Log in as the admin user 
  [X] Close app

Käyttäjä valitsee sopivan vaihtoehdon antamalla sitä vastaavan kirjaimen []. Sovellus hyväksyy sekä ison että pienen kirjaimen. Sekä uusi käyttäjä
että jo aiemmin tilin luonut käyttäjä pääsevät tunnus-salasana -vaiheen jälkeen äänestämään elokuvaa. Admin-kirjautuminen antaa tarjolle admin-työkalut:
  [P]rint current voting list 
  [C]lear voting list 
  [S]et up a new votings list 
  [E]xit admin tools 

## Ennen kirjautumista

Sovelluksen käynnistyessä käyttäjällä on meljä vaihtoehtoa:
  [N] Create new user account
  [L] Log in as returning user
  [A] Log in as the admin user
  [X] Close app

- Käyttäjä voi luoda järjestelmään käyttäjätilin (käyttäjätunnuksen täytyy olla uniikki ja vähintään 3 merkkiä pitkä - TEHTY
- Järjestelmään kirjaudutaan tunnuksella ja salanalla. Jos tunnusta ei ole olemassa tai salasana on väärin, siitä tulee virheilmoitus. - TEHTY
- Admin-käyttäjälle on määritelty omat työkalut - TEHTY

## Kirjautumisen jälkeen

Käyttäjä:
  - Käyttäjällä on mahdollisuus äänestää elokuvaa - TEHTY
  - Käyttäjä voi ehdottaa uuttaa elokuvaa ensi viikon äänestykseen
  - Käyttäjä voi kirjautua ulos järjestelmästä - TEHTY

Admin:
  - Voi tyhjentää elokuvalistan - TEHTY
  - Voi asettaa uuden äänestyslistan 
  - Voi julkaista äänestyksen voittaneen elokuvan
  - voi hyväksyä käyttäjän elokuvaehdotuksen osaksi seuraavaa äänestyslistaa

## Jatkokehitysideoita

Perusversion jälkeen sovellukseen voisi lisätä mm. seuraavat ominaisuudet
- Mahdollisuus katsoa äänestystilanne ilman kirjautumista (ns. vieraskäyttäjä-status, apin käyttö ilman käyttäjätiliä)
- Käyttäjä: vaihtaa mielipidettä eli perua aiemman äänestyksen ja äänestää uudelleen
- Chat, jossa voi keskustella leffavalinnoista, ja pääkäyttäjälle editointioikeudet siihen
- Tilasto aiemmista äänestyksistä
- Mahdollisuus poistaa käyttäjätunnus (joko itse tai sitten pääkäyttäjä heittää käyttäjän ulos)
