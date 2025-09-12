@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=source
set BUILDDIR=build

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.https://www.sphinx-doc.org/
	exit /b 1
)

REM Check if sphinx-autobuild exists when livehtml is requested
if "%1" == "live" (
    sphinx-autobuild --version >NUL 2>NUL
    if errorlevel 9009 (
        echo.
        echo.The 'sphinx-autobuild' command was not found. Install it with:
        echo.    pip install sphinx-autobuild
        echo.
        exit /b 1
    )
    goto live
)

if "%1" == "" goto help

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:live
echo Starting live server (Ctrl+C to stop)...
echo.
sphinx-autobuild -b html "%SOURCEDIR%" "%BUILDDIR%/html" --port 8000 --open-browser %SPHINXOPTS%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
