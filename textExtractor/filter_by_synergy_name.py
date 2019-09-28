# -*- coding: utf-8 -*-
synergy_name_list = [
  'ディヴァイン',
  'アンデッド',
  'スピリット', 
  'ウイングス',
  'キラ',
  'ケーブ',
  'ゴブリン',
  'デーモン',
  'ドラゴン',
  'グレーシャー',
  'ドワーフ',
  'マリーン',
  'ビースト',
  'ヒューマン',

  'アサシン',
  'ウォーロック',
  'ウォリアー',
  'シャーマン',
  'デモンハント',
  'ドルイド',
  'ナイト',
  'ハンター',
  'メイジ',
  'メカニック',
  'プリースト',
]

def filter_by_synergy_name (classified_result):
  # must be  uniq value
  api_response = {}

  for key, value in classified_result.items():
    print(key)
    print(value)
    api_response[key] = []
    uniq_classified_result = set(value)
    for maybe_synergy_name in uniq_classified_result:
      if maybe_synergy_name in synergy_name_list:
        print(maybe_synergy_name)
        api_response[key].append(maybe_synergy_name)

    

  return api_response
 