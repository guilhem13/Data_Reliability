"""
Name: Data Reliability Demo
Author: Guilhem Maillebuau
Api which outlow the concept of data reliability as code 
"""

from waitress import serve
from api import create_app


if __name__ == "__main__":   

    app = create_app()
    serve(app, host="0.0.0.0", port=5000)