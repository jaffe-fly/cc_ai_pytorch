# -*- coding: UTF-8 -*-

from flask import Flask, request, jsonify
# from nemo.core.config import hydra_runner
import hydra
import logging
# from nemo.utils import logging


@hydra.main(config_path="conf", config_name="citrinet_512")
def main(cfg):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "superman"

    @app.route("/predict", methods=['POST'])
    def predict():
        try:
            data = request.files
            # data = request.get_json()
            if 'input' not in data:
                return 'input not exsit', 500
            file = data['input']



            result = []
            return jsonify({'content': result})

        except Exception as e:
            logging.error(e)
            # logger.error(e.args)
            return f'未知错误:[{e}]', 500

    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
