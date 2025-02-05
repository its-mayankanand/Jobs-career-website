'''
import os
import importlib

# Get all Python files in the current directory (excluding app.py)
python_files = [f[:-3] for f in os.listdir() if f.endswith('.py') and f != 'app.py']

# Import and execute all modules

for module_name in python_files:
    module = importlib.import_module(module_name)
    if hasattr(module, 'main'):
        print(f'Executing {module_name}.main()')
        module.main()
'''

#------------------------------------------------------
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, world , hello nanaji left"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
