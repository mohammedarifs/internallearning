import numpy as np
import pandas as pd
from faker import Faker
import random
from concurrent.futures import ProcessPoolExecutor
import time
import json

# Initialize Faker
fake = Faker()
Faker.seed(42)

# Setup constants and configurations
num_records = 1_000_0
tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'FB', 'TSLA', 'NFLX']
markets = ['NYSE', 'NASDAQ', 'OTC']
trade_types = ['buy', 'sell']
order_types = ['market', 'limit', 'stop']
statuses = ['executed', 'pending', 'canceled']
currencies = ['USD', 'EUR', 'JPY']
exchanges = ['NYSE', 'NASDAQ', 'OTC']

def generate_value(column_name, sample_values=None):
    """Generate a value based on the column name or use a random sample value."""
    if sample_values:
        return random.choice(sample_values)
    elif 'id' in column_name:
        return fake.uuid4()
    elif 'date' in column_name:
        return fake.date_time_between(start_date='-5y', end_date='now').isoformat()
    elif 'volume' in column_name or 'quantity' in column_name:
        return random.randint(1, 1000)
    elif 'price' in column_name or 'value' in column_name:
        return round(random.uniform(100, 1500), 2)
    elif 'fee' in column_name or 'commission' in column_name:
        return round(random.uniform(0.1, 50), 2)
    elif 'rate' in column_name:
        return round(random.uniform(0.8, 1.2), 2)
    elif 'ticker' in column_name:
        return random.choice(tickers)
    elif 'market' in column_name:
        return random.choice(markets)
    elif 'type' in column_name:
        return random.choice(trade_types)
    elif 'status' in column_name:
        return random.choice(statuses)
    elif 'currency' in column_name:
        return random.choice(currencies)
    elif 'exchange' in column_name:
        return random.choice(exchanges)
    else:
        return fake.word()

def generate_trades(start, end, columns, sample_values_dict):
    trades = np.empty((end - start, len(columns)), dtype=object)
    for i in range(start, end):
        trade_data = {col: generate_value(col, sample_values_dict.get(col)) for col in columns}
        trades[i - start] = [trade_data[col] for col in columns]
    return trades

# Function to parallelize the data generation
def parallel_trades_generation(columns, sample_values_dict):
    chunk_size = num_records // 4  # Assumes using 4 chunks
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(generate_trades, i, i + chunk_size, columns, sample_values_dict) for i in range(0, num_records, chunk_size)]
        results = [future.result() for future in futures]
    return np.vstack(results)

if __name__ == '__main__':
    print("Started generating trade data for records:", num_records)

    start_time = time.time()  # Record the start time

    # Read column names, data types, and sample values from JSON configuration
    with open('metadata_config.json', 'r') as file:
        config = json.load(file)
    columns = [col['name'] for col in config['columns']]
    dtypes = {col['name']: col['dtype'] for col in config['columns']}
    sample_values_dict = {col['name']: col.get('sample_values') for col in config['columns']}

    # Collect the generated data

    data_array = parallel_trades_generation(columns, sample_values_dict)

    # Convert to Pandas DataFrame with specified data types
    data = pd.DataFrame(data_array, columns=columns).astype(dtypes)

    # Add line numbers
    ##data.insert(0, 'line_number', range(1, len(data) + 1))

    # Save to a CSV file with line numbers
    data.to_csv('trade_data_with_line_numbers.csv', index=False)
    end_time = time.time()  # Record the end time
    time_taken = end_time - start_time  # Calculate the time taken

    print("Completed trade data generation")
    print(f"Time taken for data generation: {time_taken:.2f} seconds")
