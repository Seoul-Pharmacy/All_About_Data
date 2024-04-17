from sklearn.neighbors import KNeighborsRegressor
from haversine import haversine

def get_pharmacy(datas, user_latitude, user_longitude):
    
    filtered_longitude=[]
    filtered_latitude=[]
    datas_results=[]

    for i in range(len(datas)):
        filtered_longitude.append(float(datas[i]['longitude']))
        filtered_latitude.append(float(datas[i]['latitude']))
    filtered_longitude_array=np.array(filtered_longitude)
    filtered_latitude_array=np.array(filtered_latitude)

    kn=KNeighborsRegressor()

    kn.fit(filtered_latitude_array.reshape(-1,1), filtered_longitude_array.reshape(-1,1)) #드롭다운 된 경도, 위도를 통해 학습합니다.
    distances, indexes=kn.kneighbors([user_latitude])
  
    for i in indexes[0]:
        datas_results.append(datas[i])
    
    for i in indexes[0]:
        datas[i]["distance"]=(str(haversine((float(user_latitude[0]), float(user_longitude[0])),(float(datas[i]['latitude']),float(datas[i]['longitude']))))+"km") #사용자로부터 가까운 5개 약국과의 거리를 저장합니다.

    return datas_results
