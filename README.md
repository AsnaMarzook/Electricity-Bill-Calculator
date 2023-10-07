# Electricity-Bill-Calculator
This is a simple Python code to calculate electricity bill using Streamlit.

## How to use:
Clone this repository to your local machine.
Install the required dependencies:
```
pip install streamlit
```

Run the following command to start the Streamlit app:
```
streamlit run app.py
```

Enter the number of units consumed and any outstanding value.
Click the "Calculate" button.
The total bill amount will be displayed below.

**Example:**

Number of units: 100

Outstanding value: 500

Total bill amount: 1500

### Notes:

The electricity bill calculation is based on the following rates:

- 0-30 units: ₹400 per unit
- 31-60 units: ₹550 per unit
- 61-90 units: ₹650 per unit
- 91-120 units: ₹1500 per unit
- 121-180 units: ₹1500 per unit
- 181+ units: ₹2000 per unit

  
The outstanding value is added to the total bill amount.

## Contribution:

This code is open source and contributions are welcome. Please feel free to create pull requests with any improvements or suggestions.
