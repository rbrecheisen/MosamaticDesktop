import sys
import tomli # type: ignore
import tomli_w


def main(requirements_file):
    with open('mosamaticdesktop/pyproject.toml', 'rb') as f:
        data = tomli.load(f)
    print(data['tool']['briefcase']['app']['mosamaticdesktop'])
    with open(requirements_file, 'r') as f:
        requires = []
        start_including = False
        for line in f.readlines():
            line = line.strip()
            if line.startswith('# Application'):
                start_including = True
                continue
            if start_including:
                requires.append(line.strip())
        data['tool']['briefcase']['app']['mosamaticdesktop']['requires'] = requires
    with open('mosamaticdesktop/pyproject.toml', 'wb') as f:
        tomli_w.dump(data, f)


if __name__ == '__main__':
    requirements_file = 'requirements-windows.txt' if sys.argv[1] == 'windows' else 'requirements-macos.txt'
    main(requirements_file)