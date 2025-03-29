import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATASET_DIR = os.path.join(BASE_DIR, 'datasets/user_datasets/')
MODEL_DIR = os.path.join(BASE_DIR, 'models/base_model/')
FINE_TUNED_MODEL_DIR = os.path.join(BASE_DIR, 'fine_tuned_models/user_models/')
