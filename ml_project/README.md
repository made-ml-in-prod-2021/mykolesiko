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

   python -m src.implement_pipeline -config [path to config.yaml file]

5. Get predictions:
    
   python -m src.model.predict --data [path_to_data] --model [path_to_model] --output_path [path_to_predictions]

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

