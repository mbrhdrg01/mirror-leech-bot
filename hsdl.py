import os
import subprocess
import argparse


print("__________________________________\n\n")
print("Tej Hotstar NON DRM DOWNLOADER")
print("__________________________________\n\n")


currentFile = "wv.mkv"
realPath = os.path.realpath(currentFile)
dirPath = os.path.dirname(realPath)
dirName = os.path.basename(dirPath)

ytdlp = dirPath + '/bin/yt-dlp.exe'
aria2c = dirPath + '/bin/aria2c.exe'
mp4decrypt = dirPath + '/bin/mp4decrypt.exe'
mkvmerge = dirPath + '/bin/mkvmerge.exe'

arguments = argparse.ArgumentParser()
arguments.add_argument("-l", dest="url", help="url")
args = arguments.parse_args()

def download():
   print("[Downloading] Downloading From Url")

   url = args.url
   filename = subprocess.run([ytdlp,'--cookies-from-browser','chrome','--get-filename','--allow-unplayable-formats',url,'--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36', '--no-check-certificate','-o','%(title)s'],shell = True)
   subprocess.run([ytdlp, '-k', '--allow-unplayable-formats', '--cookies-from-browser','chrome','--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36', '--no-check-certificate', '-F', url],shell= True)
   formats = input("IF THE VIDEO AND AUDIO SEPARATE ??....CLICK 'yes/no' \n")
   if formats == ("yes"):
      v_id = input("Input Video ID : ")
      a_id = input("Input Audio ID 1: ")
      a_id2 = input("Input Audio ID 2: ")
      subprocess.run([ytdlp,'-k','--cookies-from-browser','chrome','--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36','--external-downloader', aria2c, '--allow-unplayable-formats','--no-check-certificate','-o','Video.mp4', '-f',v_id, url],shell = True)
      subprocess.run([ytdlp,'-k','--cookies-from-browser','chrome','--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36','--external-downloader', aria2c, '--allow-unplayable-formats','--no-check-certificate','-o', 'Audio.m4a','-f',a_id,url],shell = True)
      subprocess.run([ytdlp,'-k','cookies-from-browser','chrome','--user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36','--external-downloader', aria2c, '--allow-unplayable-formats','--no-check-certificate','-o', 'Audio2.m4a','-f', a_id2,url],shell = True)
   elif formats==("no"):
     f_id = input("Input Format ID : ")
     subprocess.run([ytdlp,'--cookies-from-browser','chrome','--external-downloader','aria2c', '--allow-unplayable-formats','--no-check-certificate','-o','"%(title)s.%(ext)s"' , '--external-downloader-args', '-x 16 -s 16 -k 1M','-f', f_id, url],shell = True)
   
download()


def merger():
    output = input("Enter The File Name Without Extension: ")
    print("[Merging] Merging Decrypted Content...")
    subprocess.run([mkvmerge, '--ui-language' ,'en', '--output', output +'Tele_Pirate.mkv','--track-name','0:Tele_Pirate','--track-name','1:Tele_Pirate','--track-name','2:Tele_Pirate', '--language', '0:und', '--default-track', '0:yes', '--compression', '0:none', 'Video.mp4', '--language', '0:und', '--default-track', '0:yes', '--compression' ,'0:none', '.Audio.m4a','--language', '0:id', '--language', '0:und', '--default-track', '0:yes', '--compression' ,'0:none', 'Audio2.m4a','--language', '0:id'])

merger()





