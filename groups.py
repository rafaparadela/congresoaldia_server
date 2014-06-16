from firebase import Firebase
import json
import urllib
from constants import *

def update_groups():
    gruposRef = Firebase(FIREBASE_BASE_URL+'groups')
    gruposRef.delete();

    results = json.load(urllib.urlopen(API_BASE_URL+"group/"))

    for grupo in results['objects']:
        grupoRef = Firebase(FIREBASE_BASE_URL+'groups/'+str(grupo['id']))
        grupoRef.set(grupo)


update_groups()
