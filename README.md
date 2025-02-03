# E-commerce Data Models

This repository contains SQL and NoSQL data models for an e-commerce application. It demonstrates two approaches to data modeling: a relational model using PostgreSQL and a document model using MongoDB. The project includes schema definitions, sample data scripts, and Python-based data ingestion scripts.

## Overview

- **SQL-Relational Model:**  
  Designed for PostgreSQL, this model features normalized tables for users, products, orders, and order items. It includes Docker Compose configurations for both PostgreSQL and pgAdmin, SQL scripts to create schemas and insert sample data, and a Python script to ingest CSV data.

- **NoSQL-Document Model:**  
  Designed for MongoDB, this model uses denormalized documents to represent e-commerce data. It includes Docker Compose configurations for MongoDB and Mongo Express, JSON files with sample documents, and a Python script to ingest JSON data.
  


## Prerequisites

- **Docker & Docker Compose:** Ensure you have Docker and Docker Compose installed.
- **Python 3.8+ Libraries:**  
  - For SQL ingestion: `pandas`, `SQLAlchemy`, `psycopg2-binary`  
  - For NoSQL ingestion: `pandas`, `pymongo` (or equivalent)

## Setup and Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/ecommerce-data-models.git
   cd ecommerce-data-models
   ```
