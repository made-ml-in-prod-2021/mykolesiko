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

   pytest --cov=src -v 

4. Create and train model. In this pipeline next steps would be :

   python -m src.implement_pipeline --config [path to config.yaml file] 
   
   try example:
   python -m src.implement_pipeline --config model_randomforest.yaml 

   Model, transform, logs and metrics would be saved in folder models.[model_folder](where model_folder can be configured in yaml file)	
	

5. Generate test data 

   python -m src.data.generate_data --train_data [path_to_train_data_file] --rows [num_of_rows_to_generate] --test_data [path_to_test_data_file]  

   try example:
   python -m src.data.generate_data --train_data ./data/raw/heart.csv  --rows 100  --test_data ./data/test/test.csv
  
   check file test.csv	

6. Get predictions ():
   path_to_save_predictions - use predict/{some_new_folder_name}, if there is no such folder, it would be created.
    
   python -m src.predict --data [path_to_data_file] --model [path_to_model_file] --transformer [path_transformer_file] -output_path [path_to_save_predictions]

   try example:
   python -m src.predict --data ./data/test/test1.csv --model ./models/RandomForest/model.pkl --transformer ./model/RandomForest/transformer.pkl --output ./predicts

   check files in ./predicts

Let's estimate what's was done in this homework:

  -2) ������� ���� homework1 (1 ����) +
  -1) ������� ��� � ����� ml_project   +
   0) � ���ᠭ�� � �㫫 ४����� ���ᠭ� �᭮��� "���⥪����" � ⠪��᪨� �襭��, 
      ����� ᤥ���� � ��襩 ࠡ��. � ��饬, ���ᠭ�� �� ������ �� ᤥ���� � ��� 祣�, 
      �⮡� ��訬 ॢ��ࠬ �뫮 ���� ������ ��� ���. (2 �����) +

   1) �믮������ EDA, ���������� ����� � ����� � ����㪠�� (2 ������) +
      �� ⠪ �� ����� ����ந�� � ����㪥 ���⨯(�᫨ �� ����뢠���� � ��� �⨫� ࠡ���)
      ����� �ᯮ�짮���� �� �����, � �ਯ�, ����� ᣥ���� ����, ���������� � �ਯ� � ���� (�� �� + 1 ����)

   2) �஥�� ����� ������� ��������(�� �� � ����� 䠩�� =) ) (2 ������) +
   3) �ᯮ�짮���� ������� (2 �����) +
   4) ����ᠭ� ���� �� �⤥��� ���㫨 � �� �ண�� �ᥣ� ���������(3 ������) +-
   5) ��� ��⮢ ����������� ᨭ���᪨� �����, �ਡ������� � ॠ��� (3 ������) +
	- ����� ��ᬮ���� �� ������⥪� https://faker.readthedocs.io/en/, https://feature-forge.readthedocs.io/en/latest/
	- ����� ���� �㪠�� ��ᮧ������ ������, ᮡ�⢥�����筮 ����ᠭ�묨 �㭪�ﬨ
	��� ����ୠ⨢�, ����� ���������� 䠩� � ���������⢮� �३��(�� �� �業�������) 

   6) ���祭�� ������ ���䨣������� � ������� ���䨣�� � json ��� yaml, ���������� ��� ������ 2 ���४�� ���䨣��樨, 
      � ������� ������ ����� ������ ������ (ࠧ�� ������, ���⥣�� split, preprocessing) (3 �����) +

   7) �ᯮ������� ��⠪����� ��� ��魮�⥩ �� ���䨣�, � �� ���� dict (3 �����) +
   8) �ᯮ���� ���⮬�� �࠭��ଥ�(����ᠭ�� ᢮��� �㪠��) � �������� ���(3 �����) +
   9) ����� ������, ������ � readme ��� �� �।�������� (3 �����) +
   10) ������ �㭪�� predict, ����� �ਬ�� �� �室 ���䠪�/� �� ���祭��, ��⮢�� �롮��(��� ��⮪) � 
       ������ �।���, ������ � readme ��� �� ᤥ���� (3 �����)   +

   11) �ᯮ������ hydra  (https://hydra.cc/docs/intro/) (3 ����� - ��� �����) (-)
   12) ����஥� CI(�ண�� ��⮢, �����) �� �᭮�� github actions  (3 ����� - ��� ����� (�㤥� ��室��� ����� � ����, �� �᫨ ���� ������� ��ࠧ������� - welcome)
   13) �஢���� ᠬ��業��, �����, � ����� ����� ������ �� ��襬� ������ �⮨� �業��� ���� ࠡ��� � ��祬� (1 ���� ��� �����) +



