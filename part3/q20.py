import json

if __name__ == '__main__':
    with open('./jawiki-country.json', 'r') as f:
        target_json = json.load(f)

        print(target_json)
