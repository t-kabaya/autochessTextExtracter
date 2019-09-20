import re
from extract_text_from_image import detect_text_uri

extracted_texts = detect_text_uri('https://firebasestorage.googleapis.com/v0/b/ipgpushnotifmasterserver.appspot.com/o/Screenshot_20190917-101012.jpg?alt=media&token=bb3fa819-ebfa-41db-84ed-1faa4083f1e2')
print(extracted_texts)

re_katakana = re.compile(r'[\u30A1-\u30F4]+')

# incrementされていく
userRank = 1

for text in extracted_texts:
  # カタカナの時のみ
  status_kata = re_katakana.fullmatch(text.description)
  if(status_kata):
    print(text.description)

  if (text.description.startswith('Lv:')):
    print(text.description)
    y = text.bounding_poly.vertices
    print(y)
    print(str(userRank) + '位')
    userRank += 1


# 「Lv」という文字の、下端のyをMapとして返す。
def create_level_and_positionY_map(extracted_texts):
  for text in extracted_texts:
    if (text.description.startswith('Lv:')):
      # 型を調べる。
      print(type(text.bounding_poly))
      vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])
      return vertices

result = create_level_and_positionY_map(extracted_texts)
print(result)

