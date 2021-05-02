import wptools as wptools
from src.constansts import *


def extract_wikipedia_descriptions(wikidata_code):
    art_wiki_description_es = get_info_from_wikidata(wikidata_code, LANG_ES)
    art_wiki_description_en = get_info_from_wikidata(wikidata_code, LANG_EN)
    art_wiki_description_fr = get_info_from_wikidata(wikidata_code, LANG_FR)
    art_wiki_description_it = get_info_from_wikidata(wikidata_code, LANG_IT)
    return [art_wiki_description_es, art_wiki_description_en, art_wiki_description_fr, art_wiki_description_it]


def get_info_from_wikidata(wikidata_code, lang):
    skip_request = [WPR_CLAIMS, WPR_IMAGE_INFO, WPR_LABELS, WPR_PARSE, WPR_RANDOM, WPR_RESTBASE]
    return wptools \
        .page(wikibase=wikidata_code, lang=lang, skip=skip_request, silent=True, verbose=False) \
        .get() \
        .data[WPT_LEAD]
