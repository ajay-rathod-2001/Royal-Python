import pickle 
import os
from datetime import datetime
import pandas as pd
import numpy as np

class Inference:
    def __init__(self, model_path, sc_path):
        self.model = model_path
        self.sc = sc_path
        
        if os.path.exists(self.model) and os.path.exists(self.sc):
            self.model = pickle.load(open(self.model, "rb"))
            self.sc = pickle.load(open(self.sc, "rb"))
        else:
            print("Model OR Standard Scaler Path is not Founded OR Correct : ")
            
    def get_string_to_datetime(self, date):
        dt = datetime.strptime(date, "%d/%m/%Y")
        return {"day": dt.day, "month": dt.month, "year": dt.year, "week_day": dt.strftime("%A")}
     
    def season_to_df(self, seasons):
        seasons_cols = ['Spring', 'Summer', 'Winter']
        seasons_data =np.zeros((1, len(seasons_cols)), dtype="int")

        df_seasons =pd.DataFrame(seasons_data, columns=seasons_cols)
        if seasons in seasons_cols:
            df_seasons[seasons]=1
        return df_seasons
    
    def days_df(self,week_day):
        day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',  'Saturday', 'Sunday']
        day_names_data = np.zeros((1, len(day_names)), dtype="int")

        df_days = pd.DataFrame(day_names_data, columns=day_names)
        if week_day in day_names:
            df_days[week_day] = 1
        return df_days
     
        
    def users_input(self):
        print("Enter The Correct Information to Predict Rented Bike For a Day with Respect to Time : ")
        
        date =input(" Date (dd/mm/yyyy): ")
        hour = int(input("Hours(0-23): "))
        temperature =float(input("Temperature (in C): "))
        humidity = float(input("Humidity: "))
        wind_speed = float(input("Wind Speed: "))
        visibility = float(input("Visibility: "))
        solar_radiation = float(input("Solar Radition: "))
        rainfall = float(input("Ranifall: "))
        snowfall =float(input("Snowfall: "))
        seasons = input("Seasons (Antum, Summer, Winter, Spring): ")
        holiday = input("Holiday (Holiday/  NO Holiday): ")
        functional_day =input("Function Day(Yes/NO): ")

        holiday_dic = {"Holiday":0, "No Holiday":1}
        functioning_day = {"No":0, "Yes":1}

        str_to_date = self.get_string_to_datetime(date)
        
        u_input_list = [
            hour,
            temperature,
            humidity,
            wind_speed,
            visibility,
            solar_radiation,
            rainfall,
            snowfall,
            holiday_dic[holiday],
            functioning_day[functional_day],
            str_to_date["day"],
            str_to_date["month"],
            str_to_date["year"],
]

        features_name = ['Hour', 'Temperature(°C)', 'Humidity(%)',
            'Wind speed (m/s)', 'Visibility (10m)', 'Solar Radiation (MJ/m2)',
            'Rainfall(mm)', 'Snowfall (cm)', 'Holiday', 'Functioning Day', 'Day',
            'Month', 'Year']
        
        expected_columns = ['Hour', 'Temperature(°C)', 'Humidity(%)',
       'Wind speed (m/s)', 'Visibility (10m)', 'Solar Radiation (MJ/m2)',
       'Rainfall(mm)', 'Snowfall (cm)', 'Holiday', 'Functioning Day', 'Day',
       'Month', 'Year', 'Spring', 'Summer', 'Winter', 'Monday', 'Saturday',
       'Sunday', 'Thursday', 'Tuesday', 'Wednesday']
        
        df_u_input =pd.DataFrame([u_input_list], columns=features_name)
        df_seasons =self.season_to_df(seasons)
        df_days=self.days_df(str_to_date["week_day"])
        df_for_pred =pd.concat([df_u_input, df_seasons, df_days], axis=1)
        df_for_pred = df_for_pred[expected_columns]
        
        return df_for_pred
    
    def prediction(self):
        df = self.users_input()
        scaled_data = self.sc.transform(df)
        prediction = self.model.predict(scaled_data)
        return prediction
    
if __name__ =="__main__":
    ml_model_path = r"C:\Users\ajayr\OneDrive\Docs\GitHub\Royal-Python\Bike Sharing Demand Prediction Project\Models\xgboost_regressor_r2_0_947_v1.pkl"
    standard_scaler_path = r"C:\Users\ajayr\OneDrive\Docs\GitHub\Royal-Python\Bike Sharing Demand Prediction Project\Models\scaler.pkl"
    inference = Inference(ml_model_path,standard_scaler_path)
    
    pred = inference.prediction()
    
    print(f"Rented Bike Count Prediction  with Respect to Date and Time : {round(pred.tolist()[0])}")