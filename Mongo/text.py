import sys
from bson import ObjectId
sys.path.append("Mongo")
from mongotest import insert_data 

data3 ={"ocrtext":"PickMe - Let's Get This Party","description":'dsdsdsds',"sourceurl":'',"extracteddate":'',"extracteddate":''}
insert_data(data3)