# Filename: dads_budget_tracker.py
import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Papa's Budget Tracker 💰", layout="centered")

st.title("💰 Papa's Personal Budget Tracker")
st.write("Track your income and expenses easily. Keep your finances organized!")

# File to store data
data_file = "budget_data.csv"

# Load existing data
if os.path.exists(data_file):
    df = pd.read_csv(data_file)
else:
    df = pd.DataFrame(columns=["Date", "Category", "Type", "Amount", "Notes"])

# Input form for new transaction
st.subheader("Add Income / Expense")
with st.form("entry_form"):
    date = st.date_input("Date")
    category = st.text_input("Category (e.g., Food, Bills, Travel)")
    type_ = st.selectbox("Type", ["Income", "Expense"])
    amount = st.number_input("Amount", min_value=0.0, step=0.01)
    notes = st.text_area("Notes (optional)")
    submitted = st.form_submit_button("Add Entry")
    
    if submitted:
        new_entry = {"Date": date, "Category": category, "Type": type_, "Amount": amount, "Notes": notes}
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_csv(data_file, index=False)
        st.success(f"✅ {type_} entry added successfully!")

# Display all transactions
st.subheader("All Transactions")
st.dataframe(df)

# Summary metrics
st.subheader("Summary")
total_income = df[df["Type"]=="Income"]["Amount"].sum()
total_expense = df[df["Type"]=="Expense"]["Amount"].sum()
balance = total_income - total_expense
st.metric("Total Income", f"${total_income:.2f}")
st.metric("Total Expense", f"${total_expense:.2f}")
st.metric("Balance", f"${balance:.2f}")

# Pie chart of expenses by category
expense_df = df[df["Type"]=="Expense"]
if not expense_df.empty:
    expense_by_category = expense_df.groupby("Category")["Amount"].sum()
    fig, ax = plt.subplots()
    ax.pie(expense_by_category, labels=expense_by_category.index, autopct="%1.1f%%", startangle=140)
    ax.set_title("Expenses by Category")
    st.pyplot(fig)

# Download CSV option
st.subheader("Download Your Transactions")
if not df.empty:
    csv = df.to_csv(index=False)
    st.download_button(label="📥 Download CSV", data=csv, file_name="dad_budget_data.csv", mime="text/csv")

# Personalized message
st.write("---")
st.success("This budget tracker is made with ❤️ just for you, Dad! Keep smiling and stay financially smart! 😊")
