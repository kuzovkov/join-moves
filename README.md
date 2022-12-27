###Merge video files from IP camera's SD card

put `join.py` for root of day folder
uncomment line according output format you need (mp4 or mkv)
```python
#command = 'ffmpeg -f concat -safe 0 -i movies.txt -c copy output.mkv'
command = 'ffmpeg -f concat -safe 0 -i movies.txt -c:v copy -c:a aac -strict experimental output.mp4'
```

####Run script

```bash
chmod a+x join.py
./join.py
```

####Output example:
```bash
user1@kuzovkov-pc:/media/user1/400C8B560C8B45BE/training/20221226$ ./join.py
Join video /media/user1/400C8B560C8B45BE/training/20221226
ffmpeg version 2.8.17-0ubuntu0.1 Copyright (c) 2000-2020 the FFmpeg developers
  built with gcc 5.4.0 (Ubuntu 5.4.0-6ubuntu1~16.04.12) 20160609
  configuration: --prefix=/usr --extra-version=0ubuntu0.1 --build-suffix=-ffmpeg --toolchain=hardened --libdir=/usr/lib/x86_64-linux-gnu --incdir=/usr/include/x86_64-linux-gnu --cc=cc --cxx=g++ --enable-gpl --enable-shared --disable-stripping --disable-decoder=libopenjpeg --disable-decoder=libschroedinger --enable-avresample --enable-avisynth --enable-gnutls --enable-ladspa --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libcdio --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme --enable-libgsm --enable-libmodplug --enable-libmp3lame --enable-libopenjpeg --enable-libopus --enable-libpulse --enable-librtmp --enable-libschroedinger --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libssh --enable-libtheora --enable-libtwolame --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx265 --enable-libxvid --enable-libzvbi --enable-openal --enable-opengl --enable-x11grab --enable-libdc1394 --enable-libiec61883 --enable-libzmq --enable-frei0r --enable-libx264 --enable-libopencv
  libavutil      54. 31.100 / 54. 31.100
  libavcodec     56. 60.100 / 56. 60.100
  libavformat    56. 40.101 / 56. 40.101
  libavdevice    56.  4.100 / 56.  4.100
  libavfilter     5. 40.101 /  5. 40.101
  libavresample   2.  1.  0 /  2.  1.  0
  libswscale      3.  1.101 /  3.  1.101
  libswresample   1.  2.101 /  1.  2.101
  libpostproc    53.  3.100 / 53.  3.100
Guessed Channel Layout for  Input Stream #0.0 : mono
Input #0, concat, from 'movies.txt':
  Duration: N/A, start: 0.000000, bitrate: 960 kb/s
    Stream #0:0(und): Audio: pcm_alaw (alaw / 0x77616C61), 8000 Hz, 1 channels, s16, 64 kb/s
    Metadata:
      creation_time   : 2022-12-26 16:22:22
    Stream #0:1(und): Video: hevc (Main) (hvc1 / 0x31637668), yuv420p(tv, unknown/bt709/unknown), 2304x1296, 896 kb/s, 20 fps, 20 tbr, 90k tbn, 20 tbc
    Metadata:
      creation_time   : 2022-12-26 16:22:22
File 'output.mp4' already exists. Overwrite ? [y/N] y
[aac @ 0x25c4120] Too many bits per frame requested, clamping to max
[mp4 @ 0x2607100] Codec for stream 0 does not use global headers but container format requires global headers
Output #0, mp4, to 'output.mp4':
  Metadata:
    encoder         : Lavf56.40.101
    Stream #0:0(und): Video: hevc ([35][0][0][0] / 0x0023), yuv420p, 2304x1296, q=2-31, 896 kb/s, 20 fps, 20 tbr, 90k tbn, 90k tbc
    Metadata:
      creation_time   : 2022-12-26 16:22:22
    Stream #0:1(und): Audio: aac ([64][0][0][0] / 0x0040), 8000 Hz, mono, fltp, 48 kb/s
    Metadata:
      creation_time   : 2022-12-26 16:22:22
      encoder         : Lavc56.60.100 aac
Stream mapping:
  Stream #0:1 -> #0:0 (copy)
  Stream #0:0 -> #0:1 (pcm_alaw (native) -> aac (native))
Press [q] to stop, [?] for help
frame=97117 fps=6105 q=-1.0 Lsize=  695649kB time=01:21:00.36 bitrate=1172.5kbits/s    
video:669752kB audio:24674kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 0.176095%

```
