import urllib.request
import csv
import io
from typing import List, Dict, Optional

def get_exchange_rates(currency_filter: Optional[str] = None) -> List[Dict[str, str]]:
    """
    Fetches real-time exchange rates from the Bank of Taiwan.
    
    Args:
        currency_filter: Optional currency code (e.g., 'USD', 'JPY') to filter results.
                         If None, returns all currencies.
    
    Returns:
        A list of dictionaries containing exchange rate info.
        Fields: currency, cash_buy, cash_sell, spot_buy, spot_sell.
        Note: 
        - 'cash_buy': Bank buys cash from user (User sells).
        - 'cash_sell': Bank sells cash to user (User buys).
    """
    url = "https://rate.bot.com.tw/xrt/flcsv/0/day"
    try:
        with urllib.request.urlopen(url) as response:
            csv_text = response.read().decode('utf-8')
    except Exception as e:
        return [{"error": f"Failed to fetch rates: {str(e)}"}]

    results = []
    f = io.StringIO(csv_text)
    reader = csv.reader(f)
    
    # Skip header
    try:
        next(reader)
    except StopIteration:
        return []

    for row in reader:
        if not row or len(row) < 14:
            continue
        
        curr = row[0]
        
        # Filter if requested
        if currency_filter and currency_filter.upper() != curr:
            continue
            
        # Parse fields (handle dashes or empty strings as 'N/A')
        def clean(val):
            return val if val and val != '-' else 'N/A'

        data = {
            "currency": curr,
            "cash_buying": clean(row[2]), # Bank buys from you
            "cash_selling": clean(row[12]), # Bank sells to you
            "spot_buying": clean(row[3]),
            "spot_selling": clean(row[13])
        }
        results.append(data)
        
    return results
