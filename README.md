# fastapi-starter

python fastapi starter

> ⚠️ **DISCLAIMER:** the boilerplate code may not work (as it's not meant to be) use the folder structure that's the purpose.

# Setting up the project

## setting up virutal env

`.env` is the name of the virutal env folder, you can change it as you like.

```bash
python -m venv .env
```

Source into the virutal env

```bash
source ./.env/bin/activate
```

download the requirements

```bash
pip install -r requirements.txt
```

# Running the app

simply do

```bash
fastapi run app/main.py
```

recommended one: (both works choice tbh)

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

for production

```bash
fastapi run
```

or recommended

```bash
CMD uvicorn app.main:app --port 8000
```

(u may want to replace the port with either an env variable or the port u're exposing it on the remote host...)
