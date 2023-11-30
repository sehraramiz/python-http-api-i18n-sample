from fastapi import FastAPI, Header, Request

import i18n


app = FastAPI()


@app.middleware("http")
async def set_locale(request: Request, call_next):
    lang = request.headers.get("accept-language", "en")
    i18n.set_lang_code(lang)
    response = await call_next(request)
    response.headers["Content-Language"] = lang
    return response


@app.get("/")
def index(accept_language: str = Header()) -> list[str]:
    return [
        i18n.gettext("Hello World"),
        i18n.gettext("yes"),
        i18n.gettext("no"),
        i18n.gettext("Free Palestine :watermelon:"),
    ]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", reload=True)
