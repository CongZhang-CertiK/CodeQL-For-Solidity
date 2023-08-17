virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python3 docker-build.py
python3 compile.py