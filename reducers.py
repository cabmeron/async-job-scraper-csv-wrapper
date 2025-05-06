import pandas as pd
from models import *
from pprint import pprint

# REDUCER LOGIC
def reduction_generator(data, reduction_type):
    """
        Business Logic for Data Reduction Object Generation
            Returns data-reduced object from provided context
            mapped callback (dataclass)
    """
    match reduction_type:
        case 0:
            res = []
            for i, df in data.iterrows():
                res.append(
                    ReducedResponse(
                        title=df["title"],
                        job_url=df["job_url"],
                        location=df["location"],
                        date_posted=df["date_posted"],
                        num_employees=df["company_num_employees"],
                        job_url_direct=df["job_url_direct"],
                        company_url_direct=df["company_url_direct"],
                    )
                )
            return res
        
# REDUCER APIS
def get_reduction(data, reduction_callback=0):
    """
        APIS for returning a specificied data reduction
    """
    match reduction_callback:
        case 0:
            return reduction_generator(data, reduction_callback)
    