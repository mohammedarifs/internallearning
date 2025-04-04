# read_config.py
import yaml
import os


def export_variable():
    with open('./projectconfig.yaml', 'r') as file:
        config = yaml.safe_load(file)
        test_data_create_flag = config.get('test_data_create_flag')

        # Export as environment variable

        print(f"::set-output name=test_data_create_flag::{test_data_create_flag}")
        print("--",test_data_create_flag)
if __name__ == "__main__":
    export_variable()
