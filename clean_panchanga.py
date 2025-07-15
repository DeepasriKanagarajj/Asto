import swisseph as swe
import datetime
import pytz

def get_panchanga(year, month, day, hour, minute, LAT=11.0168, LON=76.9558, TZ=5.5):
    # Timezone handling
    local = pytz.timezone('Asia/Kolkata')
    dt_local = local.localize(datetime.datetime(year, month, day, hour, minute))
    dt_utc = dt_local.astimezone(pytz.utc)
    jd = swe.julday(dt_utc.year, dt_utc.month, dt_utc.day, dt_utc.hour + dt_utc.minute / 60.0)

    moon_long = swe.calc_ut(jd, swe.MOON)[0][0]
    sun_long = swe.calc_ut(jd, swe.SUN)[0][0]

    def get_angle_diff(a, b):
        return (b - a) % 360

    tithi = int(get_angle_diff(sun_long, moon_long) / 12) + 1
    nakshatra = int(moon_long / (360 / 27)) + 1
    yoga = int((sun_long + moon_long) % 360 / (360 / 27)) + 1
    karana = int((get_angle_diff(sun_long, moon_long) % 60) / 6) + 1
    weekday = dt_local.strftime('%A')

    print(f"\nPANCHANGA for {dt_local.strftime('%Y-%m-%d %H:%M')}")
    print(f"Location: {LAT}°N, {LON}°E")
    print(f"Timezone: UTC+{TZ}\n")
    print(f"Tithi     : {tithi}")
    print(f"Nakshatra : {nakshatra}")
    print(f"Yoga      : {yoga}")
    print(f"Karana    : {karana}")
    print(f"Vaara     : {weekday}")
    return {
        "date": dt_local,
        "tithi": tithi,
        "nakshatra": nakshatra,
        "yoga": yoga,
        "karana": karana,
        "vaara": weekday
    }

# --- Ask User for Input ---
if __name__ == "__main__":
    date_input = input("Enter date (YYYY-MM-DD): ")
    time_input = input("Enter time (HH:MM, 24hr): ")

    year, month, day = map(int, date_input.split("-"))
    hour, minute = map(int, time_input.split(":"))

    get_panchanga(year, month, day, hour, minute)
