# 🎬 Netflix Data Project

A comprehensive Exploratory Data Analysis (EDA) on Netflix's content catalog — uncovering insights into popular shows, top actors, genre trends, revenue patterns, and more through data cleaning, feature engineering, and rich visualizations.

---

## 📌 Project Overview

Netflix hosts thousands of titles across hundreds of countries and genres. This project digs deep into Netflix's dataset to answer key questions such as:

- Which shows and movies are the most popular on Netflix?
- Who are the most frequently appearing actors on the platform?
- How has Netflix's content library grown over time?
- What genres dominate the platform and across which regions?
- What does Netflix's revenue trend look like?

The analysis combines data wrangling, feature engineering, and a variety of visualization techniques to surface meaningful, business-relevant insights from raw data.

---

## 📁 Repository Structure

```
Netflix-Data-Project/
└── Netflix_Data_Project/
    ├── data/                   # Raw Netflix dataset (CSV)
    ├── notebooks/              # Jupyter Notebooks with full EDA
    ├── visuals/                # Exported charts and plots
    └── README.md
```

---

## 🔧 Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3.x** | Core programming language |
| **Pandas** | Data manipulation and cleaning |
| **NumPy** | Numerical operations |
| **Matplotlib** | Base plotting library |
| **Seaborn** | Statistical visualizations (heatmaps, distplots) |
| **WordCloud** | Text-based visual analysis of titles and genres |
| **Jupyter Notebook** | Interactive analysis environment |

---

## 🔍 Key Analyses Performed

### 🧹 Data Cleaning & Preprocessing
- Handled missing values across director, cast, country, and date columns
- Parsed and converted `date_added` to datetime format
- Split multi-valued columns (genres, cast) for granular analysis
- Removed duplicates and standardized categorical fields

### ⚙️ Feature Engineering
- Extracted `year_added` and `month_added` from date fields
- Derived content age (years since release vs. year added to Netflix)
- Created binary `type` flag (Movie vs. TV Show)
- Counted cast size and number of genres per title

### 📊 Visualizations
- **Bar Plots** — Top countries by content volume, most prolific directors
- **Heatmaps** — Correlation between features; content additions by month/year
- **Distplots** — Distribution of movie durations and TV show seasons
- **Word Clouds** — Most frequent words in titles, genres, and cast names
- **Line Charts** — Netflix revenue growth over time
- **Count Plots** — Content type breakdown (Movies vs. TV Shows)

---

## 📈 Key Insights

- The **United States** and **India** contribute the highest volume of Netflix content
- **Drama** and **International Movies** are the most dominant genres on the platform
- Netflix saw an exponential surge in content additions between **2016 and 2020**
- A small set of actors appear across a disproportionately large number of titles
- The majority of Netflix movies fall in the **90–120 minute** duration range
- Netflix's global revenue has grown consistently year-over-year, driven by subscriber expansion

---

## 🚀 Getting Started

### Prerequisites

Install the required Python libraries:

```bash
pip install pandas numpy matplotlib seaborn wordcloud jupyter
```

### Running the Project

1. **Clone the repository**

```bash
git clone https://github.com/AADITYA-NAHAR-JAIN/Netflix-Data-Project.git
cd Netflix-Data-Project/Netflix_Data_Project
```

2. **Launch Jupyter Notebook**

```bash
jupyter notebook
```

3. Open the notebook and run all cells sequentially to reproduce the full analysis.

---

## 📦 Dataset

The project uses the **Netflix Movies and TV Shows** dataset, widely available on [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows). It contains metadata on 8,000+ titles including:

- `title`, `type`, `director`, `cast`
- `country`, `date_added`, `release_year`
- `rating`, `duration`, `listed_in` (genres)
- `description`

---

## 🤝 Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create your branch (`git checkout -b feature/new-insight`)
3. Commit your changes (`git commit -m 'Add new visualization'`)
4. Push to your branch (`git push origin feature/new-insight`)
5. Open a Pull Request

---

## 👤 Author

**Aaditya Nahar Jain**
- GitHub: [@AADITYA-NAHAR-JAIN](https://github.com/AADITYA-NAHAR-JAIN)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
