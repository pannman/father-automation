#サブサイン
def sub_sign(time):
    if time == "日中":
        return "+121"
    if time == "後場":
        return "+233"
    if time == "前場":
        return "-333"

#メインサイン
def main_sign(time):
    if time == "日中":
        return "+321"
    if time == "後場":
        return "+243"
    if time == "前場":
        return "-53"