import streamlit as st
import pandas as pd
import joblib
import datetime

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(page_title="Loan Approval Portal", layout="centered", page_icon="🏦")

# -----------------------------
# Load the pre-trained model
# -----------------------------
model = joblib.load("model_baseline.pkl")  # Adjust path if needed

# -----------------------------
# Custom CSS Styling
# -----------------------------
st.markdown("""
    <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1728044849347-ea6ff59d98dd?q=80&w=2070&auto=format&fit=crop");
            background-attachment: fixed;
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }

        .block-container {
            background-color: rgba(255, 255, 255, 0.92);
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
        }

        header, footer, .stDeployButton {
            visibility: hidden;
        }
    </style>
""", unsafe_allow_html=True)


# -----------------------------
# Preprocessing Function
# -----------------------------
def preprocess_input(df):
    df = df.copy()
    df["home_ownership"] = df["home_ownership"].astype('category').cat.codes
    df["verification_status"] = df["verification_status"].astype('category').cat.codes
    df["purpose"] = df["purpose"].astype('category').cat.codes
    return df

# -----------------------------
# UI Header
# -----------------------------
st.markdown("<h1>Loan Approval Application</h1>", unsafe_allow_html=True)
st.markdown("Please fill in the applicant's loan details below for instant eligibility prediction.")
st.markdown("---")

# -----------------------------
# Input Form (Two Columns)
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    loan_amnt = st.number_input("Loan Amount ($)", min_value=1000.0, step=500.0)
    int_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=30.0, step=0.1)
    installment = st.number_input("Monthly Installment ($)", min_value=50.0, step=10.0)
    emp_length = st.slider("Employment Length (years)", 0, 40, 5)
    grade = st.selectbox("Loan Grade", options=list(range(7)), format_func=lambda x: chr(ord('A') + x))

with col2:
    annual_inc = st.number_input("Annual Income ($)", min_value=0.0, step=1000.0)
    dti = st.number_input("Debt-to-Income Ratio", min_value=0.0, step=0.1)
    home_ownership = st.selectbox("Home Ownership", ["RENT", "OWN", "MORTGAGE", "OTHER"])
    verification_status = st.selectbox("Verification Status", ["Verified", "Not Verified", "Source Verified"])
    purpose = st.selectbox("Loan Purpose", [
        "debt_consolidation", "credit_card", "home_improvement", "major_purchase",
        "small_business", "car", "other"
    ])

# -----------------------------
# Prediction Logic + Display
# -----------------------------
if st.button("Submit for Review"):
    input_dict = {
        "loan_amnt": [loan_amnt],
        "int_rate": [int_rate],
        "installment": [installment],
        "grade": [grade],
        "emp_length": [emp_length],
        "home_ownership": [home_ownership],
        "annual_inc": [annual_inc],
        "verification_status": [verification_status],
        "purpose": [purpose],
        "dti": [dti]
    }

    input_df = pd.DataFrame(input_dict)
    input_df = preprocess_input(input_df)

    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0][1]
    decision = "✅ Approved" if prediction == 1 else "❌ Rejected"

    # Display summary and result
    st.markdown("---")
    st.markdown("### Review Summary")
    summary_df = pd.DataFrame(input_dict).T.rename(columns={0: "Value"})
    summary_df["Value"] = summary_df["Value"].astype(str)
    st.dataframe(summary_df, use_container_width=True)

    st.markdown("### Decision")
    if prediction == 1:
        st.success(f"✅ The loan application is **approved**.\n\n**Approval Confidence:** {proba:.2%}")
    else:
        st.error(f"❌ The loan application is **rejected**.\n\n**Rejection Confidence:** {1 - proba:.2%}")

    # Save to log file
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_output = f"""
📲 LOAN PREDICTION – {timestamp}
----------------------------
Input Summary:
""" + "\n".join([f"  {key}: {value[0]}" for key, value in input_dict.items()]) + f"""

Prediction Result:
  Decision: {decision}
  Approval Probability: {proba:.2%}
----------------------------
"""

    with open("output.log", "a", encoding="utf-8") as f:
        f.write(log_output)