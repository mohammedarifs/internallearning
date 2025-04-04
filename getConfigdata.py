# read_config.py
import yaml
import os


def export_variable():
    with open('./projectconfig.yaml', 'r') as file:
        config = yaml.safe_load(file)
        test_data_create_flag = config.get('test_data_create_flag', False)

        # Export as environment variable
        os.environ['TEST_DATA_CREATE_FLAG'] = str(test_data_create_flag)
    print(os.getenv('TEST_DATA_CREATE_FLAG'))

if __name__ == "__main__":
    export_variable()
