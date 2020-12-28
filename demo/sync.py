import datetime
import requests
import bs4
from colorama import Fore

from demo.support import URL, colored_print


def get_html(number: int) -> str:
    colored_print(color=Fore.YELLOW, string=f'Getting HTML #{number} iteration')
    response = requests.get(URL)
    response.raise_for_status()
    return response.text


def get_title(html: str, number: int) -> str:
    colored_print(color=Fore.CYAN, string=f'Getting TITLE #{number} iteration')
    soup = bs4.BeautifulSoup(html, 'html.parser')
    header = soup.select_one('h1')
    if not header:
        return 'MISSING'
    return header.text.strip()


def get_title_range() -> None:
    for iteration in range(10):  # type: int
        html: str = get_html(iteration)
        title: str = get_title(html, iteration)
        colored_print(color=Fore.WHITE, string=f'Title found: {title}')


def main() -> None:
    start_time = datetime.datetime.now()
    get_title_range()
    end_time = datetime.datetime.now() - start_time
    print(f"Done in {end_time.total_seconds():.2f} sec.")


if __name__ == '__main__':
    main()
