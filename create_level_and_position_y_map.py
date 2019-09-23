# 「Lv」という文字の、下端のyをMapとして返す。
# 各ユーザーのデータをグループするためのもの。

MARGIN = 20

def create_level_and_position_y_map(extracted_texts):
  lv_text_position_list = {}
  player_count = 1

  for text in extracted_texts:
    if (text.description.startswith('Lv:')):
      # 型を調べる。
      lv_text_position_y = ( [vertex.y for vertex in text.bounding_poly.vertices])
      lv_text_position_list ['player' + str(player_count)] = max(lv_text_position_y)
      player_count += 1

  return lv_text_position_list