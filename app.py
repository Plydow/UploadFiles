from flask import Flask
import yaml

from routes.views import views

app = Flask(__name__)

def load_config(app, config_file='config.yaml'):
    with open(config_file) as yaml_file:
        cfg = yaml.safe_load(yaml_file)
    app.config.update(cfg)

if __name__ == '__main__':
    load_config(app)
    app.register_blueprint(views)
    app.run()