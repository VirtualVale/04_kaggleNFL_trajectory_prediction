from typing import Union, Tuple
import pandas as pd
import numpy as np

def deg2arrowPosition(angles: Union[float, np.ndarray, pd.Series]) -> Tuple[np.ndarray, np.ndarray]:
    """
    Convert angle(s) in degrees to arrow components (dx, dy).
    Accepts scalar, numpy array or pandas Series. Returns two numpy arrays.
    """
    
    theta = np.deg2rad(angles)
    dx = np.sin(theta)
    dy = np.cos(theta)

    return np.asarray(dx), np.asarray(dy)