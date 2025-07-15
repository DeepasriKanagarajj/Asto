import swisseph as swe

SATURN_RETURN_DEGREE = 30  # Roughly every 29.5 years
SADE_SATI_START = -45      # Moon 45 degrees before Saturn
SADE_SATI_END = 15         # Moon 15 degrees after Saturn

def get_saturn_return(birth_jd, target_jd):
    saturn_birth = swe.calc_ut(birth_jd, swe.SATURN)[0]
    saturn_target = swe.calc_ut(target_jd, swe.SATURN)[0]

    if abs(saturn_target - saturn_birth) < 5:
        return "🪐 Saturn Return is active — major life restructuring phase."
    return None

def get_sade_sati(moon_birth_deg, saturn_target_deg):
    delta = (saturn_target_deg - moon_birth_deg + 360) % 360
    if SADE_SATI_START % 360 <= delta <= SADE_SATI_END % 360:
        return "🌑 Sade Sati phase — emotional and karmic challenges."
    return None

def analyze_patterns(birth_jd, target_jd):
    results = []

    # Saturn Return
    sr = get_saturn_return(birth_jd, target_jd)
    if sr:
        results.append(sr)

    # Sade Sati
    moon_birth_deg = swe.calc_ut(birth_jd, swe.MOON)[0]
    saturn_target_deg = swe.calc_ut(target_jd, swe.SATURN)[0]
    ss = get_sade_sati(moon_birth_deg, saturn_target_deg)
    if ss:
        results.append(ss)

    return results
