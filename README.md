# Financial Structure and Crisis Risk

Exploring how countries' reliance on syndicated (bank) loans versus corporate
bond markets for corporate financing relates to their historical exposure to
systemic banking crises.

## Research question

Do countries that lean more heavily on bank-intermediated financing
(syndicated loans) versus market-based financing (corporate bonds) show
different patterns of banking crisis incidence?

## Data

All data comes from World Bank sources, pulled via the [World Bank API]
(https://data.worldbank.org/) using the `wbgapi` Python package.

| Indicator | Code | Source | Description |
|---|---|---|---|
| Syndicated loan issuance to GDP (%) | `GFDD.DM.12` | GFDR | New syndicated loan volume / GDP |
| Corporate bond issuance to GDP (%) | `GFDD.DM.13` | GFDR | New corporate bond volume / GDP |
| Banking crisis dummy | `GFDD.OI.19` | GFDR (Laeven & Valencia) | 1 = systemic banking crisis, 0 = none |
| GDP, GDP growth, income group | various | WDI | Context / controls |

**Coverage note:** the syndicated loan and bond issuance series (Dealogic-based)
only cover ~2000–2021 and are patchier for smaller/lower-income economies.
The EDA explicitly profiles this coverage before drawing any conclusions.

## Project structure

```
financial-structure-crisis-risk/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/              # unmodified API pulls (gitignored, regenerate via notebook 01)
│   └── processed/        # cleaned/merged panel used for analysis
├── notebooks/
│   ├── 01_data_collection.ipynb   # pull WDI + GFDR series via wbgapi
│   ├── 02_data_cleaning.ipynb     # merge, reshape to panel, handle missing data
│   ├── 03_eda.ipynb               # exploratory data analysis (see below)
│   └── 04_analysis.ipynb          # crisis vs non-crisis comparison, correlations
├── src/
│   └── data_utils.py      # reusable fetch/clean functions
└── outputs/
    └── figures/           # exported charts for README / portfolio site
```

## EDA plan (notebook 03)

1. Data coverage — which countries/years have complete data
2. Univariate distributions of each ratio (log-transform if skewed)
3. Time trends — global average ratios over time, with crisis years marked
4. Cross-country comparison by income group / region
5. Crisis vs. non-crisis distribution comparison (core exploratory result)
6. Correlation between the two financing ratios, colored by crisis status
7. Event-window view for a few well-known crisis episodes

## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook notebooks/01_data_collection.ipynb
```

## Status

Scaffold + starter notebooks generated. Run notebook 01 to pull live data
(requires internet access to the World Bank API), then work through 02 → 04.

## License

MIT
