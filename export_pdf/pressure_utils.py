def convert_pressure_from_kPa(values, pressure_type):
    if pressure_type == 'kPa':
        return values
    elif pressure_type == 'mbar':
        return [v * 10 if v is not None else None for v in values]
    elif pressure_type == 'mH2O':
        return [float(v) * 0.10197 if v is not None else None for v in values]
    return values

def pressure_label(pressure_type):
    labels = {
        "kPa":"Давление (kPa)",
        "mbar":"Давление (mbar)",
        "mH2O":"Давление (mH2O)"
    }
    return labels.get(pressure_type, "Давление")

def convert_pressure_from_mbar(values, pressure_type):
    if pressure_type == 'kPa':
        return [v / 10 if v is not None else None for v in values]
    elif pressure_type == 'mbar':
        return values
    elif pressure_type == 'mH2O':
        return [float(v) * 0.010197 if v is not None else None for v in values]
    return values