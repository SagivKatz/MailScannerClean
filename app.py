import streamlit as st

def render_policy():
    st.title("Welcome to my accounts!")
    st.subheader("Privacy Policy")
    st.write("This application does not store or share your data. We only temporarily scan your email subjects to identify your linked accounts.")
    if st.button("I consent, continue"):
        st.session_state["stage"] = "input"

def render_email_input():
    st.title("Welcome to my accounts!")
    email = st.text_input("Enter your email address (for display only):")
    if st.button("Scan for accounts"):
        st.session_state["email"] = email
        st.session_state["stage"] = "results"

def render_results():
    st.title("Welcome to my accounts!")
    st.write(f"Presenting registered accounts for: `{st.session_state.get('email', '')}`")

    # Mock data (פייק מידע לצורך הדגמה)
    mock_accounts = [
        ("Netflix", "https://www.netflix.com/account"),
        ("Spotify", "https://www.spotify.com/account"),
        ("Amazon", "https://www.amazon.com/gp/css/homepage.html")
    ]

    if mock_accounts:
        for service, url in mock_accounts:
            st.markdown(f"✅ **{service}** — [Manage/Delete Account]({url})")
    else:
        st.info("No matched services found based on email subjects.")

def main():
    if "stage" not in st.session_state:
        st.session_state["stage"] = "policy"

    if st.session_state["stage"] == "policy":
        render_policy()
    elif st.session_state["stage"] == "input":
        render_email_input()
    elif st.session_state["stage"] == "results":
        render_results()

if __name__ == "__main__":
    main()