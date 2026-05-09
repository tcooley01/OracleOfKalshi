import kalshi_python_sync
from kalshi_python_sync.models.get_markets_response import GetMarketsResponse

def get_ticker_result_pairs(limit: int = 100,
                            cursor: str = None,
                            event_ticker: str = None,
                            series_ticker: str = None,
                            tickers: str = None
                            ) -> list[tuple[str, str]]:
    
    configuration = kalshi_python_sync.Configuration(
        host = "https://external-api.kalshi.com/trade-api/v2"
    )

    client = kalshi_python_sync.KalshiClient(configuration)

    try:
        api_response = client.get_markets(
            limit=limit,
            cursor=cursor,
            event_ticker=event_ticker,
            series_ticker=series_ticker,
            tickers=tickers
        )
    
    except Exception as e:
        print(e)
        
        return None
    
    ticker_responses = [(market.ticker, market.result) for market in api_response]

    return ticker_responses