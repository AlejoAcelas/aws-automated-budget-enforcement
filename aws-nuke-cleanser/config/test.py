# %%
import yaml

with open("nuke_generic_config.yaml", "r") as file:
    config = yaml.safe_load(file)

filter_objs = config['accounts']['ACCOUNT']['filters']
print(list(filter_objs.keys()))
# %%
