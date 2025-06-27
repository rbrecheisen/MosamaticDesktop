import tomli # type: ignore
import tomli_w


def main():
    with open('mosamaticdesktop/pyproject.toml', 'rb') as f:
        data = tomli.load(f)
    print(data['tool']['briefcase']['app']['mosamaticdesktop'])
    with open('requirements.txt', 'r') as f:
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
    main()