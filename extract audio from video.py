import pafy
url=""#video url link
FOLDER=""#path for downloaded audio
video=pafy.new(url)
audios=video.audiostreams
best_audio=video.getbestaudio()
best_audio.download(filepath = FOLDER)
