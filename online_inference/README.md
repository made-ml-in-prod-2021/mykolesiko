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
0 |+| ����� �������� homework2, �������� ��� � ����� online_inference | -
1 |+| �������� inference ����� ������ � rest ������(�� ������ ������������ ��� FastAPI, ��� � flask, ������ ���������� �� ������������, ���� �� ������� ��������� ������������ ��� �����������), ������ ���� endpoint /predict | 3
2 |-| �������� ���� ��� /predict | 3
3 |+| �������� ������, ������� ����� ������ ������� � ������ ������� | 2
4 |+| �������� ��������� ������� ������ (��������, ������� ������� �� ��������� � �������, ���� �� �� � ��, � ������ ����� ��������) | 3
5 |+| �������� dockerfile, �������� �� ��� ������ ����� � ��������� �������� ���������(docker build, docker run), ������ ���������� ������ ��������� ������, ���������� � �������� ������, ����������� ���, �������� � readme ���������� ������� ������~~ | 4
6 |-| ������������� ������ docker image(������� � readme.md ��� �� ����������� ��� ���������� ������� � ����� ����������� ������� ��������) | 3
7 |+| ����������� ����� � https://hub.docker.com/, ��������� docker push | 2
8 |+|�������� � readme ���������� ������� docker pull/run, ������� ������ �������� � ����, ��� �������� ���������� �� inference ���� ������ | 3
9 |+|��������� ���������� | 1