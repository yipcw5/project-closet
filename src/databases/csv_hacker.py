import os
import csv

def parse_filename(filename):
    # Remove the file extension
    base_name = os.path.splitext(filename)[0]
    # Split by the hyphen
    parts = base_name.split('-')
    if len(parts) == 3:
        brand, colour, clothing_type = parts
        return brand, colour, clothing_type
    elif len(parts) == 2:
        brand, clothing_type = parts
        return brand, '', clothing_type
    else:
        return None, None, None

def generate_csv(directory, output_csv):
    with open(output_csv, mode='w', newline='') as csvfile:
        fieldnames = ['ID', 'BRAND', 'COLOUR', 'CLOTHING TYPE', 'FILENAME', 'WEAR COUNT']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        id_counter = 1

        for filename in os.listdir(directory):
            if filename.startswith('.'):
                continue # Skip hidden files and directories
            brand, colour, clothing_type = parse_filename(filename)
            if brand is None:
                print(f"Skipping file with invalid format: {filename}")
                continue

            writer.writerow({
                'ID': id_counter,
                'BRAND': brand,
                'COLOUR': colour,
                'CLOTHING TYPE': clothing_type,
                'FILENAME': filename,
                'WEAR COUNT': 0
            })
            id_counter += 1

if __name__ == "__main__":
    directory = './thumbnails'  # Directory containing the images
    output_csv = './src/databases/clothing_inventory.csv'  # Output CSV file name
    generate_csv(directory, output_csv)
    print(f"CSV file '{output_csv}' generated successfully.")