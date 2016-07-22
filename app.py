from flask import Flask, jsonify, make_response

app = Flask(__name__)

data = [
    {
        'mobile_phone': '1310404889',
        'name': u'Ram Prayaga',
    },
    {
        'mobile_phone': '13106190965',
        'name': u'Guan Zhou',
    }
]

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
    
@app.route('/api/<string:searchMobileNumber>', methods=['GET'])
def get_task(searchMobileNumber):
    res = filter(lambda t: t['mobile_phone'] == searchMobileNumber, data)
    if len(res) == 0:
    	abort(404)
    return jsonify(res[0])

if __name__ == '__main__':
    app.run()

