import requests

base_url = "https://api.inaturalist.org/v1"
taxon_id = 324726

class Program():
    def __init__(self):
        pass

    def get_observation(self):
        params = {
            "per_page": 1,
            "taxon_id": taxon_id
        }
        try: 
            response = requests.get(f"{base_url}/observations", params=params)

            if response.status_code != 200:
                raise ValueError(f"API request failed with status code {response.status_code}: {response.text}")
            
            return response.json()
        
        except ValueError as value_error:
            return value_error

if __name__ == "__main__":
    program = Program()
    result = program.get_observation()
    print(result)