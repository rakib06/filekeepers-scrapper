# Project details

### This bot will collect data (item and it's price) from the following site... 
![image](https://user-images.githubusercontent.com/34921424/185757751-241ac38c-b091-46e3-8c4a-c0050a5614b6.png)


# Project Installation
```
git clone https://github.com/rakib06/filekeepers-scrapper.git
cd filekeepers-scrapper
```
##### create a .env file like this [.env] at ```app/.env``` (https://github.com/rakib06/filekeepers-scrapper/blob/main/env.md), and then

```
docker-compose build
docker-compose up
```

# About the Project 
### Local dir
![image](https://user-images.githubusercontent.com/34921424/185757794-a864d7fc-e053-418b-bef1-39e5eaa221c4.png)

#### ```local/log/{date}```: Scrapping Status will be shown here
![image](https://user-images.githubusercontent.com/34921424/185757870-6a9be073-faf3-4898-9cf6-ffb37fc8ae9a.png)
#### ```local/log/{mongo_db}``` DB Operations will be shown here
![image](https://user-images.githubusercontent.com/34921424/185757962-857852b9-e84c-41f7-b795-a57c63cfcc03.png)
#### local/data/{OUTPUT_FILE_NAME} Data inserted to db will be shown here using mongo query
![image](https://user-images.githubusercontent.com/34921424/185758009-7af74a30-fc9b-47e0-9169-cc2f8a11c895.png)

