import pafy
def extract_audio(url):
    FOLDER=""#path for downloaded audio
    video=pafy.new(url)
    audios=video.audiostreams
    best_audio=video.getbestaudio()
    best_video=video.getbest()
    best_audio.download(filepath = FOLDER)
    best_video.download(filepath=FOLDER)
    return FOLDER

#test url:https://www.youtube.com/watch?v=klyJChzMvtQ
