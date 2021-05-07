Homework N1

The homework is dedicated to prediction of heart desease using data of some medical
analysys. Used for investigation data was downloaded from https://www.kaggle.com/ronitf/heart-disease-uci
and is located now in data/raw directory in csv file (heart.csv). 
Structure of project (located in ml_project folder) is described at the bottom of this
article. 

Assuming that current directory is root of git repository you should make next steps
1. Create and activate new environment:

    Installation (for Windows):  
        python -m venv .venv
       .venv\Scripts\activate.bat
       pip install -r requirements.txt

    Installation (for Linux):  
       python -m venv .venv
       source .venv/bin/activate
       pip install -r requirements.txt

2. cd ml_project

3. Test the code with pytest. To run scripts use command:

   pytest tests	

4. Create and train model. In this pipeline next steps would be :

   python -m src.implement_pipeline --config [path to config.yaml file]

5. Get predictions ():
   path_to_save_predictions - use predict/{some_new_folder_name}, if there is no such folder, it would be created.
    
   python -m src.model.predict --data [path_to_data_file] --model [path_to_model_file] --transformer [path_transformer_file] -output_path [path_to_save_predictions]

Project Organization
------------

    +-- LICENSE
    +-- Makefile           <- Makefile with commands like `make data` or `make train`
    +-- README.md          <- The top-level README for developers using this project.
    +-- data
    ¦   +-- external       <- Data from third party sources.
    ¦   +-- interim        <- Intermediate data that has been transformed.
    ¦   +-- processed      <- The final, canonical data sets for modeling.
    ¦   L-- raw            <- The original, immutable data dump.
    ¦
    +-- docs               <- A default Sphinx project; see sphinx-doc.org for details
    ¦
    +-- models             <- Trained and serialized models, model predictions, or model summaries
    ¦
    +-- notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    ¦                         the creator's initials, and a short `-` delimited description, e.g.
    ¦                         `1.0-jqp-initial-data-exploration`.
    ¦
    +-- references         <- Data dictionaries, manuals, and all other explanatory materials.
    ¦
    +-- reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    ¦   L-- figures        <- Generated graphics and figures to be used in reporting
    ¦
    +-- requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    ¦                         generated with `pip freeze > requirements.txt`
    ¦
    +-- setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    +-- ml_example                <- Source code for use in this project.
    ¦   +-- __init__.py    <- Makes src a Python module
    ¦   ¦
    ¦   +-- data           <- code to download or generate data
    ¦   ¦
    ¦   +-- features       <- code to turn raw data into features for modeling
    ¦   ¦
    ¦   +-- models         <- code to train models and then use trained models to make
    ¦   ¦
    L-- tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


Let's estimate what's was done in this homework:

  -2) Назовите ветку homework1 (1 балл) +
  -1) положите код в папку ml_project   +
   0) В описании к пулл реквесту описаны основные "архитектурные" и тактические решения, 
      которые сделаны в вашей работе. В общем, описание что именно вы сделали и для чего, 
      чтобы вашим ревьюерам было легче понять ваш код. (2 балла) +

   1) Выполнение EDA, закоммитьте ноутбук в папку с ноутбуками (2 баллов) +
      Вы так же можете построить в ноутбуке прототип(если это вписывается в ваш стиль работы)
      Можете использовать не ноутбук, а скрипт, который сгенерит отчет, закоммитьте и скрипт и отчет (за это + 1 балл)

   2) Проект имеет модульную структуру(не все в одном файле =) ) (2 баллов) +
   3) использованы логгеры (2 балла) +
   4) написаны тесты на отдельные модули и на прогон всего пайплайна(3 баллов) 
   5) Для тестов генерируются синтетические данные, приближенные к реальным (3 баллов)
	- можно посмотреть на библиотеки https://faker.readthedocs.io/en/, https://feature-forge.readthedocs.io/en/latest/
	- можно просто руками посоздавать данных, собственноручно написанными функциями
	как альтернатива, можно закоммитить файл с подмножеством трейна(это не оценивается) 

   6) Обучение модели конфигурируется с помощью конфигов в json или yaml, закоммитьте как минимум 2 корректные конфигурации, 
      с помощью которых можно обучить модель (разные модели, стратегии split, preprocessing) (3 балла) +

   7) Используются датаклассы для сущностей из конфига, а не голые dict (3 балла) +
   8) Используйте кастомный трансформер(написанный своими руками) и протестируйте его(3 балла) +
   9) Обучите модель, запишите в readme как это предлагается (3 балла) +
   10) напишите функцию predict, которая примет на вход артефакт/ы от обучения, тестовую выборку(без меток) и 
       запишет предикт, напишите в readme как это сделать (3 балла)   +

   11) Используется hydra  (https://hydra.cc/docs/intro/) (3 балла - доп баллы) (-)
   12) Настроен CI(прогон тестов, линтера) на основе github actions  (3 балла - доп баллы (будем проходить дальше в курсе, но если есть желание поразбираться - welcome)
   13) Проведите самооценку, опишите, в какое колво баллов по вашему мнению стоит оценить вашу работу и почему (1 балл доп баллы) +



