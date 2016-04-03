RUN APP
---
```
sudo apt-get install libpq-dev python-dev
```

```
pip install -r requirements.txt
```

```
touch Makefile.settings && echo "DATABASE_URL=postgres://{USER}:{PASSWORD}@localhost:5432/{DATABASE}" > Makefile.settings
```