


# temporaty drop id column and create new Df after modelling phase
"""

By this point as our test DataFrame contains IdColumn, we remove it because the trained model doesn’t use
IdColumn as it’s not useful.
Create Ready File to Submit on Kaggle

temp_drop_list = ['IdColumn']
predictions = model.predict(test.drop(temp_drop_list,axis=1))

//after modelling

final_df = DataFrame({
        "IdColumn" : test["IdColumn"]
        "predicted_op": predictions
})



"""
