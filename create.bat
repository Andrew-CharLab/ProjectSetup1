@echo off

set fn=%1
set flag=%2
cd /d %~dp0

If "%1"=="" (
    echo "error"
) else ( 
    if "%2"=="" (
        python C:\Playarea\Projects\Python\ProjectSetup1\remote.py %fn% %flag%
        ) else (
            if "%2"=="l" (
                C:\Playarea\Projects\Python\ProjectSetup1\python local.py %fn%
            )
        )
    )
