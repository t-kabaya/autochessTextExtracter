from extract_text_from_image import detect_text_uri
from create_level_and_position_y_map import create_level_and_position_y_map
from filter_by_synergy_name import filter_by_synergy_name
from classify_texts_by_player import classify_texts_by_player

def create_synergy_text(image_uri):

  extracted_texts = detect_text_uri(image_uri)
  # use lv position as player position y
  level_position_dictionary = create_level_and_position_y_map(extracted_texts)
  classified_result = classify_texts_by_player(extracted_texts, level_position_dictionary)

  # TMP: show results in console
  response = filter_by_synergy_name(classified_result)

  return response
