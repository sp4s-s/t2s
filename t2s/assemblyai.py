# pip install assemblyai

import assemblyai as aai

aai.settings.api_key = ""
transcript = aai.Transcriber().transcribe("file")
subs = transcript.export_subtitles_srt()

f = open("subfile.srt", "a")
f.write(subs)
f.close()