import ffmpeg
import subprocess
from pydub import AudioSegment

def mainRoute():
    makeAudioFromVideo('./target/target.mp4')
    addSilenceAudio('./soundOnly.mp4',3*60)
    mergeVideoAudio('./movieOnly.mp4','./addSilenceAudio.mp4')

def makeAudioFromVideo(filePath):
    cmd = ['ffmpeg','-i',filePath,'-vcodec','copy','-map','0:0','movieOnly.mp4']
    cmd2 =['ffmpeg','-i',filePath,'-acodec','copy','-map','0:1','soundOnly.mp4']
    subprocess.run(cmd)
    subprocess.run(cmd2)

def addSilenceAudio(filePath,second):
    silence = AudioSegment.silent(duration=second*1000)
    data = AudioSegment.from_file(filePath,'mp4')
    result = silence + data
    result.export('addSilenceAudio.mp4',format='mp4')

def mergeVideoAudio(videoFilePath,audioFilePath):
    cmd = ['ffmpeg','-i',videoFilePath,'-vcodec','copy','-i',audioFilePath,'-acodec','copy','result/finalResult.mp4']
    subprocess.run(cmd)

if __name__ == '__main__':
    mainRoute()
