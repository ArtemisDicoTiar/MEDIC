import math


def get_SMAPE(args):
    real_val, pred_val = args

    if not math.isnan(pred_val):
        diff_df = abs(real_val - pred_val)
        sum_abs_df = abs(real_val) + abs(pred_val)

        return round(100 - (diff_df / sum_abs_df) * 100, 2)

    return None
