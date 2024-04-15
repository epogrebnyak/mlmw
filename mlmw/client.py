import pathlib
from dataclasses import dataclass
import httpx
from tqdm import tqdm


@dataclass
class TextBook:
    short: str
    url: str


class PDF(TextBook):
    @property
    def path(self):
        return pathlib.Path(f"{self.short}.pdf")


def download(path, url):
    print("Writing", path, "from", url)
    with path.open("wb") as f:
        with httpx.stream("GET", url, follow_redirects=True, timeout=10.0) as response:
            total = int(response.headers["Content-Length"])
            with tqdm(
                total=total, unit_scale=True, unit_divisor=1024, unit="B") as progress:
                num_bytes_downloaded = response.num_bytes_downloaded
                for chunk in response.iter_bytes():
                    f.write(chunk)
                    progress.update(
                        response.num_bytes_downloaded - num_bytes_downloaded
                    )
                    num_bytes_downloaded = response.num_bytes_downloaded


sources = [
    PDF(
        "ISLP",
        "https://drive.google.com/uc?export=download&id=1ajFkHO6zjrdGNqhqW1jKBZdiNGh_8YQ1",
    )
]
for source in sources:
    if not source.path.exists():
        download(source.path, source.url)
