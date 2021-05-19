Homework #2

The homework is dedicated to prediction of heart desease using data of some medical
analysys. The goal of this homework to create ready for production rest service aimed  to predict heart desease

The data is taken from: https://www.kaggle.com/ronitf/heart-disease-uci.

Assuming that current directory is root of git repository you should make next steps
1. Create and activate new environment:

```
    cd online_inference
	
    Installation (for Windows):  
        python -m venv .venv
       .venv\Scripts\activate.bat
       pip install -r requirements.txt

    Installation (for Linux):  
       python -m venv .venv
       source .venv/bin/activate
       pip install -r requirements.txt
```

2. To run the the rest service you can do it two ways:

   Build docker image by yourself:

```
docker build -t mykolesiko/model_inference:v1 .

```
Or you can Pull docker image from Docker Hub:

```
docker pull mykolesiko/model_inference:v1

```

3. Then Run docker with the rest service:

```
docker run -p 8000:8000 mykolesiko/model_inference:v1

```
Test client application aimed to request the predictions.
You should have the file with data in csv format. You should pass the arguments to the application or leave them for default 

```
python -m src.make_request --host [host] --port [port]  --path_to_data [path to csv file] --num_predictions [num_predictions]

```
To test it try example:

```
python -m src.make_request  --path_to_data data_to_predict.csv 

```


Roadmap
0 |+| Ветку назовите homework2, положите код в папку online_inference 

1 |+| Оберните inference вашей модели в rest сервис(вы можете использовать как FastAPI, так и flask, другие желательно не использовать, дабы не плодить излишнего разнообразия для проверяющих), должен быть endpoint /predict | 3

2 |-| Напишите тест для /predict | 3

3 |+| Напишите скрипт, который будет делать запросы к вашему сервису | 2

4 |+| Сделайте валидацию входных данных (например, порядок колонок не совпадает с трейном, типы не те и пр, в рамках вашей фантазии) | 3

5 |+| Напишите dockerfile, соберите на его основе образ и запустите локально контейнер(docker build, docker run), внутри контейнера должен запускать сервис, написанный в предущем пункте, закоммитьте его, напишите в readme корректную команду сборки~~ | 4

6 |+| Оптимизируйте размер docker image(опишите в readme.md что вы предприняли для сокращения размера и каких результатов удалось добиться) | 3

   Использовала в качестве базового образа python:3.8-slim вместо python:3.8

7 |+| Опубликуйте образ в https://hub.docker.com/, используя docker push | 2

8 |+|Напишите в readme корректные команды docker pull/run, которые должны привести к тому, что локально поднимется на inference ваша модель | 3

9 |+|Проведите самооценку | 1


