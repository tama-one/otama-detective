import streamlit as st

st.set_page_config(page_title="おたま探偵の事件簿", layout="centered")

# タイトル画面
st.title("🕵️‍♀️ おたま探偵の事件簿：5,000円紛失事件")
st.subheader("焼肉屋で起きた謎の金欠…犯人は誰！？")

# 登場人物（固定）
name1 = "もとぴー"
name2 = "こさっぴー"
name3 = "まむこちゃん"

if st.button("捜査開始！"):
    st.markdown("---")
    st.subheader("📍 事件概要")

    st.markdown(f"""
焼肉屋でおたまがトイレに行って戻ってきたら…  
**財布から5,000円が消えていた！！**  

現場にいたのはこの3人：  
- {name1}  
- {name2}  
- {name3}
    """)

    st.subheader("💬 証言")

    st.markdown(f"""
**{name1}：**「えっ！？そんなの知らないよ！ぼくはひたすらタン塩焼いてたし！」  
**{name2}：**「財布？さっき床に落ちてた500円なら拾ったけど…？」  
**{name3}：**「え〜〜知らな〜い。てか焼肉屋って現金使うんだっけ〜？」  
""")

    st.markdown("🔎 現場に残されていた謎のレシート：『ウーロン茶 x 1』")

    # 犯人を選ぶ
    suspect = st.radio("🕵️‍♀️ 誰が5,000円を盗んだ！？", [name1, name2, name3])

    if st.button("推理結果を見る"):
        if suspect == name3:
            st.success(f"🎉 正解！犯人は {name3} だった！")
            st.balloons()
        else:
            st.error(f"😱 残念…真犯人は {name3} だった！また挑戦してね！")
