# MarketPulse: Real-Time Finance Engine

![Type](https://img.shields.io/badge/Type-Personal_Project-blue)
![Status](https://img.shields.io/badge/Status-Active_Deployment-green)

**MarketPulse: An end-to-end data engineering project featuring a robust Python pipeline, local JSON caching for API optimization, and a SQL-backed historical data warehouse.**

## System Architecture

### [Phase 1: API to JSON](https://github.com/afreenportfolio/market-pulse-real-time-finance-engine/tree/api-to-json)

Engineered a secure Python ingestion script to fetch real-time Alpha Vantage data and optimize API usage via local JSON caching.
- Tech Stack: `Python`, `Alpha Vantage API`, `python-dotenv` (Security), `JSON`

### [Phase 2: Data Pipeline](https://github.com/afreenportfolio/market-pulse-real-time-finance-engine/tree/data-pipeline)

Developed a robust parsing engine to navigate nested time-series dictionaries and extract critical OHLCV metrics for processing.
- Tech Stack: `Python`, `JSON Parsing`, `Dictionary Mapping`

### [Phase 3: MySQL Integration](https://github.com/afreenportfolio/market-pulse-real-time-finance-engine/tree/mysql-integration)

Architected a relational database schema using DECIMAL types for financial accuracy and `ON DUPLICATE KEY UPDATE` logic for data integrity.
- Tech Stack: `MySQL`, `mysql-connector-python`, `Relational Schema Design`, `.env`

### [Phase 4: Stock Analysis](https://github.com/afreenportfolio/market-pulse-real-time-finance-engine/tree/stock_analysis)

Built a financial logic engine to calculate 5-day Moving Averages and generate actionable `BUY/SELL` crossover signals.
- Tech Stack: `Pandas` (Data Analysis), `SQL (INNER JOIN)`, `Financial Logic Modeling`

## License
- MIT License
