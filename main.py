import random
import csv

# Number of data points to generate
num_data_points = 10

# Define the factors and their weights
factors = {
    'Application Server Availability': {'weight': 0.25},
    'Master Storage Availability': {'weight': 0.25},
    'Slave Storage Availability': {'weight': 0.25},
    'Synchronization Status': {'weight': 0.15},
    'Network Status': {'weight': 0.10}
}


def generate_random_status():
    return random.choice ( [ 0, 1 ] )


def calculate_fault_tolerance_score(statuses):
    score = 0
    metrics = {}  # To store metrics for each factor

    for factor, status in zip ( factors.keys (), statuses ):
        weight = factors [ factor ] [ 'weight' ]
        factor_score = weight * status
        score += factor_score
        metrics [ factor ] = {'Status': status, 'Weight': weight, 'Factor Score': factor_score}

    return score, metrics


# Generate matrix data
matrix_data = [ ]

for _ in range ( num_data_points ):
    # Generate random status for each factor
    random_statuses = [ generate_random_status () for _ in range ( len ( factors ) ) ]

    # Calculate fault tolerance score and metrics for the current statuses
    fault_tolerance_score, metrics = calculate_fault_tolerance_score ( random_statuses )

    # Add the statuses, score, and metrics to the matrix data
    matrix_data.append ( (*random_statuses, fault_tolerance_score, metrics) )

# Define the CSV file path
csv_file_path = 'fault_tolerance_metrics.csv'

# Write the generated matrix data with metrics to the CSV file
with open ( csv_file_path, mode='w', newline='' ) as csv_file:
    fieldnames = [ 'Application Server Availability', 'Master Storage Availability', 'Slave Storage Availability',
                   'Synchronization Status', 'Network Status', 'Fault Tolerance Score' ]
    writer = csv.DictWriter ( csv_file, fieldnames=fieldnames )
    writer.writeheader ()

    for data_point in matrix_data:
        statuses = dict ( zip ( factors.keys (), data_point [ :-2 ] ) )
        score = data_point [ -2 ]
        writer.writerow ( {**statuses, 'Fault Tolerance Score': score} )

print ( f"CSV file saved to {csv_file_path}" )
