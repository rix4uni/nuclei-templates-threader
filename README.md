# nuclei-templates-threader

This tool add threads with all .yaml nuclei-templates

# Steps
```
python3 nuclei-templates-threader.py -d ~/nuclei-templates -t 50
cp -r ~/nuclei-templates ~/custom-nuclei-templates
rm -rf ~/nuclei-templates && ~/nuclei --update-templates
```
# Usage
```
usage: nuclei-templates-threader.py [-h] [-d DIRECTORY_PATH] [-t THREADS]

options:
  -h, --help            show this help message and exit
  -d DIRECTORY_PATH, --directory_path DIRECTORY_PATH
                        Path to the directory containing YAML files
  -t THREADS, --threads THREADS
                        Number of threads to use (default 5)
```
