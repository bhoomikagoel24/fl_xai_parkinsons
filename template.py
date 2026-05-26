import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s:'
)

# Project Name
project_name = "fl_xai_parkinsons"

# Project Structure
list_of_files = [

    # Root Package
    f"{project_name}/__init__.py",

    # =========================
    # CORE MODULES
    # =========================

    # Preprocessing
    f"{project_name}/core/preprocessing/__init__.py",
    f"{project_name}/core/preprocessing/data_loader.py",
    f"{project_name}/core/preprocessing/data_cleaning.py",
    f"{project_name}/core/preprocessing/feature_engineering.py",

    # Models
    f"{project_name}/core/models/__init__.py",
    f"{project_name}/core/models/cnn_model.py",
    f"{project_name}/core/models/lstm_model.py",
    f"{project_name}/core/models/hybrid_model.py",

    # Federated Learning
    f"{project_name}/core/federated/__init__.py",
    f"{project_name}/core/federated/client.py",
    f"{project_name}/core/federated/server.py",
    f"{project_name}/core/federated/training.py",

    # Aggregation
    f"{project_name}/core/aggregation/__init__.py",
    f"{project_name}/core/aggregation/fedavg.py",
    f"{project_name}/core/aggregation/secure_aggregation.py",

    # Explainability
    f"{project_name}/core/explainability/__init__.py",
    f"{project_name}/core/explainability/shap_explainer.py",
    f"{project_name}/core/explainability/lime_explainer.py",

    # Evaluation
    f"{project_name}/core/evaluation/__init__.py",
    f"{project_name}/core/evaluation/metrics.py",
    f"{project_name}/core/evaluation/evaluate.py",

    # Validation
    f"{project_name}/core/validation/__init__.py",
    f"{project_name}/core/validation/validator.py",

    # =========================
    # DASHBOARD
    # =========================

    f"{project_name}/dashboard/__init__.py",

    # Pages
    f"{project_name}/dashboard/pages/__init__.py",
    f"{project_name}/dashboard/pages/home.py",
    f"{project_name}/dashboard/pages/analytics.py",

    # Components
    f"{project_name}/dashboard/components/__init__.py",
    f"{project_name}/dashboard/components/sidebar.py",
    f"{project_name}/dashboard/components/charts.py",

    # =========================
    # EXPERIMENTS
    # =========================

    f"{project_name}/experiments/__init__.py",
    f"{project_name}/experiments/experiment_01.py",

    # =========================
    # VISUALIZATION
    # =========================

    f"{project_name}/visualization/__init__.py",
    f"{project_name}/visualization/plots.py",

    # =========================
    # CONFIG
    # =========================

    f"{project_name}/config/__init__.py",
    f"{project_name}/config/configuration.py",

    # =========================
    # OUTPUTS
    # =========================

    f"{project_name}/outputs/results/.gitkeep",

    # =========================
    # UTILS
    # =========================

    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/common.py",

    # =========================
    # LOGGER
    # =========================

    f"{project_name}/logger/__init__.py",
    f"{project_name}/logger/logging.py",

    # =========================
    # MAIN ENTRY
    # =========================

    f"{project_name}/main.py",

    # =========================
    # ROOT FILES
    # =========================

    "requirements.txt",
    "setup.py",
    "README.md",
    ".gitignore",
    ".dockerignore",
    "Dockerfile",
    "config.yaml"
]

# Create Files and Folders
for filepath in list_of_files:

    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directories
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    # Create empty files
    if not filepath.exists():
        with open(filepath, "w") as f:
            pass

        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filepath} already exists")