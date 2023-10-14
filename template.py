# Compulsory this library or code import all project
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "mlproject" # this name mention as your wish don't required any where its just for this module project package 

list_of_files = [
    ".circleci/config.yml",
    ".circleci/terraform.yml",
    "airflow/dags/__init__.py",
    "airflow/dags/demo.py",
    "airflow/dags/fc_training_pipeline.py",
    "docker-compose-resource/prometheus/prometheus.yml",
    "docker-compose-resource/promtail/config.yml",
    "infrastructure/module.tf",
    "infrastructure/finance_artifact_repository/registry.tf",
    "infrastructure/finance_artifact_repository/registry_iam_role.tf",
    "infrastructure/finance_artifact_repository/variables.tf",
    "infrastructure/finance_model_bucket/model.tf",
    "infrastructure/finance_model_bucket/model_policy.tf",
    "infrastructure/finance_model_bucket/variables.tf",
    "infrastructure/finance_virtual_machine/virtual_machine.tf",
    "infrastructure/finance_virtual_machine/virtual_machine_firewall.tf",
    "infrastructure/finance_virtual_machine/variables.tf",
    "infrastructure/finance_virtual_machine/virtual_machine_iam_policy.tf",
    "infrastructure/finance_virtual_machine/virtual_machine_service_account.tf",
    f"finance/{project_name}/__init__.py",
    f"finance/{project_name}/exception.py",
    f"finance/{project_name}/logger.py",
    f"finance/{project_name}/cloud_storage/__init__.py",
    f"finance/{project_name}/cloud_storage/s3_syncer.py",
    f"finance/{project_name}/component/__init__.py",
    f"finance/{project_name}/component/training/__init__.py",
    f"finance/{project_name}/component/training/data_ingestion.py",
    f"finance/{project_name}/component/training/data_validation.py",
    f"finance/{project_name}/component/training/data_transformation.py",
    f"finance/{project_name}/component/training/model_evaluation.py",
    f"finance/{project_name}/component/training/model_pusher.py",
    f"finance/{project_name}/component/training/model_trainer.py",
    f"finance/{project_name}/component/prediction/__init__.py",
    f"finance/{project_name}/configuration/__init__.py",
    f"finance/{project_name}/configuration/mongo_db_connection.py",
    f"finance/{project_name}/configuration/aws_connection_config.py",
    f"finance/{project_name}/configuration/spark_manager.py",
    f"finance/{project_name}/configuration/pipeline/__init__.py",
    f"finance/{project_name}/configuration/pipeline/prediction.py",
    f"finance/{project_name}/configuration/pipeline/training.py",
    f"finance/{project_name}/constant/__init__.py",
    f"finance/{project_name}/constant/database/__init__.py",
    f"finance/{project_name}/constant/environment/__init__.py",
    f"finance/{project_name}/constant/environment/variable_key.py",
    f"finance/{project_name}/constant/model/__init__.py",
    f"finance/{project_name}/constant/prediction_pipleline_config/__init__.py",
    f"finance/{project_name}/constant/prediction_pipleline_config/file_config.py",
    f"finance/{project_name}/constant/training_pipleline_config/__init__.py",
    f"finance/{project_name}/constant/training_pipleline_config/data_ingestion.py",
    f"finance/{project_name}/constant/training_pipleline_config/data_validation.py",
    f"finance/{project_name}/constant/training_pipleline_config/data_transformation.py",
    f"finance/{project_name}/constant/training_pipleline_config/model_trainer.py",
    f"finance/{project_name}/constant/training_pipleline_config/model_evaluation.py",
    f"finance/{project_name}/constant/training_pipleline_config/model_pusher.py",
    f"finance/{project_name}/data_access/__init__.py",
    f"finance/{project_name}/data_access/model_eval_artifact.py",
    f"finance/{project_name}/entity/__init__.py",
    f"finance/{project_name}/entity/artifact_entity.py",
    f"finance/{project_name}/entity/config_entity.py",
    f"finance/{project_name}/entity/estimator.py",
    f"finance/{project_name}/entity/metadata_entity.py",
    f"finance/{project_name}/entity/schema.py",
    f"finance/{project_name}/ml/__init__.py",
    f"finance/{project_name}/ml/feature.py",
    f"finance/{project_name}/pipeline/__init__.py",
    f"finance/{project_name}/pipeline/training_pipeline.py",
    f"finance/{project_name}/pipeline/prediction_pipeline.py",
    f"finance/{project_name}/utils/__init__.py",
    f"finance/{project_name}/utils/main_utils.py",
    "main.py",
    "mainpipeline.py",
    "docker-compose.yaml",
    "demo.ipynb", # this code have new additions, but this file you have created manually project
    "Dockerfile", # this code have new additions, but this file you have created manually project
    "requirements.txt",
    "setup.py",
    "start.sh",
    "research/EDA.ipynb",
    "research/Feature.ipynb",
    "research/Model.ipynb",
    "research/Model_Eval.ipynb",
    "research/Preprocessing.ipynb",
    "research/Testing.ipynb",
 
]


for filepath in list_of_files:
    # Sometimes getting a issue for backslashes because normally computer use the forward slashes so that above file use / forward slashes, below code help
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")