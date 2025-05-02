import streamlit as st

with open("custom.css", "r") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)


def show_instrument_config(user_name, instrument_name, instrument_short):
    st.header(instrument_name + " Parameters")
    enable_trades = st.checkbox(instrument_short + " Enable Trades", value=False)

    atr_period = st.number_input(
        instrument_short + " ATR Period", value=10, min_value=0, max_value=100
    )
    multiplier = st.number_input(
        instrument_short + " Multiplier", value=2.00, min_value=0.00, max_value=10.00
    )
    timeframe = st.number_input(
        instrument_short + " Timeframe", value=5, min_value=0, max_value=100
    )
    quantity = st.number_input(
        instrument_short + " Quantity", value=750, min_value=0, max_value=1000
    )

    btn_save = st.button("Save")

    if btn_save:
        file_path = user_name + "_settings.txt"
        # Open the file in write mode
        with open(file_path, "w") as file:
            file.writelines("instrument_name:" + instrument_name)
            file.writelines("\nenable_trades:" + str(enable_trades))
            file.writelines("\natr_period:" + str(atr_period))
            file.writelines("\nmultiplier:" + str(multiplier))
            file.writelines("\ntimeframe:" + str(timeframe))
            file.writelines("\nquantity:" + str(quantity))

        # if nf_enable_trades:
        #     st.write("Checkbox is checked!")


show_instrument_config("karthik", "Nifty", "NF")
