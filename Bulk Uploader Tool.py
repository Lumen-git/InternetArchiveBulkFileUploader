import internetarchive
import os
import shutil

#UPLOADER CONFIG
path = ""   #Path to upload files from
fileEXT = ""    #File type to upload (i.e. .txt)
safetyPath = "" #Reletive path to move uploaded files to

#INTERNET ARCHIVE METADATA CONFIG
IAcollection = ""   #Internet Archive Collection to uplaod to
IAtype = "" #Tpye of media being uploaded

#Valid Collections
# opensource
# opensource_audio
# opensource_movies
# opensource_media
# opensource_image
# open_source_software
# test_collection

#Valid File Types
# data
# texts
# audio
# movies
# software
# web


#Below is the magic working code

uploadList = []


CurrentFiles = os.listdir(path)
for file in CurrentFiles:
    if file[-4:] == fileEXT:
        uploadList.append(file)

for file in uploadList:
    EXTBig = fileEXT.title()
    FileName = file.title().replace(EXTBig,fileEXT).replace(" ","_").replace("(","").replace(")","").replace("_-","").replace("-_","_").replace(",_",",").replace("__","_").strip()
    meta_data = (dict(collection=IAcollection,title=str(FileName),mediatype="software"))
    uploadFile = path + file
    print("Uploading {} as {} from {}...".format(file, FileName, uploadFile))
    try:
        internetarchive.upload(str(FileName),files=str(uploadFile),metadata=meta_data)
    except:
        print("An Error Occured!")

    else:
        print("Uploaded {}".format(file))
        original = path + file
        newPlace = path + safetyPath + file
        os.rename(original, newPlace)



input("Finished!")
