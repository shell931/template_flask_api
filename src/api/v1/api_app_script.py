from flask import Blueprint, jsonify, request, abort

api_app_script_bp = Blueprint('api_app_script', __name__, url_prefix='/v1')

# GET
@api_app_script_bp.route('/test_api')
def getExample():
    return jsonify({
        "status": 200,
        "message": "succes get"
    })

# GET BY ID
@api_app_script_bp.route('/test_api/<string:parameter>')
def getExampleById(parameter):
    print(parameter)
    return jsonify({
        "status": 200,
        "message": "succes get parameter received " + parameter
    })

# POST
@api_app_script_bp.route('/test_api', methods=['POST'])
def postExample():
    print("response")
    return jsonify({
        "status": 200,
        "message": "succes post.."
    })

# PUT
@api_app_script_bp.route('/test_api/<string:parameter>', methods=['PUT'])
def editExample(parameter):

    return jsonify({
        "message": " update succes",
    })

# DELETE
@api_app_script_bp.route('/test_api/<string:parameter>', methods=['DELETE'])
def deleteExample(parameter):
    
    return jsonify({
            "message": "Delete succes"
        })
    
