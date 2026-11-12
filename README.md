# Netflix Task 5 – Content Rating & Genre Analysis

## Input required
Place `netflix_cleaned.csv` in the same folder as the Python script. The dataset must contain:
- `type`
- `rating`
- `listed_in`

## Install dependencies
```bash
pip install -r requirements.txt
```

## Run
```bash
python task5_content_rating_genre_analysis.py
```

## Generated outputs
The script creates `task5_outputs/` containing:
- `rating_analysis.csv`
- `genre_analysis.csv`
- `ratings_by_content_type.csv`
- `rating_distribution.html`
- `top_genres.html`
- `ratings_by_content_type.html`
- `task5_business_analysis_report.txt`

Open the `.html` files in a browser to explore the interactive charts.

## Notes
- Titles with multiple genres are counted once under each listed genre.
- Content ratings are classification labels, not direct evidence of actual audience demographics.
- The analysis uses the data in your cleaned CSV; no results are fabricated.
