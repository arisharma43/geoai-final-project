import pandas as pd
import os

# Define the data directory
data_dir = "../data/small/census"

# List of census files to process
census_files = [
    "ACSDT5YSPT2010.B01003-Data.csv",
    "ACSDT5YSPT2015.B01003-Data.csv",
    "ACSDT5YSPT2021.B01003-Data.csv",
]


def clean_census_file(filepath):
    """
    Clean census data file:
    1. Rename 'Geography' column to 'GEOID'
    2. Remove prefix from GEOID values (e.g., '0500000US48201' -> '48201')
    """
    print(f"\nProcessing: {os.path.basename(filepath)}")

    # Read the CSV, skipping the first row (which contains descriptions)
    df = pd.read_csv(filepath, skiprows=1)

    # Rename Geography to GEOID
    if "Geography" in df.columns:
        df.rename(columns={"Geography": "GEOID"}, inplace=True)
        print(f"  ✓ Renamed 'Geography' to 'GEOID'")
    elif "GEO_ID" in df.columns:
        df.rename(columns={"GEO_ID": "GEOID"}, inplace=True)
        print(f"  ✓ Renamed 'GEO_ID' to 'GEOID'")

    # Clean GEOID values - remove prefix
    if "GEOID" in df.columns:
        # Remove everything before and including 'US'
        df["GEOID"] = df["GEOID"].str.replace(r"^.*US", "", regex=True)
        print(f"  ✓ Cleaned GEOID values (removed prefix)")
        print(f"  Sample GEOIDs: {df['GEOID'].head(3).tolist()}")

    # Display info
    print(f"  Rows: {len(df)}")
    print(f"  Columns: {list(df.columns)}")

    return df


# Process each census file
for filename in census_files:
    filepath = os.path.join(data_dir, filename)

    if os.path.exists(filepath):
        # Clean the data
        df_cleaned = clean_census_file(filepath)

        # Save the cleaned data (overwrite original or save to new location)
        # Option 1: Overwrite original
        # df_cleaned.to_csv(filepath, index=False)

        # Option 2: Save to processed folder
        output_dir = "../data/processed/census"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"cleaned_{filename}")
        df_cleaned.to_csv(output_path, index=False)
        print(f"  ✓ Saved to: {output_path}")
    else:
        print(f"\n⚠ File not found: {filepath}")

print("\n" + "=" * 70)
print("✅ Census data cleaning complete!")
print("=" * 70)
