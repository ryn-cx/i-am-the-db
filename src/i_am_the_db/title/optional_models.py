from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from typing import Any
from pydantic import BaseModel, ConfigDict, Field

class TitleText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')

class OriginalTitleText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')

class TitleType(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')
    is_series: bool | Any = Field(None, alias='isSeries', union_mode='left_to_right')
    is_episode: bool | Any = Field(None, alias='isEpisode', union_mode='left_to_right')

class ReleaseYear(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    year: int | Any = Field(default=None, union_mode='left_to_right')
    end_year: int | Any = Field(None, alias='endYear', union_mode='left_to_right')

class ReleaseDate(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    day: int | Any = Field(default=None, union_mode='left_to_right')
    month: int | Any = Field(default=None, union_mode='left_to_right')
    year: int | Any = Field(default=None, union_mode='left_to_right')

class Runtime(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    seconds: int | Any = Field(default=None, union_mode='left_to_right')

class RatingsSummary(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    aggregate_rating: int | float | Any = Field(None, alias='aggregateRating', union_mode='left_to_right')
    vote_count: int | Any = Field(None, alias='voteCount', union_mode='left_to_right')

class RankChange(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    change_direction: str | Any = Field(None, alias='changeDirection', union_mode='left_to_right')
    difference: int | Any = Field(default=None, union_mode='left_to_right')

class MeterRanking(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    current_rank: int | Any = Field(None, alias='currentRank', union_mode='left_to_right')
    rank_change: RankChange | Any = Field(None, alias='rankChange', union_mode='left_to_right')

class Metascore(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    score: int | Any = Field(default=None, union_mode='left_to_right')

class Metacritic(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    metascore: Metascore | Any = Field(default=None, union_mode='left_to_right')

class Certificate(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    rating: str | Any = Field(default=None, union_mode='left_to_right')

class Genre(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')

class Genres(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    genres: list[Genre] | Any = Field(default=None, union_mode='left_to_right')

class PlotText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    plain_text: str | Any = Field(None, alias='plainText', union_mode='left_to_right')

class Plot(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    plot_text: PlotText | Any = Field(None, alias='plotText', union_mode='left_to_right')

class PrimaryImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')

class Country(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')

class CountriesOfOrigin(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    countries: list[Country] | Any = Field(default=None, union_mode='left_to_right')

class SpokenLanguage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    text: str | Any = Field(default=None, union_mode='left_to_right')

class SpokenLanguages(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    spoken_languages: list[SpokenLanguage] | Any = Field(None, alias='spokenLanguages', union_mode='left_to_right')

class Season(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    number: int | Any = Field(default=None, union_mode='left_to_right')

class TotalEpisodes(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    total: int | Any = Field(default=None, union_mode='left_to_right')

class Episodes(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    seasons: list[Season] | Any = Field(default=None, union_mode='left_to_right')
    total_episodes: TotalEpisodes | Any = Field(None, alias='totalEpisodes', union_mode='left_to_right')

class Title(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    title_text: TitleText | Any = Field(None, alias='titleText', union_mode='left_to_right')
    original_title_text: OriginalTitleText | Any = Field(None, alias='originalTitleText', union_mode='left_to_right')
    title_type: TitleType | Any = Field(None, alias='titleType', union_mode='left_to_right')
    release_year: ReleaseYear | Any = Field(None, alias='releaseYear', union_mode='left_to_right')
    release_date: ReleaseDate | Any = Field(None, alias='releaseDate', union_mode='left_to_right')
    runtime: Runtime | Any = Field(default=None, union_mode='left_to_right')
    ratings_summary: RatingsSummary | Any = Field(None, alias='ratingsSummary', union_mode='left_to_right')
    meter_ranking: MeterRanking | Any = Field(None, alias='meterRanking', union_mode='left_to_right')
    metacritic: Metacritic | Any = Field(default=None, union_mode='left_to_right')
    certificate: Certificate | Any = Field(default=None, union_mode='left_to_right')
    genres: Genres | Any = Field(default=None, union_mode='left_to_right')
    plot: Plot | Any = Field(default=None, union_mode='left_to_right')
    primary_image: PrimaryImage | Any = Field(None, alias='primaryImage', union_mode='left_to_right')
    countries_of_origin: CountriesOfOrigin | Any = Field(None, alias='countriesOfOrigin', union_mode='left_to_right')
    spoken_languages: SpokenLanguages | Any = Field(None, alias='spokenLanguages', union_mode='left_to_right')
    episodes: Episodes | Any = Field(default=None, union_mode='left_to_right')

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: Title | Any = Field(default=None, union_mode='left_to_right')

class ExperimentalFields(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    janet: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    metacritic: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    markdown: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    ratings: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    ranking: list[Any] | Any = Field(default=None, union_mode='left_to_right')

class Fields(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title_meter_ranking: str | Any = Field(None, alias='Title.meterRanking', union_mode='left_to_right')

class Entitlements(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    fields: Fields | Any = Field(default=None, union_mode='left_to_right')
    in_use: bool | Any = Field(None, alias='inUse', union_mode='left_to_right')

class Extensions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    disclaimer: str | Any = Field(default=None, union_mode='left_to_right')
    experimental_fields: ExperimentalFields | Any = Field(None, alias='experimentalFields', union_mode='left_to_right')
    entitlements: Entitlements | Any = Field(default=None, union_mode='left_to_right')

class TitleModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    data: Data | Any = Field(default=None, union_mode='left_to_right')
    extensions: Extensions | Any = Field(default=None, union_mode='left_to_right')
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
