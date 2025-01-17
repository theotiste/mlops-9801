from app import model_pred

new_data = {'Customer_id': 8153374,
            'Credit_line_outstanding': 0,
            'Loan_amt_outstanding': 5221.545193,
            'Total_debt_outstanding': 3915.471226,
            'Income': 78039.38546,
            'Years_employed': 5,
            'Fico_score': 605
            }


def test_predict():
    prediction = model_pred(new_data)
    assert prediction == 1, "incorrect prediction" 

