# Virtual Env Installation Mac
pip3 install virtualenv
# Setting up virtual environment
virtualenv -p python3
# Activating Environment
source venv/bin/activate
# Deactivating
deactivate

# Install python requirements
pip install -r requirements.txt

# If you are adding any new python libraries,
# make sure to add to the requirement.txt file
pip freeze >> requirements.txt