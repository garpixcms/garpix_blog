# Garpix Blog


## Быстрый старт

Установка:

```bash
pip install garpix_blog
```

Добавьте `garpix_vacancy` в `INSTALLED_APPS`:

```python
# settings.py

INSTALLED_APPS = [
    # ...
    'garpix_blog',
]

MIGRATION_MODULES.update(
    {'garpix_blog': 'app.migrations.garpix_blog'}
)
```


# Changelog

Смотри [CHANGELOG.md](CHANGELOG.md).

# Contributing

Смотри [CONTRIBUTING.md](CONTRIBUTING.md).

# License

[MIT](LICENSE)

---

Developed by Garpix / [https://garpix.com](https://garpix.com)