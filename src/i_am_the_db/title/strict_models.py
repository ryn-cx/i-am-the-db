from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from typing import Any
from pydantic import BaseModel, Field

class TitleText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str

class OriginalTitleText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str

class TitleType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    text: str
    is_series: bool = Field(..., alias='isSeries')
    is_episode: bool = Field(..., alias='isEpisode')

class ReleaseYear(BaseModel):
    model_config = ConfigDict(defer_build=True)
    year: int
    end_year: int | None = Field(..., alias='endYear')

class ReleaseDate(BaseModel):
    model_config = ConfigDict(defer_build=True)
    day: int
    month: int
    year: int

class Runtime(BaseModel):
    model_config = ConfigDict(defer_build=True)
    seconds: int

class RatingsSummary(BaseModel):
    model_config = ConfigDict(defer_build=True)
    aggregate_rating: int | float = Field(..., alias='aggregateRating')
    vote_count: int = Field(..., alias='voteCount')

class RankChange(BaseModel):
    model_config = ConfigDict(defer_build=True)
    change_direction: str = Field(..., alias='changeDirection')
    difference: int

class MeterRanking(BaseModel):
    model_config = ConfigDict(defer_build=True)
    current_rank: int = Field(..., alias='currentRank')
    rank_change: RankChange = Field(..., alias='rankChange')

class Metascore(BaseModel):
    model_config = ConfigDict(defer_build=True)
    score: int

class Metacritic(BaseModel):
    model_config = ConfigDict(defer_build=True)
    metascore: Metascore

class Certificate(BaseModel):
    model_config = ConfigDict(defer_build=True)
    rating: str

class Genre(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    text: str

class Genres(BaseModel):
    model_config = ConfigDict(defer_build=True)
    genres: list[Genre]

class PlotText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    plain_text: str = Field(..., alias='plainText')

class Plot(BaseModel):
    model_config = ConfigDict(defer_build=True)
    plot_text: PlotText = Field(..., alias='plotText')

class PrimaryImage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    width: int
    height: int

class Country(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    text: str

class CountriesOfOrigin(BaseModel):
    model_config = ConfigDict(defer_build=True)
    countries: list[Country]

class SpokenLanguage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    text: str

class SpokenLanguages(BaseModel):
    model_config = ConfigDict(defer_build=True)
    spoken_languages: list[SpokenLanguage] = Field(..., alias='spokenLanguages')

class Season(BaseModel):
    model_config = ConfigDict(defer_build=True)
    number: int

class TotalEpisodes(BaseModel):
    model_config = ConfigDict(defer_build=True)
    total: int

class Episodes(BaseModel):
    model_config = ConfigDict(defer_build=True)
    seasons: list[Season]
    total_episodes: TotalEpisodes = Field(..., alias='totalEpisodes')

class Title(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    title_text: TitleText = Field(..., alias='titleText')
    original_title_text: OriginalTitleText = Field(..., alias='originalTitleText')
    title_type: TitleType = Field(..., alias='titleType')
    release_year: ReleaseYear = Field(..., alias='releaseYear')
    release_date: ReleaseDate = Field(..., alias='releaseDate')
    runtime: Runtime | None
    ratings_summary: RatingsSummary = Field(..., alias='ratingsSummary')
    meter_ranking: MeterRanking | None = Field(..., alias='meterRanking')
    metacritic: Metacritic | None
    certificate: Certificate | None
    genres: Genres
    plot: Plot
    primary_image: PrimaryImage = Field(..., alias='primaryImage')
    countries_of_origin: CountriesOfOrigin = Field(..., alias='countriesOfOrigin')
    spoken_languages: SpokenLanguages = Field(..., alias='spokenLanguages')
    episodes: Episodes | None

class Data(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: Title

class ExperimentalFields(BaseModel):
    model_config = ConfigDict(defer_build=True)
    janet: list[None]
    metacritic: list[None] | None = None
    markdown: list[None] | None = None
    ratings: list[None] | None = None
    ranking: list[None] | None = None

class Fields(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title_meter_ranking: str = Field(..., alias='Title.meterRanking')

class Entitlements(BaseModel):
    model_config = ConfigDict(defer_build=True)
    fields: Fields
    in_use: bool = Field(..., alias='inUse')

class Extensions(BaseModel):
    model_config = ConfigDict(defer_build=True)
    disclaimer: str
    experimental_fields: ExperimentalFields = Field(..., alias='experimentalFields')
    entitlements: Entitlements

class TitleModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    data: Data
    extensions: Extensions
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
