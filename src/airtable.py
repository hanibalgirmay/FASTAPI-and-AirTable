import requests
from dataclasses import dataclass 

@dataclass()
class Airtable:
    base_id:str
    api_key:str
    table_name:str

    def create_record(self,data={}):
        if len(data.keys()) == 0:
            return False
        endpoints = f"https://api.airtable.com/v0/{self.base_id}/{self.table_name}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "records": [
                {
                    "fields": data
                }
            ]
        }
        r = requests.post(endpoints,json=data, headers=headers)
        print(endpoints, r.json())
        return r.status_code == 200 or r.status_code == 201
