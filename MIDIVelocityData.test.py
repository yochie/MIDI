from MIDIVelocityData import *
import os


MIDIFilesOnThisMachine = ['D:/Downloads/1.mid'
                         ]

FilesToOverwrite = ['D:/Downloads/2.mid'
                   ]


for i in range(1):
    vd = LoadVelocityDatafromMIDIFile(MIDIFilesOnThisMachine[i])
    SaveVelocityDatatoMIDIFile(vd, FilesToOverwrite[i])
    vd2 = LoadVelocityDatafromMIDIFile(FilesToOverwrite[i])
    assert(vd.shape == vd2.shape)

    for t in range(max(vd.shape[0],vd2.shape[0])):
        for n in MIDINotes:
            if t < vd.shape[0] and t < vd2.shape[0]:
                if not (vd[t,n] == vd2[t,n]):
                    print(("vd[{},{}] == {}, vd2[{},{}] == {}".format(t,n,vd[t,n],t,n,vd2[t,n])))
            elif t < vd.shape[0]:
                if vd[t,n] > 0:
                    print(("vd[{},{}] == {}, vd2[{},{}] == Missing".format(t,n,vd[t,n],t,n)))
            elif t < vd2.shape[0]:
                if vd2[t,n] > 0:
                    print(("vd[{},{}] == MISSING, vd2[{},{}] == Missing".format(t,n,t,n,vd2[t,n])))




