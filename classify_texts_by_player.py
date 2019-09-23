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

  # MARGINとは、ユーザーが上のユーザーのシナジーを間違って取得してしまうために入れた数値
  # しかも、この箇所に置くべきではない。
  MARGIN = 20

  for text in extracted_texts:
    synergy_name = text.description
    for vertex in text.bounding_poly.vertices:
      y = vertex.y - MARGIN
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