# Underperforming Products by Region

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?logo=postgresql&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/license-unspecified-lightgrey)

A data analysis project answering a real business question: which products are underperforming, and in which regions? Built with pandas for cleaning, SQL for analysis, and Streamlit for an interactive dashboard, using the [Global Superstore](https://raw.githubusercontent.com/plotly/datasets/master/global_super_store_orders.tsv) dataset.

## Features

- Identifies underperforming Region + Sub-Category combinations by loss-making status, low margin (<10%), and below-average sales volume
- SQL-based aggregation (SQLite) of Sales/Profit/Margin by Region + Sub-Category
- Bar chart visualization of worst-performing combinations
- Interactive Streamlit dashboard with a region filter
- Key finding: Central region / Binders lost $3,349 at a -84.66% profit margin across 26 orders

## Tech Stack

- Python
- Pandas
- SQLite (SQL analysis)
- Matplotlib
- Streamlit

## Installation

```bash
git clone https://github.com/johnnnys3/underperforming-products.git
cd underperforming-products
python3 -m venv .venv
source .venv/bin/activate
pip install pandas matplotlib jupyter notebook streamlit
```

## Usage

```bash
jupyter notebook starter.ipynb   # Cleaning, SQL analysis, chart
streamlit run app.py             # Interactive dashboard
```

## Project Structure

```text
underperforming-products/
├── starter.ipynb          # Cleaning, SQL analysis, chart
├── app.py                 # Streamlit dashboard
├── global_superstore.tsv  # Raw dataset
├── superstore.db          # Cleaned data loaded into SQLite
├── top_underperformers.png
└── README.md
```

## Contributing

Contributions are welcome. Fork the repository, create a feature branch, and open a pull request describing your changes.

## License

No license specified.
