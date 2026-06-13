def parse_sqft(val):
    val = str(val).strip()
    if '-' in val:
        parts = val.split('-')
        try:
            return (float(parts[0].strip())+float(parts[1].strip()))/2
        except ValueError:
            return np.nan 
    try:
        import re
        match = re.match(r'\d+\.?\d*',val)
        if match:
            return float(match.group()) 
        else:
            np.nan
    except Exception:
        return np.nan