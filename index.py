import re
import json
from extract_text_from_image import detect_text_uri
from create_level_and_position_y_map import create_level_and_position_y_map
from filter_by_synergy_name import filter_by_synergy_name

extracted_texts = detect_text_uri('https://firebasestorage.googleapis.com/v0/b/ipgpushnotifmasterserver.appspot.com/o/Screenshot_20190917-101012.jpg?alt=media&token=bb3fa819-ebfa-41db-84ed-1faa4083f1e2')
print(extracted_texts)

# カタカナにマッチ。
re_katakana = re.compile(r'[\u30A1-\u30F4]+')

level_position_dictionary = create_level_and_position_y_map(extracted_texts)

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

  for text in extracted_texts:
    synergy_name = text.description
    for vertex in text.bounding_poly.vertices:
      y = vertex.y
      if (y < level_position_dictionary['player1']):
        players_text_list['player1'].append(synergy_name)
      elif (level_position_dictionary['player1'] < y & y < level_position_dictionary['player2'] ):
        players_text_list['player2'].append(synergy_name)
      elif (level_position_dictionary['player2'] < y & y < level_position_dictionary['player3']):
        players_text_list['player3'].append(synergy_name)
      elif (level_position_dictionary['player3'] < y & y < level_position_dictionary['player4']):
        players_text_list['player4'].append(synergy_name)
      elif (level_position_dictionary['player4'] < y & y < level_position_dictionary['player5']):
        players_text_list['player5'].append(synergy_name)
      elif (level_position_dictionary['player5'] < y & y < level_position_dictionary['player6']):
        players_text_list['player6'].append(synergy_name)
      elif (level_position_dictionary['player6'] < y & y < level_position_dictionary['player7']):
        players_text_list['player7'].append(synergy_name)
      elif (level_position_dictionary['player7'] < y & y < level_position_dictionary['player8']):
        players_text_list['player8'].append(synergy_name)

  return players_text_list

classified_result = classify_texts_by_player(extracted_texts, level_position_dictionary)

# コンソールで表示
filter_by_synergy_name(classified_result)