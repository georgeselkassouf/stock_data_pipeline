from pydantic import BaseModel, Field, root_validator
from datetime import datetime

class StockData(BaseModel):
    ticker: str = Field(alias="T", 
                        description="Stock ticker symbol (e.g., AAPL, TSLA)", 
                        default="")
    volume_weighted_avg_price: float = Field(alias="vw", 
                                             description="Volume-weighted average price", 
                                             default=0.0)
    open_price: float = Field(alias="o", 
                              description="Opening price of the stock", 
                              default=0.0)
    close_price: float = Field(alias="c", 
                               description="Closing price of the stock", 
                               default=0.0)
    volume: int = Field(alias="v", 
                        description="Total trading volume", 
                        default=0)
    high_price: float = Field(alias="h", 
                              description="Highest price during the trading session", 
                              default=0.0)
    low_price: float = Field(alias="l", 
                             description="Lowest price during the trading session", 
                             default=0.0)
    date: str = Field(alias="t", 
                      description="Date of the stock data as timestamp", 
                      default="")
    number_of_trades: int = Field(alias="n", 
                                  description="Total number of trades executed", 
                                  default=0)

    data_ingestion_timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @root_validator
    def validate_data(cls, values):
        return values
