Keystroke Dynamics Anomaly Detection
==============================
As cybersecurity attacks increase, the static methods for anomaly detection are no longer enough for protection. We proposed an algorithm for dynamic anomaly detection based on keystroke patterns that are unique for everyone, just like your fingerprint but digitally. Behavioral biometrics also overcome the most important limitation of physiological biometrics systems, as we can collect them without the knowledge of the user, allowing for continuous authentication. The user rhythm for 51 users with the fixed text password (.tie5Roanl) typed in 8 sessions for 50 repetitions per session. The proposed model Random Forrest achieve 94.09 % for F1 for this study. However, we tested the work by our own dataset which was collected and tested by typing the same password to check the user authentication.</br>
## Pre-requirement
- Java version 11.
- Logstash version 8.1.2
- Docker-compse
## Setup Enviroment
- Creat required containered (Kafka,Zookeeper,Elastic search,Kibna)<br>
-----------
    docker-compose -f setup_config\docker-compse.yml up
-----------
- copy logstash_pipeline.conf in the logstash-8.1.2\config
- run the logstash consumer
---------------
    .\bin\logstash.bat -f .\config\logstash_pipeline.conf
---------------
    
- run producer

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
