from flask import Blueprint 
from skill_read.helpers import read_csv, convert_df_to_json 

skill_api = Blueprint('skill_api', __name__)

def get_meta_skills_api(file): 
    df = read_csv(filename=file) 
    df = df.dropna(axis=1)
    json_data = convert_df_to_json(df) 
    return json_data 
     

@skill_api.route("/read_skill", methods=["GET"])
def fetch_skills(): 
    filename="Skills-dataset.csv"
    data = get_meta_skills_api(filename) 
    results = {"results": data}
    return results 

