import pandas as pd
from sqlalchemy import create_engine

# Load CSV data into a DataFrame
df = pd.read_csv('data/orders.csv')

# Create a SQLAlchemy engine
engine = create_engine('postgresql://user:password@localhost:5432/ecommerce')

# Write DataFrame to PostgreSQL table
df.to_sql('orders', engine, if_exists='append', index=False)
