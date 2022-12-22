
# Changelog

### Viikko 3

- User-luokan rakentaminen on aloitettu
- User-luokan testien kirjoittaminen on aloitettu

### Viikko 4

- Muutoksia käyttöliittymään: lisätty äänestys-toiminto (kesken) ja leffan ehdotus -toiminto (kesken)
- Tietojen tallennus siirtyy ohjelman sisäisestä tallennuksesta tiedostoon (myöhemmin pilvitiedostoon) - kesken


### Viikko 5

- Ohjelmatiedostot on jaettu järkevämmin eri alihakemistojen alle src-kansiossa
- Siirtymä tekstikäyttöliittymästä graafiseen: login-näkymän ja äänestys-näkymän runko on rakennettu, mutta toiminnallisuudet ovat hajalla
- Käyttäjätietojen tallennus ei toistaiseksi toimi


### Viikko 6

- Pitkän taistelun ja säätämisen jälkeen totesin, että en todennäköisesti ehdi saada graafista käyttöliittymää toimimaan. Joten poistin sen ja aloitin (melkein) alkusta. Tästä tulee nyt tekstiköyttöliittymäappi. (Sinne meni graafisesta UI:sta saatavat pisteet, mutta valmis on parempi kuin täydellinen.)
- Uusia toimintoja: 
	* uuden käyttäjän luominen ja tallentaminen onnistuu
	* vanhan käyttäjän kirjautuminen onnistuu
	* käyttöliittymällä on toimiva runko (vaatii vielä hienosäätöä)
	* admin-käyttäjä on määritelty
	* adminille on määritelty omat toiminnot, jotka edellyttävät admin-tunnuksia.
- Keskeneräisiä toimintoja: 
	* Movie-luokan toiminnot (elokuvan äänestäminen, elokuvalistan tulostus)
	* osa admin-työkaluista (elokuvalistan kokoaminen)
- Puuttuvia toimintoja/ominaisuuksia: 
	* Uuden elokuvan ehdottaminen
	* Try - except -virheenkäsittely kaikkialle, jossa niitä tarvitaan
	* suurinpiirtein KAIKKI testit
	* Aika paljon dokumentaatiosta
	* tavallisen käyttäjän voisi korottaa adminiksi

### Viikko 7

- Repository-luokkien luominen tiedon pysyväistallennusta varten tehdyille funktioille
- Testien kirjoitus
- Käyttöliitymän hiontaa
- Elokuvan ehdotustoiminto
- Movie-luokan toiminnot
- Arkkitehtuurikuvauksen kirjoittaminen
- Sekvenssikaavioiden piirtoa uusiksi muutosten jälkeen
