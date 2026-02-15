def traffic_light(num_breaches: int, n_obs: int):
    """
    Basel-inspired: Green<=2%, Yellow<=5%, Red>5%.
    """
    breach_ratio = num_breaches / n_obs
    if breach_ratio <= 0.02:
        return "Green"
    elif breach_ratio <= 0.05:
        return "Yellow"
    else:
        return "Red"
