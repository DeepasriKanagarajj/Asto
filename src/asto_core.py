import swisseph as swe

def get_planet_positions(jd):
    planets = [swe.SUN, swe.MOON, swe.MERCURY, swe.VENUS, swe.MARS, swe.JUPITER, swe.SATURN]
    positions = {}
    for p in planets:
        pos = swe.calc_ut(jd, p)[0][0]
        positions[p] = pos
    return positions

def analyze_transit(birth_jd, target_jd):
    planet_names = {
        swe.SUN: "Sun",
        swe.MOON: "Moon",
        swe.MERCURY: "Mercury",
        swe.VENUS: "Venus",
        swe.MARS: "Mars",
        swe.JUPITER: "Jupiter",
        swe.SATURN: "Saturn"
    }
    
    natal_positions = get_planet_positions(birth_jd)
    transit_positions = get_planet_positions(target_jd)
    results = []
    for planet in natal_positions:
        diff = abs(natal_positions[planet] - transit_positions[planet])
        diff = min(diff, 360 - diff)  # Correct for circular angle difference
        if diff < 5:
            results.append(f"Transit {planet_names[planet]} conjunct natal {planet_names[planet]}: strong influence")
    return results


