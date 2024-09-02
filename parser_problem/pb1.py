import os
import csv
import json


def parser(spec: dict, input_file_path: str) -> list:
    """
    Parses a fixed-width file based on the provided specification.

    Parameters:
    spec (dict): A dictionary containing the specification, including column offsets, encodings, etc.
    input_file_path (str): The path to the input fixed-width file.

    Returns:
    list: A list of rows, where each row is a list of parsed fields.
    """

    output_rows = []

    if not os.path.isfile(input_file_path):
        return output_rows
    
    with open(input_file_path, "r", encoding=spec["FixedWidthEncoding"]) as file:
        # skip header
        next(file)
        for line in file:
            row = []
            start = 0
            for index in spec["Offsets"]:
                end = start + int(index)
                row.append(line[start:end].strip())
                start = end
            output_rows.append(row)

    return output_rows


if __name__ == "__main__":

    try:
        # input & output file details
        input_file_path = "./files/input.txt"
        output_file_path = "./files/output.csv"
        spec_file_path = "./files/spec.json"

        spec = None
        output_rows = None

        if os.path.isfile(spec_file_path):
            with open(spec_file_path) as f:            
                spec = json.load(f)

            output_rows = parser(spec, input_file_path)

            # write to output file
            with open(
                output_file_path, "w", encoding=spec["DelimitedEncoding"], newline=""
            ) as csvfile:
                writer = csv.writer(csvfile)
                if spec["IncludeHeader"] == "True":
                    writer.writerow(spec["ColumnNames"])
                writer.writerows(output_rows)
        else:
            print("Spec file not exists")
    except Exception as e:
        print(f"An error occurred: {e}")