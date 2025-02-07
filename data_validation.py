from pydantic import BaseModel, Field, model_validator
from datetime import datetime

class StockData(BaseModel):
    ticker: str = Field(alias="T",
                        default="")
    
    date: str = Field(alias="t",
                      default="")
    
    volume_weighted_avg_price: float = Field(alias="vw", 
                                             default=0.0)
    
    open_price: float = Field(alias="o", 
                              default=0.0)
    
    close_price: float = Field(alias="c", 
                               default=0.0)
    
    volume: float = Field(alias="v",
                          default=0.0)
    
    high_price: float = Field(alias="h", 
                              default=0.0)
    
    low_price: float = Field(alias="l", 
                             default=0.0)
    
    number_of_trades: int = Field(alias="n", 
                                  default=0)

    data_ingestion_timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @model_validator(mode='before')
    def validate_data(cls, values):
        if "t" in values:
            try:
                timestamp = int(values["t"] / 1000)  # Convert milliseconds to seconds
                values["t"] = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            except Exception as e:
                raise ValueError(f"Invalid timestamp: {values['t']}. Error: {e}")
        return values
