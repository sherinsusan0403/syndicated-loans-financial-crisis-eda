"""
Reusable helpers for pulling and cleaning WDI / GFDR data via the World Bank API.

Uses the `wbgapi` package (https://pypi.org/project/wbgapi/), which wraps the
World Bank's v2 API and covers both the World Development Indicators (WDI)
and Global Financial Development (GFDR/GFDD) databases.
"""

import pandas as pd
import wbgapi as wb


GFDD_DB = 32   
WDI_DB = 2     

INDICATORS = {
    "syndicated_loans_gdp": "GFDD.DM.12",
    "corporate_bonds_gdp": "GFDD.DM.13",
    "banking_crisis_dummy": "GFDD.OI.19",
}

WDI_CONTROLS = {
    "gdp_current_usd": "NY.GDP.MKTP.CD",
    "gdp_growth_pct": "NY.GDP.MKTP.KD.ZG",
    "inflation_pct": "FP.CPI.TOTL.ZG",
}


def fetch_indicator(code: str, db: int, start_year: int = 2000, end_year: int = 2021) -> pd.DataFrame:
    df = wb.data.DataFrame(code, time=range(start_year, end_year + 1), db=db,
                            skipBlanks=True, numericTimeKeys=True)
    df = df.reset_index().melt(id_vars="economy", var_name="year", value_name=code)
    return df


def fetch_all(start_year: int = 2000, end_year: int = 2021) -> pd.DataFrame:
    frames = []
    for name, code in INDICATORS.items():
        df = fetch_indicator(code, db=GFDD_DB, start_year=start_year, end_year=end_year)
        df = df.rename(columns={code: name})
        frames.append(df.set_index(["economy", "year"]))

    for name, code in WDI_CONTROLS.items():
        df = fetch_indicator(code, db=WDI_DB, start_year=start_year, end_year=end_year)
        df = df.rename(columns={code: name})
        frames.append(df.set_index(["economy", "year"]))

    panel = pd.concat(frames, axis=1).reset_index()
    return panel


def add_country_metadata(panel: pd.DataFrame) -> pd.DataFrame:
    """
    Attach income group and region using wbgapi's economy metadata,
    and drop aggregate/regional codes so only individual countries remain.
    """
    meta = wb.economy.DataFrame()  
    meta = meta.reset_index().rename(columns={"id": "economy"})
    meta = meta[["economy", "name", "region", "incomeLevel"]]

    merged = panel.merge(meta, on="economy", how="left")
    merged = merged[merged["region"] != "Aggregates"].copy()
    return merged


def save_raw(df: pd.DataFrame, path: str = "../data/raw/panel_raw.csv") -> None:
    df.to_csv(path, index=False)


if __name__ == "__main__":
    panel = fetch_all()
    panel = add_country_metadata(panel)
    save_raw(panel)
    print(f"Saved panel with {panel.shape[0]} rows, {panel.shape[1]} columns")
