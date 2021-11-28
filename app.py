import sys

from config import OPENAPI_AUTOGEN_DIR

sys.path.append(OPENAPI_AUTOGEN_DIR)

try:
    import connexion
except ModuleNotFoundError:
    print("Please install all required packages by running:"
          " pip install -r requirements.txt")
    exit(1)

from openapi_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('carbonster-api.yaml',
                arguments={'title': 'Carbonster API'},
                pythonic_params=True)

    app.run(port=8000, debug=True)


if __name__ == '__main__':
    main()
