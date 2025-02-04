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
