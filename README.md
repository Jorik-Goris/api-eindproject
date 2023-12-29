
# Eindproject API development - Jorik Goris

Deze repository bevat de eindopdracht voor het vak API development.

## Thema

Deze API bevat een task management systeem dat het toelaat om verschillende tasks aan te maken voor gebruikers. Deze tasks hebben titels, descriptions, due dates, categories, owners, en een boolean die aanduid of ze al dan niet afgewerkt zijn.

Volgende endpoints zijn aanwezig:

![all_endpoints](https://github.com/Jorik-Goris/api-eindproject/assets/95848835/e3e0e212-beeb-4091-ae4d-564176682941)


## Demo

Hier volgt een demonstratie van alle endpoints in Postman.

### OAuth user aanmaken en authenticeren

![create_user](https://github.com/Jorik-Goris/api-eindproject/assets/95848835/59970993-867e-410a-8ff5-9be5693ac780)
![authenticate_user](https://github.com/Jorik-Goris/api-eindproject/assets/95848835/24b8581d-c85f-444d-8905-76c98f2afa65)
![:users:me 200 after auth](https://github.com/Jorik-Goris/api-eindproject/assets/95848835/70b76a0a-2775-4f4d-aa2c-06b3eec804d0)


### Aanmaken van gebruikers

In deze stap worden enkele users aangemaakt: Harry Potter, Voldemort en Perkamentus. In de volgende stappen zullen voor enkele van deze users tasks aangemaakt/beheerd worden.

### Aanmaken van tasks voor een bepaalde user

Om een task aan te maken voor een bepaalde user kan de user_id meegegeven worden. In de response body kan men de owner van deze task zien met de username die behoort tot deze user_id.

### Alle tasks voor een bepaalde user ophalen

Met volgende endpoint is het mogelijk alle tasks op te halen die toe behoren tot een specifieke user. Dit kan met de user_id als path parameter. 

### Alle tasks voor alle users ophalen

Het is ook mogelijk alle tasks op te halen. Onder het owner attribuut kan men de username (key) en value van de owner van deze task terugvinden.

### Tasks opvragen op basis van categorie

Het is mogelijk tasks op te halen op basis van hun categorie. In dit voorbeeld wordt gebruik gemaakt van de categorie 'Education'. Hier zit 1 task in. Wanneer dit er meerdere zouden zijn worden deze ook getoond.


### Updaten van een task

Tasks kunnen doormiddel van een put request en hun task_id bijgewerkt worden. In dit voorbeeld werd de due_date aangepast.


### Deleten van een task

Het verwijderen van een task kan door middel van een DELETE request en de task_id








