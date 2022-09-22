import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Love Page", page_icon=":hibiscus:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_b0cdvgnr.json")
foto_1= Image.open("images/foto1.jpeg")
foto_2= Image.open("images/foto2.jpeg")
foto_3= Image.open("images/foto3.jpeg")
foto_4= Image.open("images/foto4.jpeg")



# ---- HEADER SECTION ----
with st.container():
    st.subheader("Aslan Parçası ve Koçumm Sayfası 💙 💜")
    st.title("Güzelim :point_right: Ebrar'ım")
    st.write(
        "Aslan parçası adlı Güzelim için hazırlanan bir sayfadır. Başka hanfendiler giremez."
    )

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Neden Hazırladım")
        st.write("##")
        st.write(
            """
            Neden aslan parçası için web sitesi yazdım:
            - Kodlama biliyorum (çok hawli).
            - Yani napaydım sadece emoji filan mi ataydım.
            - Çok seviyommmmm.
            - Bir de üstüne sürekli yeni şeyler ekleyebilirimmm
            - Sonraki buluşmaya kadar özlem giderebiliriz. 
            """
        )

    with right_column:
        st_lottie(lottie_coding, height=450, key="coding")

with st.container():
    image_1, image_2 = st.columns((2, 2))
    with image_1:
        st.image(foto_1)
        st.image(foto_2)
    with image_2:
        st.image(foto_3)
        st.image(foto_4)


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Adınız 'Aslan Parçası', 'Güzelim' veya 'Bir tanem' ise Koçum'a ulaşabilirsiniz.")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/suleymankaplan7254@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
