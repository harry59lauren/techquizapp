import yaml
import json
import pprint

with open("test.yaml", 'r') as quizyaml:
    quiz = yaml.safe_load(quizyaml)
    pprint.pprint(quiz)