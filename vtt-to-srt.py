import pathlib as pl
import easygui as eg
import webvtt

# PATHS #

print("Select folder of VTT files.")
VTT_path = pl.Path(eg.diropenbox())

print("Select folder where SRT files will be saved.")
SRT_path = pl.Path(eg.diropenbox())

# CONVERTING VTT FILES #

for VTTFile in VTT_path.glob("*.vtt"):
    print(f"Converting: {VTTFile.name}...")
    
    # Set save path.
    save_path = SRT_path / (f"{VTTFile.stem}.srt")
    
    # Read VTT contents.
    VTTcontents = webvtt.read(str(VTTFile))
    
    # Convert to SRT.
    try:
        VTTcontents.save_as_srt(str(save_path))
        print(f"{VTTFile.name} converted succesfully!")
        
    except:
        print(f"Failed to convert {VTTFile.name} due to {webvtt.errors}")

input("Done! Press any key to continue...")