import requests
from flask import Blueprint, render_template, request, jsonify

joins = Blueprint(__name__, "joins")

@joins.route("/")
def join_page():
    args = request.args
    token = args.get('token')
    channel= args.get('channel')
    user_id= args.get('user_id')
    r = requests.get(f'https://api.telegram.org/bot{token}/getChatMember?chat_id={channel}&user_id={user_id}')
    d = r.json()
    b = d ['ok']
    try:
        if b == True:
            status = 'join'
            return jsonify({
                'status': status
                })
        elif b == False:
            c = d ['description']
            status = 'left'
            description = c
            return jsonify({
                'status': status ,
                'description': description
                
            })
    except Exception:
        status = 'erorr'
        return jsonify({
            'status': status
            })

