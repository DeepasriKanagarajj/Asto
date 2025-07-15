from asto_patterns import analyze_patterns
from asto_core import analyze_transit
import swisseph as swe

birth_jd = swe.julday(1996, 10, 23, 12 + 45/60)

def run_timeline_analysis(start_year=2010, end_year=2026):
    print("\n🔍 Asto is analyzing transits on your birthday from", start_year, "to", end_year)
    for year in range(start_year, end_year + 1):
        target_jd = swe.julday(year, 10, 23, 12)  # Your birthday at noon
        results = analyze_transit(birth_jd, target_jd)
        print(f"\n📅 {year}-10-23:")
        if results:
            for res in results:
                print("Asto:", res)
        else:
            print("Asto: No major transits on this birthday.")
run_timeline_analysis(2010, 2026)

while True:
    user_input = input("Enter date to analyze (YYYY-MM-DD) or 'exit': ")
    if user_input.lower() == 'exit':
        break
    try:
        year, month, day = map(int, user_input.split('-'))
        target_jd = swe.julday(year, month, day, 12)  # Noon for calculation
        
        # Analyze transits
        results = analyze_transit(birth_jd, target_jd)
        if results:
            for res in results:
                print("Asto:", res)
        else:
            print("Asto: No significant transits on this day.")
        
        # Analyze astrological patterns like Saturn return, Sade Sati
        patterns = analyze_patterns(birth_jd, target_jd)
        if patterns:
            for pattern in patterns:
                print("Asto (Pattern):", pattern)
        else:
            print("Asto: No notable astrological patterns on this day.")
        
    except Exception as e:
        print("Invalid input. Please enter date as YYYY-MM-DD.")

