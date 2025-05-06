import asyncio
from models import *
from constants import *
from pprint import pprint
from file_writing import *
from jobspy import scrape_jobs
from reducers import get_reduction

async def init(write_result):
    res = []
    q = asyncio.Queue()
    await asyncio.gather(producer(q, LOCATIONS, REQUEST_DETAILS), consumer(q, res))

    if write_result:
        write_to_csv(res)

    return True

async def consumer(queue, res_store):
    consumption_idx = 0
    while queue.qsize() > 0:
        item: Request = await queue.get()
        jobs = scrape_jobs(
            location=item.location,
            distance=item.distance,
            site_name=item.site_name,
            hours_old=item.hours_old,
            search_term=item.search_term,
            results_wanted=item.results_wanted,
            country_indeed=item.country_indeed,
            google_search_term=item.google_search_term
        )
        reduced_jobs = get_reduction(jobs)        
        res_store.append(reduced_jobs)
        consumption_idx += 1
        
    print(f'{consumption_idx} items consumed')

async def producer(queue: asyncio.Queue, locations: list, request_details: Request): 
    production_count = 0
    for location in locations:
        try:
            request = Request(
                location=location,
                distance=request_details["distance"],
                hours_old=request_details["hours_old"],
                site_name=request_details["site_name"],
                search_term=request_details["search_term"],
                results_wanted=request_details["results_wanted"],
                country_indeed=request_details["country_indeed"],
                google_search_term=request_details["google_search_term"],
            )
        except:
            raise ValueError

        await queue.put(request)
        production_count += 1
    
    print(f'{production_count} items produced')