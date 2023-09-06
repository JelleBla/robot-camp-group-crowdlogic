from datetime import datetime
def solution_station_2(date_string):
    date_obj = datetime.strptime(date_string, "%Y-%m-%d")
    day_of_week = date_obj.weekday()
    week_days = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]
    return week_days[day_of_week]