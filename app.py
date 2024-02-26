from flask import Flask
import yaml

from routes.views import views

app = Flask(__name__)

def load_config(app, config_file='config/config.yaml'):
    with open(config_file) as yaml_file:
        cfg = yaml.safe_load(yaml_file)
    app.config.update(cfg)

def create_app():
    load_config(app)
    app.register_blueprint(views)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=False, host='0.0.0.0', port=5000)