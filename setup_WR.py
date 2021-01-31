import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    # 'packages': ['main'],
}
setup(
    name='Weather_Reminder',
    version='0.0.1',
    description='Weather Reminder for Jove',
    options={
        'build_exe': build_exe_options
    },
    executables=[Executable('Weather_Reminder.py',
                            base='Win32GUI',
                            targetName='Weather_Reminder.exe',
                            )]
)
