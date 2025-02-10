from datetime import datetime
from pydantic import BaseModel, Field, model_validator

class TickerDetails(BaseModel):
    ticker: str = Field(alias="ticker",
                        default="")

    name: str = Field(alias="name",
                      default="")

    primary_exchange: str = Field(alias="primary_exchange",
                                  default="")

    market_cap: float = Field(alias="market_cap",
                              default=0.0)

    description: str = Field(alias="description",
                             default="")

    homepage_url: str = Field(alias="homepage_url",
                              default="")

    total_employees: int = Field(alias="total_employees",
                                 default=0)

    list_date: str = Field(alias="list_date",
                           default="")

    @model_validator(mode='before')
    def validate_data(cls, values):
        if "list_date" in values:
            values["list_date"] = datetime.strptime(values["list_date"], "%Y-%m-%d").strftime('%Y-%m-%d %H:%M:%S')
        return values
