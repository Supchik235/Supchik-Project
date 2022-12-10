#---------------------IMPORT PACKAGES------------------------------
import streamlit as st
from streamlit_option_menu import option_menu
import database as db

#----------------------DATABASE CONFIG-----------------------------
def get_all_periods():
    items = db.fetch_all_periods()
    periods = [item["key"] for item in items]
    return periods
#----------------------CONFIGURE SESSION STATES---------------------
if 'count' not in st.session_state:
	st.session_state.count = 0
#---------------------STREAMLIT PAGE CONFIG------------------------
st.set_page_config("Shopario", page_icon=":cloud:")

#---------------------REMOVE ST STYLING----------------------------
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

#---------------------CREATE NAV BAR--------------------------------
selected = option_menu(menu_title=None,options=["Create Order", "View Orders"],orientation="horizontal")
if selected == "Create Order":
#---------------------CREATE MAIN WINDOW---------------------------
    with st.form(key="order_creation", clear_on_submit=True):
        st.header("Create an order:")
        name = st.text_input("Name of Order maker:", key="name")
        lmb = ["Active"]
        status = st.selectbox("Status:",options=lmb, key="status")
        imp = ["Low", "Medium", "High"]
        level = st.selectbox("Importance:", options=imp, key="Impo")
        order = st.text_area("Your Order", key="order")
        "---"
        
            
        Button = st.form_submit_button("Create Order")
        
            
            
#---------------------AFTER BUTTON ACTIONS--------------------------
            
        if Button:
            if len(name) == 0:
                st.error("There Are Blank lines")
            else:
                period = str(st.session_state["name"]) + "_" + str(st.session_state["Impo"]) + "_" + str(st.session_state["order"] + "_" + str(st.session_state["status"]))
                db.insert_period(name,level,order,status)
                st.success("Order has been Created")
                
                
else:
    with st.form(key="form1"):

        period = st.selectbox("Select name:", get_all_periods())
        submit_button = st.form_submit_button("Search")
        if submit_button:
            period_data = db.get_period(period)
            name = period_data.get("name")
            level = period_data.get("Impo")
            order = period_data.get("order")
            status = period_data.get("status")
            
            st.write(f"Order from {period}:")
            st.write(order)
            st.write(f"Status:{status}")
            if level == "High":
                st.error("This Order is important")
    if st.button("Approve Order"):
        
        db.del_item(f"{period}")
        st.success("Succesfully approved order")
                
            
                

                
                
            
            
        
        
            
                
                
                

            
        
                
                    
                
                    
            
        

    
        
        


