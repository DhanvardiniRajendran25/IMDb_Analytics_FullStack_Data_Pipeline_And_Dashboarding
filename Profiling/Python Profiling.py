# Install necessary libraries (Run in terminal first: pip install pandas ydata-profiling)
import pandas as pd
import os
from ydata_profiling import ProfileReport

# Define file path (Make sure to use 'r' to avoid escape sequences)
file_path = r"D:\NEU\SPRING 2025\DAMG 7370 - Designing Advanced Data Architectures for Business Intelligence\Midterm Project - IMDB\name.basics.tsv"

# Check if the file exists
if not os.path.exists(file_path):
    print("❌ Error: File not found! Check the file path.")
else:
    print("✅ File found. Proceeding with data loading...")

    # Load the dataset
    df = pd.read_csv(file_path, sep='\t', low_memory=False)
    
    # Display first few rows to verify data
    print(df.head())

    # Generate profile report
    profile = ProfileReport(df, title="IMDB Data Profiling Report")

    # Define output path for the report
    output_path = r"D:\NEU\SPRING 2025\DAMG 7370 - Designing Advanced Data Architectures for Business Intelligence\Midterm Project - IMDB\name_basics_report.html"
    
    # Save the report as an HTML file
    profile.to_file(output_path)

    print(f"✅ Report Generated Successfully! Saved at: {output_path}")
