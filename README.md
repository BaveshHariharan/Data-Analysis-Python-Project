# Data-Analysis-Python-Project
Python data analytics program that reads a CSV file and generates statistical insights on student vs non-student engagement, platform usage, and age-income similarity.
The script extracts and processes the dataset to produce four outputs:
  SEPARATED USERS INTO STUDENTS AND NON-STUDENTS:
    *Stores their age, time spent, and engagement score
  CALCULATES PLATFORM ENGAGEMENT STATISTICS: 
    *Total engagement
    *Average engagement
    *Standard deviation per platform
  COMPUTED SIMILARITY BETWEEN AGE AND INCOME: 
    *Uses a custom cosine similarity function
    *Returns similarity scores for students vsnon-students
  PERFORMS STATISTICAL COMPARISON OF ENGAGEMENT: 
    *Cohen’s d effect size (graceful termination if incorrect)
