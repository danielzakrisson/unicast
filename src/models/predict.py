from models.src.models.expected_timefraction_predictions import expected_timefraction, best_range


def model_predict(inp, model_data=[]):
    
    
    #metadata = {}
    #if hasattr(inp, "historic_point"):
    #    historic_point = inp.historic_point
    #    if historic_point:
    #        historic_point = datetime.datetime.strptime(historic_point, "%m/%d/%Y, %H:%M:%S")
    #        metadata['historic point'] = historic_point

    if inp.prediction_type == 'Expected_timefraction':
        
        lower_bound = inp.lower_bound
        upper_bound = inp.upper_bound
        time_horizon = inp.time_horizon
        #res = 17
        res = expected_timefraction(lower_bound, upper_bound, time_horizon)
        name = "Expected_timefraction"
    else:
        
        timefraction = inp.time_fraction
        time_horizon = inp.time_horizon
        res = best_range(timefraction, time_horizon)
        name = "Best range"
        
    return {name: res}
