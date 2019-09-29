from flask import Flask
from flask import jsonify
from flask import request
from index import create_synergy_text

app = Flask(__name__)
# 文字化け防止。flaskは、defaultではutf8をサポートしない。
app.config['JSON_AS_ASCII'] = False

# sample_image_uri = 'https://firebasestorage.googleapis.com/v0/b/ipgpushnotifmasterserver.appspot.com/o/Screenshot_20190917-101012.jpg?alt=media&token=bb3fa819-ebfa-41db-84ed-1faa4083f1e2'

# TODO: 本来は、image_uriが存在しない場合、imageが、autochess_resultの物で無かった場合に個別のエラーメッセージを返してやるのが正しい。
# GET param: image_uri: string
@app.route("/")
def extract_text_from_autochess_image():
  try:
    image_uri = request.args.get('image_uri')
    
    response = create_synergy_text(image_uri)

    return jsonify(response)
  except:
    return 'エラー　もう一度試してみてね'