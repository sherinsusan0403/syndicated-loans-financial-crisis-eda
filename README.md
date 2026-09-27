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



```

1. Data coverage — which countries/years have complete data
2. Univariate distributions of each ratio (log-transform if skewed)
3. Time trends — global average ratios over time, with crisis years marked
4. Cross-country comparison by income group/region
5. Crisis vs. non-crisis distribution comparison (core exploratory result)
6. Correlation between the two financing ratios, colored by crisis status
7. Event-window view for a few well-known crisis episodes

## Key Findings

1. **Financing Ratio vs. Crisis Risk:**
* Countries that rely heavily on **bank-intermediated financing** (syndicated loans) exhibit distinct banking crisis patterns compared to those leveraging **market-based financing** (corporate bond markets).
* The distribution analysis contrasts how the loan-to-GDP and bond-to-GDP ratios differ during crisis periods versus non-crisis periods.


2. **Core Exploratory Findings:**
* **Distribution Comparison:** High dependency on syndicated loans aligns with heightened vulnerability during global liquidity shocks.
* **Correlation & Crisis Status:** Correlations between loan issuance ratios and corporate bond issuance ratios show distinct clusters when colored by systemic banking crisis events.
* **Income Group Variations:** The mix of loan vs. bond financing and its correlation to crisis risk varies significantly when segmented across World Bank income groups and geographic regions.
* **Event Windows:** Historical crisis timelines highlight marked drops and shifts in loan-to-GDP ratios during major systemic banking crisis episodes.



