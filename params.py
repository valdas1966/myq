from f_utils import u_file
from f_utils import u_pickle


# Path to Pickle-File with Myq-Parameters
pickle_params = __file__[0] + ':\\myq\\params.pickle'


def set(param, value):
    """
    ============================================================================
     Description: Set Param Value.
    ============================================================================
     Arguments:
    ----------------------------------------------------------------------------
        1. param : str (Param Name)
        2. value : obj
    ============================================================================
    """
    params = dict()
    if u_file.is_exists(pickle_params):
        params = u_pickle.load(pickle_params)
    params[param] = value
    u_pickle.dump(obj=params, path=pickle_params)


def get(param):
    """
    ============================================================================
     Description: Return Param-Value.
    ============================================================================
     Arguments:
    ----------------------------------------------------------------------------
        1. param : str (Param Name)
    ============================================================================
     Return: obj (Param Value)
    ============================================================================
    """
    params = u_pickle.load(pickle_params)
    return params[param]
