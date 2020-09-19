# importing the requests library 
import requests 

class RobotInterface:
  # api-endpoint 
  robot_ip = "http://192.168.1.35:4900"
  URL = robot_ip + "/serial/sendSerial"

  def robota_gonder(self,data):
    r=request.post(URL,data)
    print(r)
