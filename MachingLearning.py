from sklearn.neighbors import KNeighborsClassifier
from haversine import haversine

def get_pharmacy(longitude, latitude, user_location)
  kn=KNeighborsClassifier()
  kn.fit(longitude, latitude) #드롭다운 된 경도, 위도를 가져와야 합니다.
  kn.predict([user_location]) 
  distances, indexes=kn.neighbors([user_location])
  
  name_results=[]
  for i in indexes:
    name_results.append(name[i])
    
  address_results=[] 
  for i in indexes:
    address_results.append(gu[i]+" "+road_name_adress[i]) #사용자 주변 5개의 약국 이름, 약국 주소를 출력합니다.

  distances_results=[]
  for i in indexes:
    distances_results.append(haversine(user_location,(longitude[i],latitude[i]))+"km")
