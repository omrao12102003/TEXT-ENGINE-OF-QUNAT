def validate_intent(intent_dict: dict) -> list:
    
    errors = []
    
    # Weights sum check
    if abs(sum(intent_dict.get('weights', [0])) - 1.0) > 0.01:
        errors.append("Weights must sum to 100%")
    
    # Years check
    if intent_dict.get('start_year', 0) >= intent_dict.get('end_year', 9999):
        errors.append("Start year must be before end year")
    
    return errors
