import os

PROJECT_APP_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_DIR = os.path.realpath(os.path.join(PROJECT_APP_DIR, ".."))
LOG_PATH = os.path.join(PROJECT_DIR, "logs")

print(PROJECT_APP_DIR)
print(PROJECT_DIR)
print(LOG_PATH)

