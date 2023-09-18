import csv

# Define the job titles for which you want to compute the average
target_job_titles = ["Data Architect", "Senior Business Analyst", "Data Scientist", "Machine Learning Engineer"]

# Create a dictionary to store the total salaries and counts for each job title
job_title_data = {title: {"total_salaries": 0, "count": 0} for title in target_job_titles}

# Open the input CSV file
with open("job_data.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    
    # Iterate through each row in the CSV file
    for row in csv_reader:
        job_title = row["job_title"]
        num_of_salaries = int(row["num_of_salaries"])
        
        # Check if the job title is in the target list
        if job_title in target_job_titles:
            # Update the total salaries and count for the job title
            job_title_data[job_title]["total_salaries"] += num_of_salaries
            job_title_data[job_title]["count"] += 1

# Compute and print the average num_of_salaries for each job title
for title in target_job_titles:
    total_salaries = job_title_data[title]["total_salaries"]
    count = job_title_data[title]["count"]
    
    if count > 0:
        average_salary = total_salaries / count
        print(f"Average num_of_salaries for {title}: {average_salary:.2f}")
    else:
        print(f"No data found for {title}")

