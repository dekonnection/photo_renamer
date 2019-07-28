# photo_renamer

A simple script to rename your ugly and inconsistently named pictures, to something usable.

## Why

I was fed up with the pseudo-standard way digital photography files are named by cameras.

You end up with something like that :

```
DSCF0459.JPG
DSCF0459.RAF
DSCF0460.JPG
DSCF0460.RAF
DSCF0461.JPG
DSCF0461.RAF
DSCF0462.JPG
DSCF0462.RAF
DSCF0463.JPG
DSCF0463.RAF
DSCF0464.JPG
DSCF0464.RAF
```

Problems :

* It's not informative :
  * you cannot even know which year this photo has been taken
  * ... or with which camera
* The ordering is broken / you can have name clashes :
  * If you use multiple cameras at the same event, bye bye chronology
  * If you take more than 9999 photographs whith a camera, you go back to DSCF0001.JPG
  * On my camera, if I apply a new RAW development on an existing picture, this creates a new serial (as if you had shot a new pic) for the resulting JPEG : one picture, two very different names.
* It's ugly.

I find way better to rename them with a consistent template like this one :

```
<date>-<time>_<camera_model>_<original_serial>.ext
```

This way, you get :

* consistent chronology
* more information when handling files
* no name clashes, even if you choose to mix files from different cameras (I wouldn't do that for storage, but when curating photos for a web gallery ...)
* no information loss : we keep the original serial, if you need it.

## Requirements

* Python 3.6
* modules :
  * exif

I use poetry to handle my venv and modules, but this is not a requirement.

I only tested the script with files from my Fujifilm cameras, but since it gets information from standard EXIF fields, this should be compatible with almost 100% of digital cameras.

(if this is not the case, feel free to open an issue)

## Usage

You just need to pass your files to the `-f` flag, separated by spaces.

(so if you need to rename an entire directory, `-f *.JPG` will do the job)

```
$ python -m photo_renamer -f ./pics/*
Welcome to photo_renamer !
(this is unsupported software, please make backups before using it)


Your files would be renamed like this :

./pics/DSCF0459.JPG => ./pics/20190714-093518_X-T2_DSCF0459.JPG : (preview)
./pics/DSCF0459.RAF => ./pics/20190714-093518_X-T2_DSCF0459.RAF : (preview)
./pics/DSCF0460.JPG => ./pics/20190714-093647_X-T2_DSCF0460.JPG : (preview)
./pics/DSCF0460.RAF => ./pics/20190714-093647_X-T2_DSCF0460.RAF : (preview)
./pics/DSCF0461.JPG => ./pics/20190714-093703_X-T2_DSCF0461.JPG : (preview)
./pics/DSCF0461.RAF => ./pics/20190714-093703_X-T2_DSCF0461.RAF : (preview)
./pics/DSCF0462.JPG => ./pics/20190714-093715_X-T2_DSCF0462.JPG : (preview)
./pics/DSCF0462.RAF => ./pics/20190714-093715_X-T2_DSCF0462.RAF : (preview)
./pics/DSCF0463.JPG => ./pics/20190714-093731_X-T2_DSCF0463.JPG : (preview)
./pics/DSCF0463.RAF => ./pics/20190714-093731_X-T2_DSCF0463.RAF : (preview)
./pics/DSCF0464.JPG => ./pics/20190714-093837_X-T2_DSCF0464.JPG : (preview)
./pics/DSCF0464.RAF => ./pics/20190714-093837_X-T2_DSCF0464.RAF : (preview)

Is this OK with you ? (y/N)y

Renaming :

./pics/DSCF0459.JPG => ./pics/20190714-093518_X-T2_DSCF0459.JPG : OK (renamed successfully)
./pics/DSCF0459.RAF => ./pics/20190714-093518_X-T2_DSCF0459.RAF : OK (renamed successfully)
./pics/DSCF0460.JPG => ./pics/20190714-093647_X-T2_DSCF0460.JPG : OK (renamed successfully)
./pics/DSCF0460.RAF => ./pics/20190714-093647_X-T2_DSCF0460.RAF : OK (renamed successfully)
./pics/DSCF0461.JPG => ./pics/20190714-093703_X-T2_DSCF0461.JPG : OK (renamed successfully)
./pics/DSCF0461.RAF => ./pics/20190714-093703_X-T2_DSCF0461.RAF : OK (renamed successfully)
./pics/DSCF0462.JPG => ./pics/20190714-093715_X-T2_DSCF0462.JPG : OK (renamed successfully)
./pics/DSCF0462.RAF => ./pics/20190714-093715_X-T2_DSCF0462.RAF : OK (renamed successfully)
./pics/DSCF0463.JPG => ./pics/20190714-093731_X-T2_DSCF0463.JPG : OK (renamed successfully)
./pics/DSCF0463.RAF => ./pics/20190714-093731_X-T2_DSCF0463.RAF : OK (renamed successfully)
./pics/DSCF0464.JPG => ./pics/20190714-093837_X-T2_DSCF0464.JPG : OK (renamed successfully)
./pics/DSCF0464.RAF => ./pics/20190714-093837_X-T2_DSCF0464.RAF : OK (renamed successfully)
```
