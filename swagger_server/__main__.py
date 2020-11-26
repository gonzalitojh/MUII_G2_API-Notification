#!/usr/bin/env python3

import connexion

from swagger_server import encoder

app = connexion.App(__name__, specification_dir='./swagger/')

def main():
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Notification Management API'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
