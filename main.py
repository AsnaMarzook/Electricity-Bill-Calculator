import streamlit
streamlit.title("Electricity Bill Calculator")

no_units = (streamlit.text_input("Number of Units"))
outstanding = (streamlit.text_input("Outstanding Value"))

def total_value(value,outstanding):
  outstanding = int (outstanding)
  return value+outstanding

def calculator(no_units):
  no_units = int(no_units)
  if no_units>0 and no_units<=30:
    return no_units*400
  elif no_units>30 and no_units<=60:
    return no_units*550
  elif no_units>60 and no_units<=90:
    return no_units*650
  elif no_units>90 and no_units<=120:
    return no_units*1500
  elif no_units>120 and no_units<=180:
    return no_units*1500
  elif no_units>180:
    return no_units*200

if streamlit.button("Calculate"):
    streamlit.write(total_value(calculator(no_units),int(outstanding)))
else:
    pass
