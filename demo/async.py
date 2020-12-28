from asyncio import Task, get_event_loop
from typing import List, Tuple

import aiohttp
import datetime
import bs4
from colorama import Fore

from demo.support import URL, colored_print

loop = get_event_loop()


async def get_html(number: int) -> str:
    colored_print(color=Fore.YELLOW, string=f'Getting HTML #{number} iteration')
    async with aiohttp.ClientSession() as client:
        response = await client.get(URL)
        response.raise_for_status()
        return await response.text()


async def get_title(html: str, number: int) -> str:
    colored_print(color=Fore.CYAN, string=f'Getting TITLE #{number} iteration')
    soup = bs4.BeautifulSoup(html, 'html.parser')
    header = soup.select_one('h1')
    if not header:
        return 'MISSING'
    return header.text.strip()


async def get_title_range() -> None:
    tasks: List[Tuple[int, Task]] = []
    for iteration in range(10):  # type: int
        tasks.append((iteration, loop.create_task(get_html(iteration))))
    for number, task in tasks:  # type: int, Task
        html: str = await task
        title: str = await get_title(html, number)
        colored_print(color=Fore.WHITE, string=f'Title found: {title}')


def main() -> None:
    start_time = datetime.datetime.now()
    loop.run_until_complete(get_title_range())
    end_time = datetime.datetime.now() - start_time
    print(f'Done in {end_time.total_seconds():.2f} sec.')


if __name__ == '__main__':
    main()
