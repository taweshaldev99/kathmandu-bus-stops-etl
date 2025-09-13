# 🚌 Kathmandu Bus Stops ETL Pipeline (Data Engineering Project)

## 📌 Project Overview
This project is part of my **application for the Dlytica Data Science & Analytics Fellowship (Nepal)**.  
It demonstrates a **mini ETL (Extract → Transform → Load) pipeline** built in Python, using real-world **Kathmandu bus stop data** from OpenStreetMap.

The pipeline:
1. **Extracts** bus stop data from OpenStreetMap (Overpass API).
2. **Transforms** it into a clean dataset (removes duplicates, handles missing values).
3. **Loads** the data into an SQL database (SQLite, extendable to PostgreSQL).
4. **Performs analytics** using SQL queries.

---

## ⚙️ Tech Stack
- **Python** (Pandas, Requests, SQLite3)
- **OpenStreetMap (Overpass API)** for real data
- **SQLite** database (can be extended to PostgreSQL/MySQL)
- **VS Code** for development

---

## 📂 Project Structure
