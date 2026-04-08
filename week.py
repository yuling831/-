# import streamlit as st
# import math

# st.title("🔮 元素匹配器")

# fire_score = st.slider("你的火属性分数", 0, 10, 5)
# water_score = st.slider("你的水属性分数", 0, 10, 5)
# wind_score = st.slider("你的风属性分数", 0, 10, 5)

# user = [fire_score, water_score, wind_score]
# fire_type = [10, 4, 7]
# water_type = [4, 10, 5]
# wind_type = [7, 7, 10]
 
# if st.button("开始匹配"):
#     st.balloons()
#     dist_fire = math.sqrt((user[0] - fire_type[0]) ** 2 + (user[1] - fire_type[1])** 2 + (user[2] - fire_type[2])** 2)
#     dist_water = math.sqrt((user[0] - water_type[0]) ** 2 + (user[1] - water_type[1]) ** 2 + (user[2] - water_type[2])** 2)
#     dist_wind = math.sqrt((user[0] - wind_type[0]) ** 2 + (user[1] - wind_type[1])** 2 + (user[2] - wind_type[2])** 2)

#     min_dist = min(dist_fire, dist_fire, dist_wind)
#     if min_dist == dist_fire:
#         st.success("结果：你更接近 🔥 烈焰型")
#     elif min_dist == dist_water:
#         st.success("结果：你更接近 🌪️ 疾风型")
#     else:
#         st.success("结果：你更接近 💧 潮汐型")











# ————————————————————4.1——————————————————————————

import math
import streamlit as st

st.title("🧪 元素人格测试仪")

name = st.text_input("输入你的代号：", "见习炼金术士")

fire_score = st.slider("火属性", 0, 10, 5)
water_score = st.slider("水属性", 0, 10, 5)

user = [fire_score, water_score]

profiles = {
    "🔥 烈焰型": [10, 3],
    "💧 潮汐型": [3, 10],
    "🌪️ 平衡游侠": [7, 7],
    "🌩️ 惊雷型": [8, 4] 
}

min_dist = 999999.0
best_match = ""

if st.button("开始最终匹配"):
    for title, coords in profiles.items():
        dist = math.sqrt((user[0] - coords[0]) ** 2 + (user[1] - coords[1]) ** 2)
        st.write(f"{title} → 距离：{dist:.2f}")
        if dist < min_dist:
            min_dist = dist
            best_match = title

    st.balloons()
    st.success(f"{name}，你最接近的模板是：{best_match},最小距离为:{min_dist}")





#----------------------------4.7--------------------------------


