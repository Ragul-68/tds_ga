import streamlit as st

def greatest_of_three(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("Greatest of Three Numbers App")

    # User input for three numbers
    num1 = st.number_input("Enter the first number:", value=0)
    num2 = st.number_input("Enter the second number:", value=0)
    num3 = st.number_input("Enter the third number:", value=0)

    # Button to calculate and display the result
    if st.button("Find Greatest"):
        result = greatest_of_three(num1, num2, num3)
        st.success(f"The greatest of the three numbers is: {result}")

if __name__ == "__main__":
    main()
