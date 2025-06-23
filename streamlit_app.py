import streamlit as st

# Valid voucher code
valid_code = "AMZLOL5M2025"

# Streamlit Page Config
st.set_page_config(page_title="Amozon Gift Redemption", page_icon="🎁")

# Title and instructions
st.title("🎁 Amozon Gift Voucher Redemption")
st.subheader("Enter your voucher code to unlock your surprise!")

# Input field
user_input = st.text_input("Voucher Code")

# Voucher Validation
if user_input:
    if user_input.strip().upper() == valid_code:
        st.success("🎉 Congratulations Bikash! You've unlocked ₹5 Million in Laughter Credits!")
        st.markdown("""
        - 🤣 Redeem with 2 Bikash-Type jokes  
        - 🧠 Bonus Riddle: Why did the gift voucher go to therapy? *It had too much emotional value.*  
        - 💼 Bonus Riddle: What do you call a joke that's a financial asset? *A pun-damental investment.*  
        - 📊 Bonus Riddle: Why did the accountant bring a ladder to work? *To climb the corporate balance sheet.*  
        - 📅 Valid until: 24th June 2026  
        """)
    else:
        st.error("❌ Invalid code! Either your sense of humor expired or you typed it wrong.")
