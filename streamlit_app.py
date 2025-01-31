# Streamlitライブラリをインポート
import streamlit as st
import random

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

# タイトルを設定
st.title('恋御籤♥')

# テキスト入力ボックスを作成し、ユーザー♥からの入力を受け取る
user_input = st.text_input('あなたの名前を入力してください')
gender = st.radio("性別を選択してください", ["男性", "女性"])

# ボタンを作成し、クリックされたらメッセージを表示
if st.button('参拝方法'):
    if user_input:  # 名前が入力されているかチェック
        st.success(f' こちらでは恋にまつわるおみくじを引くことができます。大凶、凶、大吉の中から{user_input}さん!の運勢をうらないます。')  # メッセージをハイライト
    else:
        st.error('名前を入力してください。')  # エラーメッセージを表示


  
# スライダーを作成し、値を選択
if st.button("運勢を占う"):
    def omikuji():
        fortunes = ["大吉　確実に何かいいことが起こるチャンスが穴やに与えられます。そのチャンスをつかむのはあなた次第ですが、つかむ姿勢さえあればあなたの恋は成就します。",
                    "凶　何をやっても空回り。何もしないほうがいいです。",
                    "凶　何も行動しないあなたは何かしらしたほうがいいでしょう。うまくいくほしょうはありませんが、何もしないよりましです。",
                    "凶　そろそろ幸運な時も終わりです。悪いことが起きます",
                    "大凶",
                    "大凶",
                      "大凶"]
        return random.choice(fortunes)
    result = omikuji()
    st.write("あなたの運勢は「{result}」")

