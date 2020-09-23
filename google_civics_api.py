from config import CIVICS_API_KEY
import requests

class GoogleCivicsApi:
  
  def get_officials(self):
    url = self.create_api_url()
    r = requests.get(url=url)
    print(url)
    print(r.json())
  
  def create_api_url(self):
    url = 'https://civicinfo.googleapis.com/civicinfo/v2/representatives?address=17110%20Simon%20Ct%2C%20Richmond%2C%20Texas%2C%2077407'
    url += '&includeOffices=true&key={api_key}'.format(api_key=CIVICS_API_KEY)
    return url

google_civics_api = GoogleCivicsApi()
google_civics_api.get_officials()