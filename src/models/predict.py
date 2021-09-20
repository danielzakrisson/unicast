from src.models.expected_timefraction_predictions import expected_timefraction


def model_predict(inp, model_data=[]):

    lower_bound = inp.lower_bound
    upper_bound = inp.upper_bound
    time_horizon = inp.time_horizon

    timefrac = expected_timefraction(lower_bound, upper_bound, time_horizon)
    return {'Expected_timefraction': timefrac}