
all_time_pattern = {
    "time_period": "(sáng|trưa|chiều|tối)",

    "number_previous_day": "(\\d\\d?) ngày trước",

    "previous_day": "(ngày hôm qua|hôm qua|hôm trước|hôm vừa rồi)",

    "today": "(nay|hôm nay)",

    "the_next_day": "(mai|ngày mai|ngày hôm sau|hôm sau|bữa sau|1 ngày nữa|một ngày nữa)",

    "double_next_day": "(ngày mốt|2 ngày nữa|hai ngày nữa)",

    "triple_next_day": "(ngày kia|3 ngày nữa|ba ngày nữa)",

    "number_next_day": "(\\d\\d?) ngày nữa|ngày tới|ngày sắp tới|ngày sau",

    "begin_of_previous_week": "đầu tuần trước|đầu tuần vừa rồi|đầu tuần rồi",
    "end_of_previous_week": "cuối tuần trước|cuối tuần vừa rồi|cuối tuần rồi",
    "all_previous_week": "tuần trước|tuần vừa rồi|tuần rồi",

    "begin_of_current_week": "đầu tuần này|đầu tuần hiện tại",
    "end_of_current_week": "cuối tuần này|cuối tuần hiện tại",
    "all_current_week": "tuần này|tuần hiện tại",

    "begin_of_next_week": "đầu tuần tới|đầu tuần sau|đầu tuần kế tiếp|đầu tuần tiếp theo",
    "end_of_next_week": "cuối tuần tới|cuối tuần sau|cuối tuần kế tiếp|cuối tuần tiếp theo",
    "all_next_week": "tuần sau|tuần tới|tuần kế tiếp|tuần tiếp theo|tuần tiếp theo",

    "begin_of_previous_month": "đầu tháng trước|đầu tháng vừa rồi|đầu tháng rồi",
    "end_of_previous_month": "cuối tháng trước|cuối tháng vừa rồi|cuối tháng rồi",
    "all_previous_month": "tháng trước|tháng vừa rồi|tháng rồi",

    "begin_of_current_month": "đầu tháng này|đầu tháng hiện tại",
    "end_of_current_month": "cuối tháng này|cuối tháng hiện tại",
    "all_curent_month": "tháng này|tháng hiện tại",

    "begin_of_next_month": "đầu tháng tới|đầu tháng sau|đầu tháng kế tiếp|đầu tháng tiếp theo",
    "end_of_next_month": "cuối tháng tới|cuối tháng sau|cuối tháng kế tiếp|cuối tháng tiếp theo",
    "all_next_month": "tháng sau|tháng tới|tháng kế tiếp|tháng tiếp theo",

    "begin_of_month_number_year": "đầu tháng[ ]*\\d\\d?[ ]*năm[ ]*\\d\\d\\d?\\d?|đầu tháng[ ]*\\d\\d?[ ]*[/-][ ]*\\d\\d\\d?\\d?|đầu \\d\\d?[ ]*[/-][ ]*\\d\\d\\d\\d",
    "end_of_month_number_year": "cuối tháng[ ]*\\d\\d?[ ]*năm[ ]*\\d\\d\\d?\\d?|cuối tháng[ ]*\\d\\d?[ ]*[/-][ ]*\\d\\d\\d?\\d?|cuối \\d\\d?[ ]*[/-][ ]*\\d\\d\\d\\d",

    "begin_of_month_number": "đầu tháng (\\d\\d?|một|giêng|hai|ba|tư|bốn|năm|sáu|bảy|tám|chín|mười|mười một|mười hai)",
    "end_of_month_number": "cuối tháng (\\d\\d?|một|giêng|hai|ba|tư|bốn|năm|sáu|bảy|tám|chín|mười|mười một|mười hai)",
    "all_number_month": "tháng (\\d\\d?|một|giêng|hai|ba|tư|bốn|năm|sáu|bảy|tám|chín|mười|mười một|mười hai)",

    "begin_of_previous_year": "đầu năm trước|đầu năm vừa rồi|đầu năm ngoái|đầu năm rồi",
    "end_of_previous_year": "cuối năm trước|cuối năm vừa rồi|cuối năm ngoái|cuối năm rồi",
    "all_previous_year": "năm trước|năm vừa rồi|năm ngoái|năm rồi",

    "begin_of_current_year": "đầu năm nay|đầu năm hiện tại",
    "end_of_current_year": "cuối năm nay|cuối năm hiện tại",
    "all_current_year": "năm nay|năm hiện tại",

    "begin_of_next_year": "đầu năm tới|đầu năm sau|đầu năm kế tiếp|đầu năm tiếp theo",
    "end_of_next_year": "cuối năm tới|cuối năm sau|cuối năm kế tiếp|cuối năm tiếp theo",
    "all_next_year": "năm tới|năm sau|năm kế tiếp|năm tiếp theo",

    "day_month_year": "(ngày[ ]*\\d\\d?[ ]*tháng[ ]*\\d\\d?[ ]*năm[ ]*\\d\\d\\d?\\d?|ngày[ ]*\\d\\d?[ ]*[/-][ ]*\\d\\d?[ ]*[/-][ ]*\\d\\d\\d?\\d?|\\d\\d?[ ]*[/-][ ]*\\d\\d?[ ]*[/-][ ]*\\d\\d\\d?\\d?)",

    "hour_minute_second": "(\\d\\d?[ ]*giờ[ ]*\\d\\d?[ ]*phút[ ]*\\d\\d?[ ]*giây|\\d\\d?[ ]*[hg:][ ]*\\d\\d?[ ]*[mp:][ ]*\\d\\d?[ ]*[s]?)",

    "hour_minute": "(\\d\\d?[ ]*giờ[ ]*\\d?\\d?[ ]*phút|\\d\\d?[ ]*giờ[ ]*\\d?\\d?[phút]?|\\d\\d?[ ]*[hg:][ ]*\\d?\\d?[ ]*[mp]?)",

    "month_year": "tháng[ ]*\\d\\d?[ ]*năm[ ]*\\d\\d\\d?\\d?|tháng[ ]*\\d\\d?[ ]*[/-][ ]*\\d\\d\\d?\\d?|\\d\\d?[ ]*[/-][ ]*\\d\\d\\d\\d",

    "day_month": "(ngày[ ]*\\d\\d?[ ]*tháng[ ]*\\d\\d?|ngày[ ]*\\d\\d?[ ]*[/-][ ]*\\d\\d?|\\d\\d?[ ]*[/-][ ]*\\d\\d?)",

    "day": "ngày[ ]*(\\d\\d?)",

    "month": "tháng[ ]*(\\d\\d?)",

    "year": "năm[ ]*(\\d\\d\\d?\\d?)",

    "hour": "(\\d\\d?[ ]*giờ|\\d\\d?[ ]*[hg])",
}

