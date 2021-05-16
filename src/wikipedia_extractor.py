import wptools as wptools
from src.constansts import *


def extract_wikipedia_descriptions(wikidata_code, language):
    art_wiki_descriptions = []
    if API_ES in language:
        art_wiki_descriptions.append(get_info_from_wikidata(wikidata_code, LANG_ES))
    if API_EN in language:
        art_wiki_descriptions.append(get_info_from_wikidata(wikidata_code, LANG_EN))
    if API_FR in language:
        art_wiki_descriptions.append(get_info_from_wikidata(wikidata_code, LANG_FR))
    if API_IT in language:
        art_wiki_descriptions.append(get_info_from_wikidata(wikidata_code, LANG_IT))
    return art_wiki_descriptions


def get_info_from_wikidata(wikidata_code, lang):
    skip_request = [WPR_CLAIMS, WPR_IMAGE_INFO, WPR_LABELS, WPR_PARSE, WPR_RANDOM]
    return wptools \
        .page(wikibase=wikidata_code, lang=lang, skip=skip_request, silent=True, verbose=False) \
        .get() \
        .data[WPT_TEXT]
