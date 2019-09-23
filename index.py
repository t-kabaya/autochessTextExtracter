import re
import json
from extract_text_from_image import detect_text_uri
from create_level_and_position_y_map import create_level_and_position_y_map
from filter_by_synergy_name import filter_by_synergy_name

extracted_texts = detect_text_uri('https://firebasestorage.googleapis.com/v0/b/ipgpushnotifmasterserver.appspot.com/o/Screenshot_20190917-101012.jpg?alt=media&token=bb3fa819-ebfa-41db-84ed-1faa4083f1e2')
print(extracted_texts)

re_katakana = re.compile(r'[\u30A1-\u30F4]+')

# # incrementされていく
# userRank = 1

# for text in extracted_texts:
#   # カタカナの時のみ
#   status_kata = re_katakana.fullmatch(text.description)
#   if(status_kata):
#     print(text.description)

#   if (text.description.startswith('Lv:')):
#     print(text.description)
#     y = text.bounding_poly.vertices
#     print(y)
#     print(str(userRank) + '位')
#     userRank += 1

level_position_dictionary = create_level_and_position_y_map(extracted_texts)
print('lv_text_position_y = ' + json.dumps(level_position_dictionary))

# 処理が複雑になりそうなので、一旦player1の文字列だけ返す。
def classify_texts_by_player(extracted_texts, level_position_dictionary):
  players_text_list = {
    'player1': [],
    'player2': [],
    'player3': [],
    'player4': [],
    'player5': [],
    'player6': [],
    'player7': [],
    'player8': [],
  }
  # user['player1'].append('lol')

  text_of_player1 = []
  for text in extracted_texts:
    for vertex in text.bounding_poly.vertices:
      if (vertex.y < level_position_dictionary['player1']):
        players_text_list['player1'].append(text.description)

  return players_text_list

classified_result = classify_texts_by_player(extracted_texts, level_position_dictionary)

# コンソールで表示
filter_by_synergy_name(classified_result)