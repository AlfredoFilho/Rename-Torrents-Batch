# Rename-Torrents-Batch

Rename multiple torrents with the hash name to the title.

#### Example:
##### Before
```bash
c48344299a520b2b269ca956f5403dab9c4bc998.torrent
```
##### After
```bash
[3.97 GiB] ubuntu-20.04.6-live-server-amd64.iso.torrent
```

#### How to use:
##### 1. Clone
```bash
git clone https://github.com/AlfredoFilho/Rename-Torrents-Batch.git
```
##### 2. Install dependencies
```bash
pip3 install requirements.txt
```
##### 3. Run
```bash
python3 rename-torrents-batch.py
```

#### Details:
##### Input:
- The folder with the files with hash names.
##### Output:
- In the project folder a folder will be created (`OutputTorrents/`) with the new renamed files.
```bash
[<total size torrent>] <torrent title>.torrent
```
- In the project folder, a CSV will be generated (`data.csv`) with the key and value of the old names for the new ones.

| oldNames | newNames |
|---|---|
| c48344299a520b2b269ca956f5403dab9c4bc998.torrent | [3.97 GiB] ubuntu-20.04.6-live-server-amd64.iso.torrent |