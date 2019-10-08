# [START gae_python37_app]
from flask import Flask
from flask import jsonify
from flask import request
from index import create_synergy_text
from error import Error

app = Flask(__name__)
# 文字化け防止。flaskは、defaultではutf8をサポートしない。
app.config['JSON_AS_ASCII'] = False

# sample_image_uri = 'https://firebasestorage.googleapis.com/v0/b/ipgpushnotifmasterserver.appspot.com/o/Screenshot_20190917-101012.jpg?alt=media&token=bb3fa819-ebfa-41db-84ed-1faa4083f1e2'

# TODO: 本来は、image_uriが存在しない場合、imageが、autochess_resultの物で無かった場合に個別のエラーメッセージを返してやるのが正しい。
# エラーが帰っているのに、successというstatusが返っている。404, 200など、status codedを
# GET param: image_uri: string
@app.route("/")
def extract_text_from_autochess_image():
  image_uri = request.args.get('image_uri')
  if image_uri is None:
    raise Error('image_uriパラメーターが必要です', status_code=410)
    
  response = create_synergy_text(image_uri)

  return jsonify(response)

# 例外処理
@app.errorhandler(Error)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
