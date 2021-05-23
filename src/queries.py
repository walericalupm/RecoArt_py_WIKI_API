from peewee import DoesNotExist
from src.constants import OK, NOT_FOUND, SERVER_ERROR
from src.wikipedia_extractor import extract_wikipedia_descriptions
from src.dtos import DescriptionsDTO, DescriptionDTO
from src.models import WikipediaPaintCatalog


def get_wikipedia_descriptions_by_recoart_code(recoartcode, language):
    try:
        wikipedia_paint_code = WikipediaPaintCatalog\
            .get(WikipediaPaintCatalog.RecoArtPaintCode == recoartcode)\
            .WikipediaPaintCode
        wikipedia_descriptions = extract_wikipedia_descriptions(wikipedia_paint_code, language)
        wikipedia_descriptions_dto = []
        for i in range(0, len(wikipedia_descriptions)):
            description_dto = DescriptionDTO(Language=i, Description=wikipedia_descriptions[i])
            wikipedia_descriptions_dto.insert(i, description_dto)
        wikipedia_description_dto = DescriptionsDTO(RecoArtPaintCode=recoartcode,
                                                    WikipediaPaintCode=wikipedia_paint_code,
                                                    Descriptions=wikipedia_descriptions_dto)
        return OK, wikipedia_description_dto.dict()
    except DoesNotExist:
        return NOT_FOUND, ''
    except:
        return SERVER_ERROR, ''
