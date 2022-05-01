# songstem
Creates stems for an album or list of songs.

It separates the drums, bass or vocals from the given songs. It is based on demucs at: https://github.com/facebookresearch/demucs/blob/main/README.md.



To install all the dependencies just run:

```
pip install -r requirements.txt
```

The next thing is to add the executable to the PATH. In UNIX:

```
export PATH=${PATH}":${HOME}/your/repositories/path/songstem/bin"
```

To permently add to the PATH include the line in your ```.bashrc``` or ```.zprofile```.
