#!/usr/bin/env python3
"""Util to easly fetch sample xls files."""

import json
import logging
from dataclasses import dataclass
from urllib.error import HTTPError
from urllib.request import Request, urlopen

logging.basicConfig(encoding="utf-8", level=logging.INFO, format="%(asctime)-15s %(levelname)-8s | %(message)s")


@dataclass
class SampleSource:
    """Class representing a source"""

    remote_url: str
    local_filename: str


def download_from_source(source: SampleSource):
    """Function used to download files."""

    logging.info("Fetching %s", source.local_filename)
    request = Request(url=source.remote_url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(url=request, timeout=10) as connection:
            data = connection.read()
    except HTTPError as exp:
        logging.exception(exp)
    else:
        with open(source.local_filename, "wb") as output:
            output.write(data)


def get_samples():
    """Function used to fetch samples."""

    with open("samples.json", encoding="utf-8") as config_file:
        sample_configs = json.load(config_file).get("samples")

    for sample_config in sample_configs:
        download_from_source(
            SampleSource(remote_url=sample_config.get("remote_url"), local_filename=sample_config.get("local_filename"))
        )


if __name__ == "__main__":
    get_samples()
