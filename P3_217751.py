import os


# EXCERCICI 1
# REF: http://underpop.online.fr/f/ffmpeg/help/hls-2.htm.gz
# https://sonnati.wordpress.com/2011/08/30/ffmpeg-%E2%80%93-the-swiss-army-knife-of-internet-streaming-%E2%80%93-part-iv/

def container_HLS(input_video):
    com = 'ffmpeg -i ' + input_video + ' -c:v h264 -flags +cgop -g 30 -hls_time 1 out.m3u8'
    os.system(com)


# EXERCICI 3
# REF: https://trac.ffmpeg.org/wiki/StreamingGuide
def streaming(input_video):
    com = 'ffmpeg -re -i ' + input_video + ' -f mpegts udp://192.168.1.219'
    os.system(com)


if __name__ == '__main__':
    # container_HLS('BBB_1_min.mp4')
    streaming('BBB_1_min.mp4')
