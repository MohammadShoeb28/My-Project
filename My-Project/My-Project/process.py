#converts the videos to mp3
import os
# import subprocess
files=os.listdir("videos")
for file in files:
    tutorial_number=file.split("[")[0].split("#")[1]
    file_name=file.split(" l ")[0]
    print(tutorial_number,file_name)

##ffmpeg is a open source command line framework used to record,convert,stream and edit video..
    # subprocess.run(["ffmpeg","-i",f"videos/{file}",f"audio/{tutorial_number}_{file_name}.mp3"])