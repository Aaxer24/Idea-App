from flask import Flask,request

app = Flask(__name__)  # this app name must be same as the name of 'app.py'

# create the idea repository
ideas = {
    1 : {
        "id":1,
        "idea_name":"ONDC",
        "idea_description":"details about ONDC",
        "idea_author":"Adeeb"
    },
    2: {
        "id":2,
        "idea_name":"Save Soil",
        "idea_description":"details about saving soil",
        "idea_author":"Ankit Sharma"
    }
        
}

@app.get("/ideaapp/api/v1/ideas")
def get_all_ideas():
    # I need to read the query params
    idea_author = request.args.get('idea_author')
    
    if idea_author:
        idea_res={}
        # filter all idea created by this author
        for key,value in ideas.items():
            if value['idea_author']==idea_author:
                idea_res[key] = value
        return idea_res
    # logic to fetch all ideas and support query params
    
    return ideas 


'''
To add new idea 
'''
@app.post("/ideaapp/api/v1/ideas")
def create_ideas():
    
    try:
        # first read the request body
        request_body = request.get_json() # >> this represent the request body passed by the user  >> request_body is that we have written in postman
        
        # check if the idea id passed is not present already
        if request_body["id"] and request_body["id"] in ideas:
            return "idea with the same id already present",400 # 400 is error code which we will get
        
        # insert the passed idea in the ideas dictionary
        ideas[request_body["id"]] = request_body
        
        # return the response saying idea got saved
        return "idea created and saved successfully",201
    except KeyError:
        return "id is missing",400
    except:
        return "Some internal error",500
    
    
'''
To fetch idea based on id
'''
@app.get("/ideaapp/api/v1/ideas/<idea_id>") # path params (which is not constant) must be under angled bracket (<>)
def get_idea_id(idea_id):
    try:
        if int(idea_id) in ideas:
            return ideas[int(idea_id)],200
        else:
            return "idea id passed is not present",400
        
    except:
        return "Some internal error happened",500
 
 
'''To update the idea
'''
@app.put("/ideaapp/api/v1/ideas/<idea_id>")
def update_idea_id(idea_id):
    try:
        if int(idea_id) in ideas:
            ideas[int(idea_id)] = request.get_json()
            return ideas[int(idea_id)],200
        else:
            return "idea id passed is not present",400
        
    except:
        return "Some internal error happened",500
    
'''
To delet an idea
'''
@app.delete("/ideaapp/api/v1/ideas/<idea_id>")
def delete_idea_id(idea_id):
    try:
        if int(idea_id) in ideas:
            ideas.pop(int(idea_id))
            return "idea got deleted successfully"
        else:
            return "idea id passed is not present",400
        
    except:
        return "Some internal error happened",500
    
if __name__ == "__main__":
    app.run(port=8080)