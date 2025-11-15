import streamlit as st
import base64
import streamlit.components.v1 as components
from streamlit_extras.let_it_rain import rain

# st.markdown("""
# <style>
# html, body, [data-testid="stAppViewContainer"] {
#     background-color: #0E1117;
#     color: #ffffff;
# }
# </style>
# """, unsafe_allow_html=True)

emoji_size = 50
falling_speed = 7
animation_length = "infinite"

def emoji1(): #f1 emoji + driving car wheel emoji
    rain(
        emoji="🏎️💪🏼",
        font_size=emoji_size,
        falling_speed=falling_speed,
        animation_length=animation_length,
    )
def emoji2(): #itachi emoji
    rain(
        emoji="㊧ɪᴛᴀᴄʜɪᴜᴄʜɪꫝᴀ࿋",
        font_size=emoji_size,
        falling_speed=falling_speed,
        animation_length=animation_length,
    )
def emoji3(): #weights emoji
    rain(
        emoji="🏋🏽🔥💪🏼🎧",
        font_size=emoji_size,
        falling_speed=falling_speed,
        animation_length=animation_length,
    )
def emoji4(): #crown soccer emoji + lawyer emoji
    rain(
        emoji="👑⚽👩‍⚖️",
        font_size=emoji_size,
        falling_speed=falling_speed,
        animation_length=animation_length,
    )

def emoji5(): #snake emoji + blue heart emoji
    rain(
        emoji="🐍💙",
        font_size=emoji_size,
        falling_speed=falling_speed,
        animation_length=animation_length,
    )

def emoji6(): #flower emoji
    rain(
        emoji="🐍🌷",
        font_size=emoji_size,
        falling_speed=falling_speed,
        animation_length=animation_length,
    )

def emoji7(): #anime emoji
    rain(
        emoji="⛩️🌸🍥",
        font_size=emoji_size,
        falling_speed=falling_speed,
        animation_length=animation_length,
    )

def emoji8(): #star emoji
    rain(
        emoji="🐍🌹",
        font_size=emoji_size,
        falling_speed=falling_speed,
        animation_length=animation_length,
    )
def emoji9(): #cigarette emoji
    rain(
        emoji="🚬",
        font_size=emoji_size,
        falling_speed=falling_speed,
        animation_length=animation_length,
    )

guest_list = {
    "anh Huy": "anh Ninh Xuân Quang Huy",
    "anh Sơn": "anh Nguyễn Lam Sơn",
    "anh Hiếu": "anh Hoàng Minh Hiếu",
    "anh Trung": "anh Nguyễn Thành Trung",
    "chị Vân Anh": "chị Trần Thị Vân Anh",
    "chị Tâm": "chị Phan Ngọc Bảo Tâm",
    "chị Ngọc": "chị Trần Hồng Bảo Ngọc",
    "chị Linh": "chị Lê Thùy Linh"
}

# Vinh's separate route data
vinh_data = {
    "key": "anh Vinh",
    "full_name": "anh Nguyễn Thế Vinh",
    "sound_file": "sound/glimpse_of_us.mp3",
    "action": emoji9
}

st.set_page_config(
    page_title="Thiệp mời lễ tốt nghiệp 🧑‍🎓",
    page_icon="🎓",
    layout="centered"
)


# CSS và header
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Satisfy&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Allura&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');


body {
    background: linear-gradient(to bottom right, #fff5e6, #e6f0ff);
    font-family: 'Segoe UI', sans-serif;
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(15px);}
    to {opacity: 1; transform: translateY(0);}
}

