:: http://gis.stackexchange.com/a/144909

REM Change OSGeo4W_ROOT to point to your install of QGIS.

SET OSGEO4W_ROOT=C:\Program Files\QGIS Wien
SET QGISNAME=qgis
SET QGIS=%OSGEO4W_ROOT%\apps\%QGISNAME%
set QGIS_PREFIX_PATH=%QGIS%

CALL "%OSGEO4W_ROOT%\bin\o4w_env.bat"

: Python Setup
set PATH=%OSGEO4W_ROOT%\bin;%QGIS%\bin;%PATH%
SET PYTHONHOME=%OSGEO4W_ROOT%\apps\Python27
set PYTHONPATH=%QGIS%\python;%PYTHONPATH%

ECHO OSGeo path is: %OSGEO4W_ROOT%
ECHO Getting QGIS libs from: %QGIS%
ECHO Python loaded from: %PYTHONHOME%

c:\python27\python.exe standalone_generate_pdf.py