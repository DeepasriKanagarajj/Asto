import swisseph as swe
import datetime
import pytz

# Location info
LAT = 11.0168   # Coimbatore
LON = 76.9558
TZ = 5.5  # India Standard Time

# Date for Panchanga
year, month, day = 2025, 7, 15
hour = 6  # 6 AM local time (you can change this)

# Convert to UTC
local = pytz.timezone('Asia/Kolkata')
dt_local = local.localize(datetime.datetime(year, month, day, hour))
dt_utc = dt_local.astimezone(pytz.utc)

# Convert to Julian Day
jd = swe.julday(dt_utc.year, dt_utc.month, dt_utc.day, dt_utc.hour + dt_utc.minute / 60.0)

# Set ephemeris path (optional)
swe.set_ephe_path('/usr/share/ephe')  # You can skip this unless using offline data

# Helper function
def get_angle_diff(a, b):
    diff = b - a
    return diff % 360

# Moon & Sun longitudes
moon_long = swe.calc_ut(jd, swe.MOON)[0][0]
sun_long = swe.calc_ut(jd, swe.SUN)[0][0]

# --- Tithi ---
tithi = int(get_angle_diff(sun_long, moon_long) / 12) + 1

# --- Nakshatra ---
nakshatra = int(moon_long / (360 / 27)) + 1

# --- Yoga ---
yoga = int((sun_long + moon_long) % 360 / (360 / 27)) + 1

# --- Karana ---
tithi_angle = get_angle_diff(sun_long, moon_long)
karana = int((tithi_angle % 60) / 6) + 1

# --- Vaara ---
weekday = dt_local.strftime('%A')

# Output
print(f"\nPANCHANGA for {dt_local.strftime('%Y-%m-%d %H:%M')}")
print(f"Location: {LAT}°N, {LON}°E")
print(f"Timezone: UTC+{TZ}\n")

print(f"Tithi     : {tithi}")
print(f"Nakshatra : {nakshatra}")
print(f"Yoga      : {yoga}")
print(f"Karana    : {karana}")
print(f"Vaara     : {weekday}")

