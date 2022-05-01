# songstem
Creates stems for an album or list of songs.

It separates the drums, bass or vocals from the given songs. It is based on demucs at: https://github.com/facebookresearch/demucs/blob/main/README.md.

Demucs allows to separate the drums, bass, vocals or other instruments from the original track. 


To install demucs just run:

```
python3 -m pip install -U demucs
```

The next thing is to add the songstem executable to the PATH. In UNIX:

```
export PATH=${PATH}":${HOME}/your/repositories/path/songstem/bin"
```

To permently add to the PATH include the line in your ```.bashrc``` or ```.zprofile```.

The available options are:

* ```-i, --input-dir```. The name of the directory where the songs are found. This is a mandatory argument.
* ```-f, --format```. The songs format (default: mp3). This is a mandatory argument.
* ```-s, --stem```. The stem that is going to be isolated (options: drums, bass, vocals, other). Default is value is other.
* ```-j```. Allow to specify a number of parallel jobs (e.g. demucs -j 2 myfile.mp3). This will multiply by the same amount the RAM used so be careful! Default value is 6 (This value depends on your computer number of cores)
* ```-id```. An identifier of the songs. For all the files in the directory use "*.". This can be useful to select individual songs (eg: "*Tears*.").

An example of how to run songstem is

```
songstem -i ThePoison -f wav -s other -j 2
```
