import requests
from datetime import datetime
import smtplib
import time


MY_LAT = "52.376060"
MY_LANG = "5.784190"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and  MY_LANG-5 <= iss_latitude <= MY_LANG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "long": MY_LANG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()
    sun_rise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sun_set = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sun_set or time_now <= sun_rise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        my_email = "inbox.a.ahmad@gmail.com"
        rec_emil = "anees.ahmad1107@gmail.com"
        password = "iizleposhoyhuwar"
        message = f"Subject:Look Up\n\nThe Iss is above you in the sky."
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=rec_emil,
                msg=message.encode("utf-8")
            )