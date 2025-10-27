import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    data = []
    unique_stations = []

    # Read CSV file
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            # Checks if not already processed (as each station entry has mutliple coords points in the data)
            station_key = row['stop_name']
            if station_key not in unique_stations:
                unique_stations.append(station_key)
                data.append(row)

    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    print(f"Converted '{csv_file_path}' to '{json_file_path}'")


if __name__ == "__main__":
    input_file = "stops.txt"      # I
    output_file = "stops.json"    # O

    csv_to_json(input_file, output_file)
