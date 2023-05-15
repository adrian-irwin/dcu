import os
import sys
import stat

# path = '.'
if len(sys.argv) == 1:
    path = '.'
else:
    path = sys.argv[1]

files = os.listdir(path)

for name in files:
    # print(name)
    full_path = os.path.join(path, name)
    print(full_path)

    stats = os.stat(full_path)
    print(f'Size: {stats.st_size} bytes')
    print(f'Permissions: {stat.filemode(stats.st_mode)}')
    print('  ' + ('file' if stats.st_mode & 0o0100000 else '-' ))
    print('  ' + ('dir' if stats.st_mode & 0o0040000 else '-' ))
    print()

