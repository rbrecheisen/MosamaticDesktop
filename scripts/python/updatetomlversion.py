import argparse
import tomli # type: ignore
import tomli_w


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('version', help='Version to use to update pyproject.toml')
    args = parser.parse_args()

    with open('mosamaticdesktop/pyproject.toml', 'rb') as f:
        data = tomli.load(f)
    data['tool']['briefcase']['version'] = args.version
    with open('mosamaticdesktop/pyproject.toml', 'wb') as f:
        tomli_w.dump(data, f)
    print(f'Updated pyproject.toml version to {args.version}')


if __name__ == '__main__':
    main()