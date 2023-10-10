#!/usr/bin/env python3
"""Util to easly fetch sample xls files."""

import logging
from dataclasses import dataclass
from urllib.error import HTTPError
from urllib.request import Request, urlopen

logging.basicConfig(encoding="utf-8", level=logging.INFO, format="%(asctime)-15s %(levelname)-8s | %(message)s")


@dataclass
class Source:
    """Class representing a source"""

    url: str
    filename: str

    def download_from_source(self):
        """Function used to download files."""
        logging.info("Fetching %s", self.filename)
        request = Request(url=self.url, headers={"User-Agent": "Mozilla/5.0"})
        try:
            with urlopen(url=request, timeout=10) as connection:
                data = connection.read()
        except HTTPError as exp:
            logging.exception(exp)
        else:
            with open(self.filename, "wb") as output:
                output.write(data)


def get_samples():
    """Function fetching samples."""
    sample_list = [
        Source(url="https://www.cmu.edu/blackboard/files/evaluate/tests-example.xls", filename="example.xls"),
        Source(url="https://www.dwsamplefiles.com/?dl_id=179", filename="sample1.xls"),
        Source(url="https://www.dwsamplefiles.com/?dl_id=180", filename="sample2.xls"),
    ]

    for sample in sample_list:
        sample.download_from_source()


if __name__ == "__main__":
    get_samples()
