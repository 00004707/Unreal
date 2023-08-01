@echo off

SET "subdir=source/Editor"
SET "currentdir=%cd%

for /R "%subdir%" /D %%d in (*) do (
	
	cd /d %%d

	for %%F in (*.gif) do (
		ffmpeg -n -i "%%d\%%~nxF" -vcodec webp -loop 0 -pix_fmt yuv420p "%%d\%%~nF.webp"    
	)

	for %%F in (*.png) do (
		ffmpeg -n -i "%%d\%%~nxF" -vcodec webp -loop 0 -pix_fmt yuv420p "%%d\%%~nF.webp"
	)

	for %%F in (*.mp4) do (
		ffmpeg -n -i "%%d\%%~nxF" -filter:v fps=24 -vcodec webp -loop 0 -pix_fmt yuv420p "%%d\%%~nF.webp"
	)
)

cd /d "%currentdir%"