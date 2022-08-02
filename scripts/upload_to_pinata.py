from pathlib import Path
import requests
import os

PINATA_BASE_URL = "https://api.pinata.cloud/"
endpoint = "pinning/pinFileToIPFS"
filepath = "./img/shiba-inu.png"
file_name = filepath.split("/")[1:][0]
header = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
}


def main():
    with Path(filepath).open("rb") as fp:
        binary_image = fp.read()
        response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (file_name, binary_image)},
            headers=header,
        )
        print(response.json())


if __name__ == "__main__":
    main()
