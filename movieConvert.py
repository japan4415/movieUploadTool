import ffmpeg
import subprocess
import os
from pydub import AudioSegment

def mainRoute(fileName):
    makeAudioFromVideo('./target/'+fileName+'.mp4',fileName)
    addSilenceAudio('./'+fileName+'soundOnly.mp4',3*60,fileName)
    mergeVideoAudio('./'+fileName+'movieOnly.mp4','./'+fileName+'addSilenceAudio.mp4',fileName)
    os.remove("./"+fileName+"soundOnly.mp4")
    os.remove("./"+fileName+"movieOnly.mp4")
    os.remove("./"+fileName+"addSilenceAudio.mp4")

def makeAudioFromVideo(filePath,fileName):
    cmd = ['ffmpeg','-i',filePath,'-vcodec','copy','-map','0:0',fileName+'movieOnly.mp4']
    cmd2 =['ffmpeg','-i',filePath,'-acodec','copy','-map','0:1',fileName+'soundOnly.mp4']
    subprocess.run(cmd)
    subprocess.run(cmd2)

def addSilenceAudio(filePath,second,fileName):
    silence = AudioSegment.silent(duration=second*1000)
    data = AudioSegment.from_file(filePath,'mp4')
    result = silence + data
    result = result + 20
    result.export(fileName+'addSilenceAudio.mp4',format='mp4')

def mergeVideoAudio(videoFilePath,audioFilePath,fileName):
    cmd = ['ffmpeg','-i',videoFilePath,'-i',audioFilePath,'-vcodec','copy','-acodec','copy','result/'+fileName+'.mp4']
    subprocess.run(cmd)

def uploadToYoutube(filePath):
    pass

if __name__ == '__main__':
    fileList = os.listdir('./target')
    mp4List = []
    for file in fileList:
        if 'mp4' in file:
            mp4List.append(file.split('.')[0])
    for mp4 in mp4List:
        mainRoute(mp4)
