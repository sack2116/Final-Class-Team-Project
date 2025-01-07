import csv
import os

def split_csv(file_path, chunk_size, output_dir):
    """
    Splits a CSV file into chunks.
    
    :param file_path: Path to the input CSV file.
    :param chunk_size: Number of rows per chunk.
    :param output_dir: Directory to save the chunk files.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Extract the header row
        
        chunk_index = 0
        rows = []
        for row in reader:
            rows.append(row)
            if len(rows) == chunk_size:
                chunk_file = os.path.join(output_dir, f'chunk_{chunk_index}.csv')
                write_csv(chunk_file, header, rows)
                chunk_index += 1
                rows = []
        
        # Write remaining rows
        if rows:
            chunk_file = os.path.join(output_dir, f'chunk_{chunk_index}.csv')
            write_csv(chunk_file, header, rows)


def join_csv(output_dir, output_file):
    """
    Joins CSV chunks back into a single file.
    
    :param output_dir: Directory containing the chunk files.
    :param output_file: Path to save the joined CSV file.
    """
    files = sorted(f for f in os.listdir(output_dir) if f.endswith('.csv'))
    
    with open(output_file, mode='w', newline='', encoding='utf-8') as joined_file:
        writer = None
        
        for file in files:
            with open(os.path.join(output_dir, file), mode='r', newline='', encoding='utf-8') as chunk_file:
                reader = csv.reader(chunk_file)
                header = next(reader)  # Get the header row
                
                if writer is None:
                    writer = csv.writer(joined_file)
                    writer.writerow(header)
                
                for row in reader:
                    writer.writerow(row)


def write_csv(file_path, header, rows):
    """
    Writes rows to a CSV file with a given header.
    
    :param file_path: Path to the output CSV file.
    :param header: Header row.
    :param rows: Data rows.
    """
    with open(file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        writer.writerows(rows)

def main():
    while True:
        print("\nCSV Utility Menu:")
        print("1. Split CSV File")
        print("2. Join CSV Chunks")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            # Split CSV
            file_path = input("Enter the path to the CSV file to split: ").strip()
            chunk_size = int(input("Enter the number of rows per chunk (excluding header): ").strip())
            output_dir = input("Enter the directory to save the chunks: ").strip()

            try:
                split_csv(file_path, chunk_size, output_dir)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            # Join CSV
            output_dir = input("Enter the directory containing the CSV chunks: ").strip()
            output_file = input("Enter the path to save the joined CSV file: ").strip()

            try:
                join_csv(output_dir, output_file)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            # Exit
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()