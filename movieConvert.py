import ffmpeg
import subprocess
import os
from pydub import AudioSegment

def mainRoute():
    makeAudioFromVideo('./target/target.mp4')
    addSilenceAudio('./soundOnly.mp4',3*60)
    mergeVideoAudio('./movieOnly.mp4','./addSilenceAudio.mp4')
    os.remove("./soundOnly.mp4")
    os.remove("./movieOnly.mp4")
    os.remove("./addSilenceAudio.mp4")

def makeAudioFromVideo(filePath):
    cmd = ['ffmpeg','-i',filePath,'-vcodec','copy','-map','0:0','movieOnly.mp4']
    cmd2 =['ffmpeg','-i',filePath,'-acodec','copy','-map','0:1','soundOnly.mp4']
    subprocess.run(cmd)
    subprocess.run(cmd2)

def addSilenceAudio(filePath,second):
    silence = AudioSegment.silent(duration=second*1000)
    data = AudioSegment.from_file(filePath,'mp4')
    result = silence + data
    result = result + 20
    result.export('addSilenceAudio.mp4',format='mp4')

def mergeVideoAudio(videoFilePath,audioFilePath):
    cmd = ['ffmpeg','-i',videoFilePath,'-i',audioFilePath,'-vcodec','copy','-acodec','copy','result/finalResult.mp4']
    subprocess.run(cmd)

def uploadToYoutube(filePath):
    pass

if __name__ == '__main__':
    mainRoute()
