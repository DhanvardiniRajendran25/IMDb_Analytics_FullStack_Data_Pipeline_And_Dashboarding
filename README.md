# 🎬 End-to-End BI Pipeline for IMDb Data Integration & Analytics

This project implements a **complete, production-style Business Intelligence (BI) and Data Engineering pipeline** using large-scale IMDb public datasets. The pipeline demonstrates how raw, semi-structured data can be transformed into **high-quality, analytics-ready datasets** and visualized through interactive dashboards.

The project follows **industry best practices** for data profiling, cleansing, orchestration, cloud data warehousing, and BI modeling, closely mirroring how enterprise analytics platforms are built in real organizations.

---

## 🧠 Project Motivation

Modern organizations deal with **massive volumes of heterogeneous data** originating from multiple sources. Without proper data profiling, validation, and modeling, analytics results can be misleading or unusable.

IMDb data provides an ideal real-world scenario:

* Very large datasets (≈ 200 million - millions of records)
* Semi-structured fields
* Missing and inconsistent values
* Complex relationships (titles, people, episodes, ratings)

This project solves these challenges by building a **robust, scalable BI pipeline** that ensures **data quality, reliability, and analytical usability**.

---

## 🎯 Project Objectives

* Design an **end-to-end ETL/ELT pipeline** from raw data to dashboards
* Perform **comprehensive data profiling and quality checks**
* Clean and standardize inconsistent and missing data
* Model data for **analytical performance and scalability**
* Enable **self-service BI analytics** using Power BI
* Apply **real-world data engineering and governance principles**

---

## 🧰 Technology Stack

| Layer                     | Tools Used               |
| ------------------------- | ------------------------ |
| Data Modeling             | ER Studio                |
| Data Orchestration        | Azure Data Factory (ADF) |
| Data Profiling & Cleaning | Alteryx, Python          |
| Cloud Data Warehouse      | Snowflake                |
| Analytics & Visualization | Power BI & Tableau       |

---

## 📂 Data Sources

The pipeline uses **IMDb Non-Commercial Datasets**, which are publicly available and widely used for analytics and research.

### Core Datasets Used

| Dataset Name           | What It Represents                                                                  | Key Columns                                                                              | Approx. Records | Why This Dataset Matters                                            | How It’s Used in Analytics                                                                       |
| ---------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | --------------: | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **`name.basics`**      | Master data for people involved in movies and TV (actors, directors, writers, crew) | `nconst`, `primaryName`, `birthYear`, `deathYear`, `primaryProfession`, `knownForTitles` |     ~14,195,000 | Serves as the **people dimension** across all IMDb analytics        | Used to analyze cast/crew participation, career spans, collaborations, and contribution patterns |
| **`title.basics`**     | Core metadata for movies, TV shows, shorts, and other content                       | `tconst`, `titleType`, `primaryTitle`, `startYear`, `runtimeMinutes`, `genres`           |     ~11,464,000 | Central **title dimension** for all reporting                       | Enables genre analysis, runtime trends, release-year analysis, and content-type comparisons      |
| **`title.akas`**       | Alternate titles by region, language, and market                                    | `tconst`, `title`, `region`, `language`, `isOriginalTitle`                               |     ~51,409,000 | Captures **internationalization and localization** of content       | Used to analyze global reach, regional naming patterns, and language distribution                |
| **`title.crew`**       | Directors and writers associated with each title                                    | `tconst`, `directors`, `writers`                                                         |     ~11,464,000 | Defines **creative ownership** of content                           | Supports director/writer analytics and correlation with ratings and success                      |
| **`title.principals`** | Principal cast and crew for each title                                              | `tconst`, `nconst`, `category`, `job`, `characters`                                      |     ~90,984,000 | Represents **many-to-many relationships** between titles and people | Used for cast prominence, role-based analysis, and collaboration networks                        |
| **`title.episode`**    | Episode-level data linking episodes to TV series                                    | `tconst`, `parentTconst`, `seasonNumber`, `episodeNumber`                                |      ~8,815,000 | Defines **hierarchical structure** of TV content                    | Enables season/episode analytics, series longevity, and content volume analysis                  |
| **`title.ratings`**    | Audience ratings and vote counts per title                                          | `tconst`, `averageRating`, `numVotes`                                                    |      ~1,536,000 | Provides **audience perception and popularity metrics**             | Used for rating distribution, vote-weighted scoring, and popularity analysis                     |

These datasets together contain **tens of millions of records**, requiring scalable processing and optimized storage.

---

## 🏗️ End-to-End Architecture

