from dict_2 import est_eng_dict, est_it_dict

def swap_dict_key_value(original_dict: dict[str, str] -> dict[str, str]):
    result_dict = {}
    for key, value in original_dict.items():
        result_dict[value] = key
    return result_dict
