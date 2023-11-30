### python i18n sample with fastapi, gettext, contextvars

sample code for implementing i18n in a fastapi/starlette (or whatever python framework (or whatever python software))

in this implementation we use python's gettext module and locale directories with .po .mo files (like how django does it)

#### useful links related to this topic:

[https://docs.python.org/3.12/library/gettext.html](https://docs.python.org/3.12/library/gettext.html)

[https://docs.python.org/3/library/contextvars.html](https://docs.python.org/3/library/contextvars.html)

[https://peps.python.org/pep-0567/](https://peps.python.org/pep-0567/)

[https://docs.djangoproject.com/en/4.2/topics/i18n/translation/](https://docs.djangoproject.com/en/4.2/topics/i18n/translation/)

[https://github.com/encode/starlette/issues/420](https://github.com/encode/starlette/issues/420)

[https://github.com/tomwojcik/starlette-context](https://github.com/tomwojcik/starlette-context)

- django also uses contextvars for translation stuff

[https://github.com/django/asgiref/blob/main/asgiref/local.py](https://github.com/django/asgiref/blob/main/asgiref/local.py)

[https://github.com/django/django/blob/b34a4771a3d4cd7829a1f38a0f6a7a0da519a724/django/utils/translation/trans_real.py#L368](https://github.com/django/django/blob/b34a4771a3d4cd7829a1f38a0f6a7a0da519a724/django/utils/translation/trans_real.py#L368)

### start to translate

0- install [gnu gettext](https://www.gnu.org/software/gettext/) to access msgfmt, xgettext,  msgmerge tools


1- create/update language .po file
```bash
make LANG=fa makemessages
```

2- translate messages in ```locales/fa/LC_MESSAGES/messages.po```

3- compile translation to .mo file
```bash
make LANG=fa compilemessages
```

### Run the app
```bash
python app.py
```

### and here is an extremely sophisticated functional test:

```curl
curl -X 'GET' \
  'http://127.0.0.1:8000/' \
  -H 'accept: application/json' \
  -H 'accept-language: fa'
```

- response should be like this

```json
[
  "سلام دنیا",
  "بله",
  "خیر",
  "خاک بر سر اسرائیل از خدا بی‌خبر :هندونه:"
]
```
