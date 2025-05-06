import asyncio
from models import *
from constants import *
from file_writing import *
from scraping import *

async def main():
    await init(write_result=True)

if __name__ == "__main__":
    asyncio.run(main())