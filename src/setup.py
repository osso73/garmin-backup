from cx_Freeze import setup, Executable


# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {
    'packages': [], 
    'excludes': [],
    'zip_include_packages': [],
    }

base = 'console'

executables = [
    Executable(
        'garmin-backup.py', 
        base=base,
        icon='../icon.ico'
    ),
]

setup(name='garmin-backup',
      version = '0.6',
      description = 'Some scripts to enhance your Windows experience',
      options = {'build_exe': build_options},
      executables = executables)
