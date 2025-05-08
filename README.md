# jobsync-async-batching

## [AsyncIO](https://docs.python.org/3/library/asyncio.html) Queueing for Multi-Location [JobSpy](https://github.com/speedyapply/JobSpy) requests

### How to run:
1) `git clone https://github.com/cabmeron/jobspy-async-batching.git`
2) `pip install -r requirements.txt`
3) `python main.py`

#### Files
* constants.py: Job Locations and Job Request Params
* scraping.py: Queue Production & Consumption
* models.py: ...
* file_writing.py: ...
* main.py: ...

```bash
├── outputs
│   └── 2025-05-05
│       ├── Los Angeles, CA
│       │   └── 1746503188.276072.csv
│       ├── New York, NY
│       │   └── 1746503188.27917.csv
│       ├── San Francisco, CA
│       │   └── 1746503297.673176.csv
│       └── Seattle, WA
│           └── 1746503188.273997.csv

```

| title | job_url   | location    | date posted    | num_employees | job_url_direct |
|:------|:---------|:-----------:|-----------------|:-------------:|---------------:|
| ReactJS Developer - Candidates from Bay Area (SFO)  |https://www.indeed.com/viewjob?jk=27cc96e7a2285efa| San Jose, CA, US      |  2025-05-03               |    11-50           | http://www.indeed.com/job/reactjs-developer-candidates-bay-area-sfo-27cc96e7a2285efa    |
| Lead SW Engineer    |  https://www.indeed.com/viewjob?jk=3249c35c05b8106  |   Foster City, CA, US       |   2025-05-02   |  10,000+   |   https://jobs.smartrecruiters.com/Visa/744000057343243-lead-sw-engineer        |
...
