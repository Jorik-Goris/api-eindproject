# Eindproject API development - Jorik Goris

Deze repository bevat de eindopdracht voor het vak API development.

## Thema

Deze API bevat een task management systeem dat het toelaat om verschillende tasks aan te maken voor gebruikers. Deze tasks hebben titels, descriptions, due dates, categories, owners, en een boolean die aanduidt of ze al dan niet afgewerkt zijn.

Volgende endpoints zijn aanwezig:

![all_endpoints](https://github.com/Jorik-Goris/api-eindproject/assets/95848835/e3e0e212-beeb-4091-ae4d-564176682941)

## Demo

Hier volgt een demonstratie van alle endpoints in Postman.

### OAuth user aanmaken en authenticeren

![create_user](https://github.com/Jorik-Goris/api-eindproject/assets/95848835/59970993-867e-410a-8ff5-9be5693ac780)
![authenticate_user](https://github.com/Jorik-Goris/api-eindproject/assets/95848835/24b8581d-c85f-444d-8905-76c98f2afa65)
![users_me_200_after_auth](https://github.com/Jorik-Goris/api-eindproject/assets/95848835/70b76a0a-2775-4f4d-aa2c-06b3eec804d0)

### Aanmaken van gebruikers

In deze stap worden enkele users aangemaakt: Harry Potter, Voldemort en Perkamentus. In de volgende stappen zullen voor enkele van deze users tasks aangemaakt/beheerd worden.

![create_user_id2](https://github.com/Jorik-Goris/api-eindproject/assets/95848835/d0bb2b1f-e26c-46e7-869b-31af6889a8d1)
![create_user_id3](https://github.com/Jorik-Goris/api-eindproject/assets/95848835/848cf28f-09ca-416e-a195-0c4e1d4e5a62)
![create_user_id4](https://github.com/Jorik-Goris/api-eindproject/assets/95848835/6e68447b-d5a8-4116-9980-65ccd2db916c)

### Aanmaken van tasks voor een bepaalde user

Om een task aan te maken voor een bepaalde user kan de user_id meegegeven worden. In de response body kan men de owner van deze task zien met de username die behoort tot deze user_id.

![create_task_harry](https://github.com/Jorik-Goris/api-eindproject/assets/95848835/433be1be-9633-43a6-a334-eb20553e54ed)
![create_task_perkamentus](https://github.com/Jorik-Goris/api-eindproject/assets/95848835/2c26c22b-df8d-4399-b806-79cec62f73bf)
![create_task_perkamentus_2](https://github.com/Jorik-Goris/api-eindproject/assets/95848835/dda0c4d6-1a0e-4305-9357-2eb59e582264)

### Alle tasks voor een bepaalde user ophalen

Met volgende endpoint is het mogelijk alle tasks op te halen die toebehoren tot een specifieke user. Dit kan met de user_id als path parameter.

![get_all_tasks_for_userid_4](https://github.com/Jorik-Goris/api-eindproject/assets/95848835/ea02d038-2a37-46f6-b462-81fcdfb67ce5)

### Alle tasks voor alle users ophalen

Het is ook mogelijk alle tasks op te halen. Onder het owner attribuut kan men de username (key) en value van de owner van deze task terugvinden.

![get_all_tasks](https://github.com/Jorik-Goris/api-eindproject/assets/95848835/5f4f794e-3021-4d1c-bae5-ccf2827d9f48)

### Tasks opvragen op basis van categorie

Het is mogelijk tasks op te halen op basis van hun categorie. In dit voorbeeld wordt gebruik gemaakt van de categorie 'Education'. Hier zit 1 task in. Wanneer dit er meerdere zouden zijn worden deze ook getoond.

![get_education_category_tasks](https://github.com/Jorik-Goris/api-eindproject/assets/95848835/f9fbb3c6-0ab4-4617-87dc-ae1ba9f1ed11)

### Updaten van een task

Tasks kunnen doormiddel van een put request en hun task_id bijgewerkt worden. In dit voorbeeld werd de due_date aangepast.

![Update_tasks_date_by_put_request](https://github.com/Jorik-Goris/api-eindproject/assets/95848835/94f9792e-00d6-4315-9c63-2d03ebe6b8bc)

### Deleten van een task

Het verwijderen van een task kan door middel van een DELETE request en de task_id

![delete_task_id_1](https://github.com/Jorik-Goris/api-eindproject/assets/95848835/165a1ff8-6f8b-46b4-aec2-9267c900341e)

## Deployment

Om dit project te deployen op Okteto Cloud kan deze gebuild worden als docker image. Hiervoor worden de dockerfile en docker-compose.yaml files gebruikt. Deze gaat een container image van de /app directory maken en de requirements file gebruiken om de nodige dependencies te installeren.

Deze wordt via de Github Actions pipeline automatisch gebuild bij een commit op de main branch.

(Bij het deployen lijkt iets mis te gaan. Okteto Cloud logs duiden op een ModuleNotFoundError: No module named app en een 'from app.database import SessionLocal, engine' op lijn 4 in main.py. Deze lijnen zijn echter aangepast en de image is gerebuild, toch blijft de oude code deployen (die niet meer bestaat in de github repo.(bug?))


## Frontend

De frontend voor de api is gebouwd met AlpineJS en opgemaakt met CSS.
![Screenshot 2024-01-02 at 11 15 11](https://github.com/Jorik-Goris/api-eindproject/assets/95848835/d41f7b4d-08d0-49ab-95c9-a3ab053eb4ca)

### Host frontend op Netlify

Om de frontend te hosten op Netlify en automatisch te voorzien van een SSL certificaat kan je volgende stappen volgen:

1. Sign up op Netlify
2. Geef toegang tot de betreffende Github repository
3. Klik OK

![Screenshot 2024-01-02 at 11 20 59](https://github.com/Jorik-Goris/api-eindproject/assets/95848835/89484d31-b773-4239-a3d0-1e7c52028250)



