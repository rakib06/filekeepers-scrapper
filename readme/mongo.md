# Mongo Test 

data should be saved at. ```app/data``` directory 

### Standalone Check 

```
docker run -d -p 27017:27017 --name m1 mongo
python app/insert.py
python app/select.py
```
