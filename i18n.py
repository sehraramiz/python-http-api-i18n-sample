import gettext as gettext_module
import pathlib
from contextvars import ContextVar


BASE_DIR = pathlib.PurePath(__file__).parent
localedir = BASE_DIR / "locales"
_lang_ctx_var: ContextVar[str] = ContextVar("lang_code", default="en")


def set_lang_code(lang_code: str) -> None:
    return _lang_ctx_var.set(lang_code)


def get_lang_code() -> str:
    return _lang_ctx_var.get()


def gettext(msg: str) -> str:
    lang_code = get_lang_code()
    translation = gettext_module.translation(
        "messages", localedir, languages=[lang_code]
    )
    return translation.gettext(msg)
