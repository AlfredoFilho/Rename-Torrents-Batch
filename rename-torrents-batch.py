#!/usr/bin/env python3
import os
import csv
from pathlib import Path
from torrentool.api import Torrent
from pathvalidate import sanitize_filename


def human_readable_size(size, decimal_places=2):
    for unit in ["B", "KiB", "MiB", "GiB", "TiB", "PiB"]:
        if size < 1024.0 or unit == "PiB":
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"


def create_output_folder():
    counter = 1
    folderName = "OutputTorrents"
    path = folderName

    while os.path.isdir(path):
        path = folderName + str(counter)
        counter += 1

    os.mkdir(path)
    return path


def main(inputDir, outputDir):
    files = [file for file in os.listdir(f"{inputDir}") if file.endswith(".torrent")]

    csvFile = csv.writer(open('data.csv', 'w'))

    for file in files:
        torrent = Torrent.from_file(os.path.join(inputDir, file))
        size = human_readable_size(torrent.total_size)

        newTorrentName = sanitize_filename(f'[{size}] {torrent.name}.torrent')
        pathToFile = os.path.join(outputDir, newTorrentName)

        torrent.to_file(pathToFile)
        csvFile.writerow(
            [f'{file}', f'{str(newTorrentName).replace(",", "")}'])

    print(f'Output Dir: {os.path.join(os.getcwd(), outputDir)}')


if __name__ == "__main__":
    inputDir = Path(input("Enter torrent folder path: "))
    outputDir = create_output_folder()
    main(inputDir, outputDir)
