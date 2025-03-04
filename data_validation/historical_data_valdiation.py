from datetime import datetime
from pydantic import BaseModel, Field, model_validator

class HistoricalData(BaseModel):
    ticker: str = Field(alias="ticker",
                        default="")

    date: str = Field(alias="date",
                      default="")

    open_price: float = Field(alias="open_price",
                              default=0.0)

    close_price: float = Field(alias="close_price",
                               default=0.0)

    volume: int = Field(alias="volume",
                          default=0)

    high_price: float = Field(alias="high_price",
                              default=0.0)

    low_price: float = Field(alias="low_price",
                             default=0.0)


    @model_validator(mode='before')
    def validate_data(cls, values):
        for field in ['open_price', 'close_price', 'high_price', 'low_price']:
            if field in values:
                value = values[field]
                if isinstance(value, str):  # Check if the value is a string
                    value = value.replace('$', '').replace(',', '').strip()  # Remove '$', ',' and whitespace
                    try:
                        values[field] = float(value)  # Convert to float
                    except ValueError:
                        raise ValueError(f"Could not convert {value} to float for {field}")

            # Convert date field to timestamp for BigQuery (format: 'YYYY-MM-DD 00:00:00')
            if "date" in values:
                try:
                    values["date"] = (datetime.strptime(values["date"], '%m/%d/%Y')).strftime('%Y-%m-%d') + ' 00:00:00'
                except Exception as e:
                    raise ValueError(f"Invalid timestamp: {values['date']}. Error: {e}")
        return values
