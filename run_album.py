import os
import glob
import shutil

def album2BackTrack(files_dir,file_id, **kwargs):

    ### Optional arguments
    stems = kwargs["stems"] if "stems" in kwargs else other
    j = kwargs["j"] if "j" in kwargs else 2
    identifier = kwargs["identifier"] if "identifier" in kwargs else "*."

    ### List of all the files
    listOfFiles = sorted(glob.glob(files_dir+identifier+file_id))

    for f in listOfFiles:
        ### Compress white spaces
        f_nowhite = f.replace(" ", "") 
        ### Avoid strange characters
        if "(" in f_nowhite:
            f_nowhite=f_nowhite.replace("(","").replace(")","")
        if "," in f_nowhite:
            f_nowhite=f_nowhite.replace(",","")
        ### If the file exist with no white space we dont copy.
        try:
            shutil.copyfile(f, f_nowhite)
        except shutil.SameFileError:
            continue

        f = f_nowhite
        ### Name of the song
        name = f.split("/")[-1].split(".")[0]
        print("------------ Processing Song:{} -------------".format(name))

        ### Demucs command
        demucs = "demucs {} --two-stems={} -n mdx_extra -j {} -o {}".format(f, stems, j, files_dir)
        os.system(demucs)

        ### Output directory where the files are found
        f_dir = files_dir+"mdx_extra/" + name + "/"

        ### Creates Directory to separate stems 
        if not os.path.exists(files_dir+"{}/".format(stems)): os.mkdir(files_dir+"{}/".format(stems))
        if not os.path.exists(files_dir+"No_{}/".format(stems)): os.mkdir(files_dir+"No_{}/".format(stems))

        ### Move files to each directory
        #shutil.copyfile(f_dir+stems+".wav ", files_dir+"Guitar/"+name+"_Guitar.wav")
        #os.system("cp " + f_dir+stems+".wav " + files_dir+"Guitar/"+name+"_Guitar.wav")
        os.system("cp " + f_dir+stems+".wav " + files_dir+"{}/".format(stems) + name+"_{}.wav".format(stems))
        #shutil.copyfile(f_dir+"no_{}.wav ".format(stems),  files_dir+"BackingTracks/"+name+"_BackingTrack.wav")
        #os.system("cp "+ f_dir+"no_{}.wav ".format(stems) + files_dir+"BackingTracks/"+name+"_BackingTrack.wav")
        os.system("cp " + f_dir+"no_{}.wav ".format(stems) + files_dir+"No_{}/".format(stems) +name+"_no_{}.wav".format(stems))
        os.system("rm -rf {}mdx_extra/".format(files_dir))
        os.system("rm " + f)


if __name__ == "__main__":
    import sys
    import argparse
    from argparse import Action
    import os
   
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input-dir",
            action="store",
            dest="input",
            default=os.path.abspath("./"),
            help="Album directory where the songs are. ")

    parser.add_argument("-f", "--format",
            action="store",
            dest="format",
            default="mp3",
            help="Format of the input songs.")

    parser.add_argument("-s", "--stem",
            action="store",
            dest="stem",
            default="other",
            help="Type of stem you want: drums, bass, vocals, other.")

    parser.add_argument("-j",
            action="store",
            dest="j",
            type=int,
            default=6,
            help="number of parallel jobs")

    parser.add_argument("-id",
            action="store",
            dest="id",
            default="*.",
            help="Identifier of the songs. Use *. to select all files" )

    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
    
    if "/" not in args.input[-1]:
        args.input = args.input + "/"

    album2BackTrack(args.input, args.format, stems=args.stem, j=args.j, identifier=args.id)
    #album2BackTrack("Fever/", "mp3")

