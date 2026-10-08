import argostranslate.translate


def translate(text: str) -> str:
    return argostranslate.translate.translate(text, "en", "pl")
