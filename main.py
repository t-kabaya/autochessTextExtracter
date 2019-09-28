from flask import escape

# from extract_text_from_image import detect_text_uri
# from create_level_and_position_y_map import create_level_and_position_y_map
# from filter_by_synergy_name import filter_by_synergy_name
# from classify_texts_by_player import classify_texts_by_player

# image_uri = 'https://firebasestorage.googleapis.com/v0/b/ipgpushnotifmasterserver.appspot.com/o/Screenshot_20190917-101012.jpg?alt=media&token=bb3fa819-ebfa-41db-84ed-1faa4083f1e2'

# def index(request):
#   extracted_texts = detect_text_uri(image_uri)
#   # use lv position as player position y
#   level_position_dictionary = create_level_and_position_y_map(extracted_texts)
#   classified_result = classify_texts_by_player(extracted_texts, level_position_dictionary)

#   # TMP: show results in console
#   response = filter_by_synergy_name(classified_result)

#   return response

# データ構造がどのようになっているかの確認。
def debug_just_return_request_as_response(request):
  return request