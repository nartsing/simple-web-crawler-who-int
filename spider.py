import requests as req
import pickle
import tqdm
import random
def get_url(qjson, indc):
    return f'https://apps.who.int/data/mortality/api/EN/facts/query?queryJson={qjson}'

if __name__=="__main__":
    with open("./urls.pkl","rb") as f:
        urls=pickle.load(f)
    
    grasp_data=[]

    for parm in tqdm.tqdm(urls):
        url=get_url(parm['parm'], parm['indc'])
        r=req.get(url)
        try:
            grasp_data.append({"result":r.json(),"parm":parm})
        except:
            with open("./error.log","a+") as f:
                f.write(f"{parm['year']} {parm['indc']} {parm['reg']}\n")
        if random.random() <0.1:
            with open("./result.pkl","wb") as f:
                pickle.dump(grasp_data, f)
    with open("./result.pkl","wb") as f:
        pickle.dump(grasp_data, f)

print()




