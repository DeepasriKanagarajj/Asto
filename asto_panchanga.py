from jhora.ui.panchangam import Panchanga
from datetime import datetime
import pytz

def get_today_panchanga(lat, lon, timezone_str):
    tz = pytz.timezone(timezone_str)
    now = datetime.now(tz)

    p = Panchanga()
    p.compute_panchangam(
        year=now.year,
        month=now.month,
        day=now.day,
        hour=now.hour,
        minute=now.minute,
        timezone=timezone_str,
        lat=lat,
        lon=lon
    )

    return {
        "date": now.strftime('%Y-%m-%d %H:%M'),
        "tithi": p.tithi,
        "nakshatra": p.nakshatra,
        "yoga": p.yoga,
        "vaara": p.vaara
    }

if __name__ == "__main__":
    result = get_today_panchanga(lat=11.0168, lon=76.9558, timezone_str="Asia/Kolkata")
    print("🌟 ASTO Panchanga for Today 🌟")
    for key, value in result.items():
        print(f"{key.title()} : {value}")
