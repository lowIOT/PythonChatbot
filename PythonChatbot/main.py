import random

# 豆知識のリスト
facts = [
    "フラミンゴは片足で立つことで体温を逃がさないようにしているんだよ。",
    "世界で一番大きな砂漠は、実は南極大陸なんだ。",
    "猫のひげは、暗闇でも周りの状況を把握するのに役立っているんだよ。"
]

# ユーザーからの入力を処理する関数
def respond(user_input):
  # 簡単な挨拶に対応
  if "こんにちは" in user_input:
    return "こんにちは！何かお話したいことはありますか？"
  # 豆知識を要求された場合
  elif "豆知識" in user_input:
    return random.choice(facts)
  # その他の場合
  else:
    return "ごめんなさい、よくわかりません。他に何かお話したいことはありますか？"

# チャットボットとの会話を開始
print("チャットボット：こんにちは！何かお話したいことはありますか？")
while True:
  user_input = input("あなた：")
  response = respond(user_input)
  print("チャットボット：" + response)