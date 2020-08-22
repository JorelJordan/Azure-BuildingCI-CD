import random
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(5, 9)

     url = 'https://ci-cd-appservice.azurewebsites.net'
    def index_page(self):
     
    response = requests.get(url)
    assert response.status_code == 200


    def predict(self):
        data = random.randint(1, 10000)
         response = requests.post(url, data)
        self.client.post("/predict",json={  
   "CHAS":{  
      "0":0
   },
   "RM":{  
      "0":6.575
   },
   "TAX":{  
      "0":296.0
   },
   "PTRATIO":{  
      "0":15.3
   },
   "B":{  
      "0":396.9
   },
   "LSTAT":{  
      "0":4.98
   }
})