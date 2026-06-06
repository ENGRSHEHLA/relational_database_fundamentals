import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

# Connect to your database (or create in-memory database with sample data)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create student table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        major TEXT,
        age INTEGER
    )
''')

# Insert sample data from GeneralPractical_db.sql
data = [
    (1, 'Alice', 'Comp Sci', 20),
    (2, 'Bob', 'History', 22),
    (3, 'Carol', 'Politics', 21),
    (4, 'Dave', 'Math', 23),
    (5, 'Eve', 'Comp Sci', 19)
]

cursor.executemany('INSERT INTO student VALUES (?, ?, ?, ?)', data)

# Query: Count students by major
query = '''
    SELECT major, COUNT(*) as student_count
    FROM student
    WHERE major IS NOT NULL
    GROUP BY major
    ORDER BY student_count DESC
'''

df = pd.read_sql_query(query, conn)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['major'], df['student_count'], color='steelblue', edgecolor='navy', alpha=0.7)
plt.xlabel('Major', fontsize=12, fontweight='bold')
plt.ylabel('Number of Students', fontsize=12, fontweight='bold')
plt.title('Distribution of Students by Major', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()

# Save the chart
plt.savefig('Beginner_db/student_major_distribution.png', dpi=300, bbox_inches='tight')
print("✓ Bar chart saved: student_major_distribution.png")

# Display additional statistics
print("\n📊 Database Statistics:")
print(df.to_string(index=False))

# Query 2: Distribution by age group
age_query = '''
    SELECT 
        CASE 
            WHEN age < 21 THEN 'Under 21'
            WHEN age >= 21 THEN '21 and Over'
        END as age_group,
        COUNT(*) as count
    FROM student
    GROUP BY age_group
'''

df_age = pd.read_sql_query(age_query, conn)

plt.figure(figsize=(8, 6))
colors = ['#FF9999', '#66B2FF']
plt.pie(df_age['count'], labels=df_age['age_group'], autopct='%1.1f%%', 
        colors=colors, startangle=90)
plt.title('Student Distribution by Age Group', fontsize=14, fontweight='bold')
plt.tight_layout()

# Save pie chart
plt.savefig('Beginner_db/student_age_distribution.png', dpi=300, bbox_inches='tight')
print("✓ Pie chart saved: student_age_distribution.png")

conn.close()