<img width="1265" height="871" alt="image" src="https://github.com/user-attachments/assets/56961336-cac3-4bed-bf06-b04dcba41152" />

```
IMDb Raw Data (.tsv.gz)
        ↓
Data Profiling & Validation (Alteryx / Python)
        ↓
Azure Data Factory (Pipeline Orchestration)
        ↓
Snowflake Staging Tables
        ↓
Curated Analytics Tables
        ↓
Power BI Dashboards
```

---

## 🔍 Data Profiling & Quality Assessment

Before loading data into Snowflake, extensive profiling was conducted to understand data quality issues.

### Profiling Activities

* Column-level completeness analysis
* Data type consistency checks
* Detection of invalid and illogical values
* Identification of formatting issues
* Duplicate and uniqueness validation

### Key Issues Identified

* High percentage of missing values in certain year fields
* Numeric fields stored as strings
* Placeholder values (`\N`) instead of proper NULLs
* Multi-valued attributes stored in single columns
* Logical inconsistencies (e.g., death year before birth year)

---

## 🧹 Data Cleaning & Transformation

Cleaning rules were applied consistently across datasets to ensure analytical integrity.

### Global Cleaning Rules

* Replace IMDb placeholder values (`\N`) with NULLs
* Convert numeric fields to proper integer and float types
* Trim whitespace and standardize text formatting
* Validate logical constraints
* Normalize multi-valued attributes where necessary

### Dataset-Specific Examples

#### Name Basics

* Handled missing birth and death years
* Resolved illogical year values
* Standardized profession fields

#### Title Episodes

* Converted season and episode numbers to integers
* Validated hierarchical consistency between series, seasons, and episodes

#### Title Ratings

* Ensured numeric precision for ratings and vote counts
* Optional filtering of low-vote titles to reduce analytical noise

---

## 🧱 Snowflake Data Warehouse Design

The warehouse follows a **layered architecture** to separate raw ingestion from analytics consumption.

### Staging Layer

Contains cleaned but unaggregated data:

* `stg_title_basics`
* `stg_name_basics`
* `stg_title_akas`
* `stg_title_crew`
* `stg_title_principals`
* `stg_title_episode`
* `stg_title_ratings`

### Curated Analytics Layer

Optimized for BI tools and reporting:

* **Dimensions**

  * Titles
  * People
  * Genres
  * Regions and Languages
* **Fact Tables**

  * Ratings and votes
  * Title-person relationships
  * Episode-level metrics

This design improves **query performance, maintainability, and analytical clarity**.

---

## 🔁 ETL Orchestration with Azure Data Factory

ADF pipelines handle:

* Automated ingestion of cleaned datasets
* Dependency-aware execution
* Repeatable and auditable data loads
* Error handling and re-run capability

This ensures **reliable and scalable data movement** into Snowflake.

---

## 📊 Power BI Analytics & Dashboards

Power BI dashboards are built on top of curated Snowflake tables to enable insights such as:

* Genre popularity trends over time
* Rating distributions and vote-weighted analysis
* Comparison of movies vs TV series
* TV series structure (seasons, episodes, longevity)
* International title distribution by region and language
* Cast and crew participation trends

The dashboards are designed for **self-service exploration and executive-level reporting**.

---

## 📁 Repository Structure

```
.
├── data/
│   ├── raw/
│   ├── staging/
│   └── samples/
├── profiling/
│   ├── alteryx/
│   └── python/
├── adf/
│   ├── pipelines/
│   └── datasets/
├── snowflake/
│   ├── ddl/
│   ├── stages/
│   ├── transforms/
│   └── quality_checks/
├── powerbi/
│   ├── dashboards/
│   └── model/
├── docs/
│   └── architecture.md
└── README.md
```

---

## ▶️ How to Run the Project

1. Download IMDb datasets and place them in `data/raw`
2. Profile and clean data using Alteryx or Python
3. Upload cleaned data to cloud storage
4. Execute ADF pipelines to load Snowflake staging tables
5. Run SQL transformations to build curated analytics tables
6. Connect Power BI to Snowflake and refresh dashboards

---

## ✅ Data Quality & Validation Checks

* Row count reconciliation across layers
* Primary key uniqueness validation
* Null and missing value standardization
* Data type enforcement
* Logical rule validation
* BI-level sanity checks

---

## 🔮 Future Enhancements

* Incremental and CDC-based ingestion
* Slowly Changing Dimensions (SCD-2)
* dbt-based transformation and testing
* Data observability and monitoring
* Graph analytics for cast and crew networks

---