h1 {
    text-align: center;
    font-family: 'Great Vibes', cursive;
    font-size: 3em;
    color: #4b0082;
    text-shadow: 2px 2px 6px rgba(0,0,0,0.2);
}
h2, h3 { color: #333; }

.glow {
    animation: glowText 1s ease-in-out infinite alternate;
}
@keyframes glowText {
    from { text-shadow: 0 0 5px #ff99cc, 0 0 10px #ff66b3; }
    to { text-shadow: 0 0 20px #ff66cc, 0 0 30px #ff3399; }
}
</style>
""", unsafe_allow_html=True)



# Check for Vinh route via query parameter
query_params = st.query_params
is_vinh_route = query_params.get("guest") == "Vinh" or query_params.get("Vinh") is not None

if is_vinh_route:
    # Vinh's special route
    selected_guest = vinh_data["key"]
    sound_file = vinh_data["sound_file"]
    action = vinh_data["action"]
    guest_name = vinh_data["full_name"]
    
    with open(sound_file, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    
    # Show button for Vinh to open invitation
    start = st.button("📬 Mở thiệp")
else:
    # Regular route with dropdown
    st.markdown("<h3>Xin mời bạn chọn tên của mình để mở thiệp mời</h3>", unsafe_allow_html=True)
    
    selected_guest = st.selectbox("Bạn là", ["-- Chọn tên --"] + list(guest_list.keys()))
    b64 = ""
    
    if selected_guest != "-- Chọn tên --":
        sound_file = {
            "anh Huy": "sound/max.mp3",
            "anh Sơn": "sound/akatsuki.mp3",
            "anh Hiếu": "sound/lamine.mp3",
            "anh Trung": "sound/hala.mp3",
            "chị Vân Anh": "sound/ht2.mp3",
            "chị Tâm": "sound/lowg.mp3",
            "chị Ngọc": "sound/ngoc.mp3",
            "chị Linh": "sound/linh.mp3"
        }[selected_guest]
        action = {
            "anh Huy": emoji1,
            "anh Sơn": emoji2,
            "anh Hiếu": emoji3,
            "anh Trung": emoji4,
            "chị Vân Anh": emoji5,
            "chị Tâm": emoji6,
            "chị Ngọc": emoji7,
            "chị Linh": emoji8
        }[selected_guest]
        guest_name = guest_list[selected_guest]

        with open(sound_file, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()

        start = st.button("📬 Mở thiệp")
    else:
        start = False

if start:
    # Audio tự động phát khi mở thiệp
    music_html = f""" 
        <audio id="bgmusic" loop> <source src="data:audio/mp3;base64,{b64}" type="audio/mp3"> </audio>
        <script> document.body.addEventListener('click', function playMusic() {{ 
            var audio = document.getElementById('bgmusic'); 
            if(audio.paused){{ audio.play(); }} 
            document.body.removeEventListener('click', playMusic); 
            }}); 
        </script>

        <p onclick="document.getElementById('bgmusic').play()"
        style="
            text-align:center;
            font-size:2em;
            font-weight:700;
            color:#ff1493;
            cursor:pointer;
            animation: glow 1.8s infinite ease-in-out;
            text-shadow: 0 0 1px #ff69b4, 0 0 10px #ff69b4;
        ">
        🎵 Tap here! 🎵
        </p>
        """
    components.html(music_html, height=120)


    # Hiệu ứng
    st.balloons()
    st.snow()
    action()

    # Nội dung trong khung thiệp
    # Open the decorated invitation border so subsequent Streamlit outputs render inside it
    # Nội dung trong khung thiệp
    with st.container(border=True):
            st.markdown("<h1>🎓 Thư Mời Dự Lễ Tốt Nghiệp 🎓</h1>", unsafe_allow_html=True)

            # Phần kính gửi
            display_name = guest_name if is_vinh_route else guest_list[selected_guest]
            st.markdown(f"<h2 class='glow'>Kính gửi: {display_name}</h2>", unsafe_allow_html=True)

            # Phần giới thiệu nhân dịp tốt nghiệp
            st.write("Nhân dịp lễ tốt nghiệp của tân cử nhân", unsafe_allow_html=True)
            st.markdown("""
            <h2 style='
                text-align:center;
                font-family: "Pacifico", cursive;
                font-weight: 400;
                color:#4b0082;
            '>
                Trần Minh Khoa
            </h2>
            """, unsafe_allow_html=True)

            # Phần nội dung chi tiết
            display_name = guest_name if is_vinh_route else guest_list[selected_guest]
            guest_key = selected_guest
            st.write(f"""
            Trân trọng kính mời **{display_name}** đến tham dự  **Lễ tốt nghiệp** - một cột mốc đánh dấu hành trình học tập và trưởng thành của tôi. 🎓  

            **⏰ Thời gian:** vào lúc 14:00 hoặc 17:30 thứ Bảy, ngày 29 tháng 11 năm 2025  
            **🏛️ Địa điểm:** Trường Đại học Bách Khoa ĐHQG TP.HCM - cơ sở 1 tại 268 Lý Thường Kiệt, phường Diên Hồng, TP.HCM

            Sự hiện diện của {guest_key} sẽ là niềm vinh dự và niềm vui to lớn cho cá nhân tôi.  
            Xin chân thành cảm ơn và mong được đón tiếp! 🌷
            """, unsafe_allow_html=True)
            st.markdown("---")
            st.markdown("**Người gửi:** Minh Khoa ❤️", unsafe_allow_html=True)

