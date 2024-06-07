import json
import base64
import tqdm
'''
https://apps.who.int/data/mortality/api/EN/facts/query?queryJson=base64
'''
def get_data():

    with open("./req.json","r",encoding="utf-8") as f:
        parm=json.load(f)

    with open("./indicator.txt","r",encoding="utf-8") as f:
        indicators=[i.strip() for i in f.readlines()]

    with open("./region.json","r",encoding="utf-8") as f:
        region=json.load(f)

    reg_id={} # key: label

    for con in region:
        #reg_id[con['key']]=con['label']
        for reg in con['value']:
            reg_id[reg['key']]=reg['label']


    to_base64=[]

    for year in tqdm.tqdm([f'20{i}' for i in range(17,23)]):
        for indc in indicators:
            for region_key in reg_id:
                if region_key == 'AF':
                    continue
                p=parm.copy()
                p['dataFilters'][0]['values']=[indc]
                p['dataFilters'][1]['values']=[region_key]
                p['dataFilters'][2]['values']=[year]
                to_base64.append({"parm":base64.b64encode(bytes(json.dumps(p),encoding="utf-8")).decode(),"year":year,"indc":indc,"reg":region_key})
    return to_base64

if __name__=="__main__":
    import pickle
    with open("urls.pkl","wb") as f:
        pickle.dump(get_data(),f)

