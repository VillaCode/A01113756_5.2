import argparse
import json

def main():
    parser = argparse.ArgumentParser(description="Process product catalogue and sales records.")
    parser.add_argument("catalogue", help="Path to the product catalogue JSON file")
    parser.add_argument("sales", help="Path to the sales record JSON file")

    args = parser.parse_args()

    try:
        # Load the product catalogue
        with open(args.catalogue, 'r', encoding='utf-8') as catalogue_file:
            catalogue = json.load(catalogue_file)

        # Load the sales record
        with open(args.sales, 'r', encoding='utf-8') as sales_file:
            sales = json.load(sales_file)

        print("Catalogue and sales files loaded successfully.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except json.JSONDecodeError:
        print("Error: One of the provided files is not a valid JSON file.")

if __name__ == "__main__":
    main()
