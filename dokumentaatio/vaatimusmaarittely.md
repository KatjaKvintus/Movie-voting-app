# Vaatimusmäärittely

## Sovelluksen tarkoitus

Tällä sovelluksella voi ehdottaa elokuvaa ja äänestää valitusta listasta elokuvaa viikoittaista leffailtaa varten. 

## Käyttäjät

Sovelluksella on kahdenlaisia käyttäjiä: 
Peruskäyttäjä: 
- voi ehdottaa elokuvaa seuraavaan äänestykseen
- voi äänestää yhtä listan elokuvista
- voi katsoa äänestyksen tilanteen
Pääkäyttäjä
- hyväksyy tai hylkää seuraavaan äänestykseen ehdotetun elokuvan 
- julkaisee listan jolta voi äänestää leffoja
- sulkee äänestyksen ja julkaisee valitun elokuvan

## Käyttöliittymäluonnos

![](kayttoliittyma-luonnos-versio-1.png)

Sovellus koostuu viidestä eri näkymästä, joista yksi näkyy vain pääkäyttäjälle. Aloitusnäytössä on kaksi mahdollisuutta: kirjaudu sisään tai luo uusi käyttäjätili. Molemmista pääsee välivaiheen kautta varsinaiseen sovellusnäkymään, jossa näkyy ylimpänä käyttäjän status (onko jo äänestänyt menossa olevassa äänestyksessä vai ei), alareunassa mahdollisuus ehdottaa uutta leffaa seuraavaan äänestykseen, ja keskellä
ikkuna, jossa näkyy yksi kolmesta vaihtoehdosta:
- Äänestysvaihtoehdot ja äänestysnapit, jos käyttäjä ei ole vielä äänestänyt, ja äänestys on auki
- Äänestystilanne, jos käyttäjä on jo äänestänyt ja äänestys on auki
- Äänestyksen voittanut elokuva, jos äänestys on loppunut ja leffavaihtoehto valittu

## Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään käyttäjätilin (käyttäjätunnuksen täytyy olla uniikki ja vähintään 5 merkkiä pitkä, ja salasanan täytyy olla vähintään 5 merkkiä pitkä)
- Järjestelmään kirjaudutaan tunnuksella ja salanalla. Jos tunnusta ei ole olemassa tai salasana on väärin, siitä tulee virheilmoitus.

## Kirjautumisen jälkeen

* Käyttäjä näkee statuksen, joka on yksi seuraavista
- Äänestysvaihtoehdot ja äänestysnapit, jos käyttäjä ei ole vielä äänestänyt, ja äänestys on auki
- Äänestystilanne, jos käyttäjä on jo äänestänyt ja äänestys on auki
- Äänestyksen voittanut elokuva, jos äänestys on loppunut ja leffavaihtoehto valittu
* Käyttäjä voi ehdottaa uutta elokuvaa (pääkäyttäjä hyväksyy)
* Käyttäjä voi äänestää elokuvaa, jos äänestys on auki eikä hän ole vielä äänestänyt
* Käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita

Perusversion jälkeen sovellukseen voisi lisätä mm. seuraavat ominaisuudet
- Mahdollisuus katsoa äänestystilanne ilman kirjautumista (ns. vieraskäyttäjä-status, apin käyttö ilman käyttäjätiliä)
- Käyttäjä: vaihtaa mielipidettä eli perua aiemman äänestyksen ja äänestää uudelleen
- Chat, jossa voi keskustella leffavalinnoista, ja pääkäyttäjälle editointioikeudet siihen
- Tilasto aiemmista äänestyksistä
- Mahdollisuus poistaa käyttäjätunnus (joko itse tai sitten pääkäyttäjä heittää käyttäjän ulos)
