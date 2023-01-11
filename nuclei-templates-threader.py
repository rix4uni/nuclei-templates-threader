import os
import argparse
import re

def add_threads(file_path, threads):
    # Open the file
    with open(file_path, 'r') as file:
        # Read the content of the file
        content = file.read()

    if ('network:') in content:
        pass
    elif ('headless:') in content:
        pass
    elif ('dns:') in content:
        pass
    elif ('file:') in content:
        pass
    elif ('ssl:') in content:
        pass
    elif ('workflows:') in content:
        pass
    elif 'threads:' not in content:
        content += '\n    threads: {}\n'.format(threads)
    else:
        # Use regular expression to find the 'threads' key and update its value
        content = re.sub(r'threads: \d+', 'threads: {}'.format(threads), content)

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory_path', type=str, help='Path to the directory containing YAML files')
    parser.add_argument('-t', '--threads', type=int, default=5, help='Number of threads to use')
    args = parser.parse_args()

    for dirpath, dirnames, filenames in os.walk(args.directory_path):
        for file_name in filenames:
            if file_name.endswith(".yaml"):
                file_path = os.path.join(dirpath, file_name)
                add_threads(file_path, args.threads)