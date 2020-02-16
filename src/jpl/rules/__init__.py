from itertools import chain


from src.jpl.rules.playbook import info as base
from src.jpl.rules.pipeline import pipeline


rules = list(chain.from_iterable([base.rules, pipeline.rules]))
