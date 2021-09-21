from src.models.expected_timefraction_predictions import expected_timefraction, best_range


def model_predict(inp, model_data=[]):

    if inp.prediction_type == 'Expected_timefraction':
        lower_bound = inp.lower_bound
        upper_bound = inp.upper_bound
        time_horizon = inp.time_horizon
        res = expected_timefraction(lower_bound, upper_bound, time_horizon)
        name = "Expected_timefraction"
    else:
        timefraction = inp.timefraction
        time_horizon = inp.time_horizon

        res = best_range(timefraction, time_horizon)
        name = 'Best range'
    return {name: res, }
