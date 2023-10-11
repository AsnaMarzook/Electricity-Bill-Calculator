import streamlit
streamlit.title("Electricity Bill Calculator")

no_units = (streamlit.text_input("Number of Units"))
outstanding = (streamlit.text_input("Outstanding Value"))

def total_value(value,outstanding):
  outstanding = int (outstanding)
  return value+outstanding

def calculator(no_units):
  no_units = int(no_units)
  if no_units<60: 
    if no_units>0 and no_units<=30:
      return no_units*10,150
    elif no_units>30 and no_units<=60:
      return no_units*25,300
  else:
    if no_units>60 and no_units<=90:
      return no_units*35,400
    elif no_units>90 and no_units<=120:
      return no_units*50,1000
    elif no_units>120 and no_units<=180:
      return no_units*50,1500
    elif no_units>180:
      return no_units*75,2000

energy_charge,fixed_charge=calculator(no_units)

total_outstanding=total_value(energy_charge+fixed_charge,outstanding)

if streamlit.button("Calculate"):
    streamlit.write(f"Energy Charge : {energy_charge}")
    streamlit.write(f"Fixed Charge : {fixed_charge}")
    streamlit.write(f"Total Charge : {total_outstanding}")

else:
    pass
