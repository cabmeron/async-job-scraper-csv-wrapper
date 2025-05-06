from dataclasses import dataclass

@dataclass
class Request:
    distance: int
    hours_old: int
    results_wanted: int
    location: str
    site_name: str
    search_term: str
    country_indeed:str
    google_search_term: str

@dataclass
class ReducedResponse:
    title: str
    job_url: str
    location: str
    date_posted: str
    num_employees: str
    job_url_direct: str
    company_url_direct: str
