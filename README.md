# API → SQL Data Pipeline

A robust, automated data pipeline that pulls data from a REST API and stores it in a SQL database. Built as a 
portfolio project to demonstrate real-world data engineering skills for small business automation.

## Problem It Solves
Small businesses manually copy data from platforms (Shopify, Square, Google Sheets, etc.) into spreadsheets 
or databases. This pipeline automates that process, eliminating errors and saving hours of work every week.

## Architecture & Data Flow

```mermaid
graph LR
    A[REST API] --> B[Python Script]
    B --> C[Data Cleaning & Validation]
    C --> D[SQL Database]
    E[Scheduler] --> B
