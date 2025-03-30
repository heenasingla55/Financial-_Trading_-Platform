
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# In-memory data structure to hold market data
market_data = {
    "Market1": {"symbol": "MKT1", "price": 150.25},
    "Market2": {"symbol": "MKT2", "price": 2800.50},
    "Market3": {"symbol": "MKT3", "price": 3450.80},
}

# Data model for market data
class MarketData(BaseModel):
    symbol: str
    price: float

# Route to get market data by symbol
@app.get("/api/marketdata/{symbol}", response_model=MarketData)
async def get_market_data(symbol: str):
    if symbol in market_data:
        return market_data[symbol]
    else:
        return {"symbol": symbol, "price": 0.0}  # Return 0.0 if symbol not found

# Route to update market data
@app.post("/api/marketdata/")
async def update_market_data(market_data: MarketData):
    market_data_dict = market_data.dict()
    symbol = market_data_dict["symbol"]
    price = market_data_dict["price"]
    market_data[symbol] = {"symbol": symbol, "price": price}
    return market_data[symbol]
