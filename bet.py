import orjson
import urllib3

def info():

    encoded_data = orjson.dumps({"attribute": "value"})
    http = urllib3.PoolManager()
    req = http.request("GET", "https://livescore-api.com/api-client/scores/live.json?key=iI2G5gCQFf0iDI1A&secret=uRUNBADemtPpxAbPjdwou8faoft1YvCs", body=encoded_data)

    data=orjson.loads(req.data)["data"]["match"]
    rsp="" 
    for i in data:
        if i["status"]=="IN PLAY" and int(i["time"])>=35 and int(i["time"])<=45 and i["ht_score"]=="":
            if i["score"]=="0 - 0" or i["score"]=="? - ?":
                rsp+="Se enfrentan : %s vs %s  (%s) \n Marcador : %s  (%s) \n" %(i["home_name"],i["away_name"], i["competition_name"],i["score"],i["time"])
                print("Se enfrentan : %s vs %s  (%s)" %(i["home_name"],i["away_name"], i["competition_name"]) )
                print("Marcador : %s  (%s) \n" %(i["score"],i["time"]))
    print(rsp)
    return rsp

info()