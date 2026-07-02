from api import fetch_users
from transform import transform_users
from file_handler import save_to_file


def main():

    data = fetch_users()

    transformed_data = transform_users(data)

    save_to_file(transformed_data)

    print("Pipeline Completed Successfully!")


if __name__ == "__main__":
    main()