composed_pattern = {
    "time_period_number_previous_day": all_time_pattern["time_period"] + "[ ]*" + all_time_pattern["number_previous_day"],
    "time_period_previous_day": all_time_pattern["time_period"] + "[ ]*" + all_time_pattern["previous_day"],
    "time_period_the_next_day": all_time_pattern["time_period"] + "[ ]*" + all_time_pattern["the_next_day"],
    "time_period_today": all_time_pattern["time_period"] + "[ ]*" + all_time_pattern["today"],
    "time_period_double_next_day": all_time_pattern["time_period"] + "[ ]*" + all_time_pattern["double_next_day"],
    "time_period_triple_next_day": all_time_pattern["time_period"] + "[ ]*" + all_time_pattern["triple_next_day"],
    "time_period_number_next_day": all_time_pattern["time_period"] + "[ ]*" + all_time_pattern["number_next_day"],
    "time_period_day_month_year": all_time_pattern["time_period"] + "[ ]*" + all_time_pattern["day_month_year"],
    "time_period_day_month": all_time_pattern["time_period"] + "[ ]*" + all_time_pattern["day_month"],
    "time_period_day": all_time_pattern["time_period"] + "[ ]*" + all_time_pattern["day"],
    "hour_minute_day_month_year": all_time_pattern["hour_minute"] + "[ ]*" + all_time_pattern["day_month_year"],
    "hour_minute_day_month": all_time_pattern["hour_minute"] + "[ ]*" + all_time_pattern["day_month"],
    "hour_minute_day": all_time_pattern["hour_minute"] + "[ ]*" + all_time_pattern["day"],
    "day_month_year": all_time_pattern["day_month_year"],
    "begin_of_month_number_year": all_time_pattern["begin_of_month_number_year"],
    "end_of_month_number_year": all_time_pattern["end_of_month_number_year"],
    "month_year": all_time_pattern["month_year"],
    "day_month": all_time_pattern["day_month"],
    "hour_minute_second": all_time_pattern["hour_minute_second"],
    "hour_minute": all_time_pattern["hour_minute"],
    "number_previous_day": all_time_pattern["number_previous_day"],
    "previous_day": all_time_pattern["previous_day"],
    "the_next_day": all_time_pattern["the_next_day"],
    "double_next_day": all_time_pattern["double_next_day"],
    "triple_next_day": all_time_pattern["triple_next_day"],
    "number_next_day": all_time_pattern["number_next_day"],
    "begin_of_previous_week": all_time_pattern["begin_of_previous_week"],
    "end_of_previous_week": all_time_pattern["end_of_previous_week"],
    "all_previous_week": all_time_pattern["all_previous_week"],
    "begin_of_current_week": all_time_pattern["begin_of_current_week"],
    "end_of_current_week": all_time_pattern["end_of_current_week"],
    "all_current_week": all_time_pattern["all_current_week"],
    "begin_of_next_week": all_time_pattern["begin_of_next_week"],
    "end_of_next_week": all_time_pattern["end_of_next_week"],
    "all_next_week": all_time_pattern["all_next_week"],
    "begin_of_previous_month": all_time_pattern["begin_of_previous_month"],
    "end_of_previous_month": all_time_pattern["end_of_previous_month"],
    "all_previous_month": all_time_pattern["all_previous_month"],
    "begin_of_current_month": all_time_pattern["begin_of_current_month"],
    "end_of_current_month": all_time_pattern["end_of_current_month"],
    "all_curent_month": all_time_pattern["all_curent_month"],
    "begin_of_next_month": all_time_pattern["begin_of_next_month"],
    "end_of_next_month": all_time_pattern["end_of_next_month"],
    "all_next_month": all_time_pattern["all_next_month"],
    "begin_of_month_number": all_time_pattern["begin_of_month_number"],
    "end_of_month_number": all_time_pattern["end_of_month_number"],
    "all_number_month": all_time_pattern["all_number_month"],
    "begin_of_previous_year": all_time_pattern["begin_of_previous_year"],
    "end_of_previous_year": all_time_pattern["end_of_previous_year"],
    "all_previous_year": all_time_pattern["all_previous_year"],
    "begin_of_current_year": all_time_pattern["begin_of_current_year"],
    "end_of_current_year": all_time_pattern["end_of_current_year"],
    "all_current_year": all_time_pattern["all_current_year"],
    "begin_of_next_year": all_time_pattern["begin_of_next_year"],
    "end_of_next_year": all_time_pattern["end_of_next_year"],
    "all_next_year": all_time_pattern["all_next_year"],
    "day": all_time_pattern["day"],
    "month": all_time_pattern["month"],
    "year": all_time_pattern["year"],
    "today": all_time_pattern["today"],
    "hour_minute_today": all_time_pattern["hour"],
}