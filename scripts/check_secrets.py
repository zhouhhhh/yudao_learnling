"""Check tracked files for common cloud access-key IDs without printing values.

Usage: python scripts/check_secrets.py [--history]
This targeted check does not replace GitHub secret scanning.
"""
import argparse
import re
import subprocess
from pathlib import Path

PATTERN = re.compile(rb'(?:AKID[0-9A-Za-z]{16,}|LTAI[0-9A-Za-z]{12,}|AKLT[0-9A-Za-z]{12,})')
ROOT = Path(__file__).resolve().parents[1]


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--history', action='store_true', help='also check all commits reachable from HEAD')
    args = parser.parse_args()
    hits = []
    for entry in git('ls-files', '-z').split(b'\0'):
        if not entry:
            continue
        path = entry.decode('utf-8')
        file = ROOT / path
        if file.is_file() and PATTERN.search(file.read_bytes()):
            hits.append(f'working tree: {path}')
    if args.history:
        for commit in git('rev-list', 'HEAD').decode().splitlines():
            # Git grep emits filenames only, never matched credential values.
            result = subprocess.run(
                ['git', 'grep', '-I', '-l', '-E',
                 'AKID[0-9A-Za-z]{16,}|LTAI[0-9A-Za-z]{12,}|AKLT[0-9A-Za-z]{12,}', commit],
                cwd=ROOT, capture_output=True)
            if result.returncode not in (0, 1):
                raise RuntimeError('History check failed; results are incomplete.')
            hits.extend(result.stdout.decode('utf-8').splitlines())
    if hits:
        print('Potential cloud credentials found (values hidden):')
        print('\n'.join(hits))
        return 1
    print('No targeted cloud access-key ID patterns found in checked files.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
