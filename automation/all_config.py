#結果日
def result_year():
    return 2021
def result_month():
    return 4
def result_day():
    return 16

#サブサイン結果
def sub_sign(time):
    if time == "日中":
        return "-20"
    if time == "前場":
        return "-60"
    if time == "後場":
        return "±0"

#サブサイン累計
def sub_total(time):
    if time == "日中":
        return "-815"
    if time == "前場":
        return "-630"
    if time == "後場":
        return "-140"

#メインサイン
def main_sign(time):
    if time == "日中":
        return "-20"
    if time == "前場":
        return "-60"
    if time == "後場":
        return "±0"

#メイン累計
def main_total(time):
    if time == "日中":
        return "+285"
    if time == "前場":
        return "+130"
    if time == "後場":
        return "-140"


#投稿日
def reserve_year():
    return 2021
def reserve_month():
    return 4
def reserve_day():
    return 19
