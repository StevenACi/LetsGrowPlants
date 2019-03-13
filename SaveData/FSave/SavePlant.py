import base64
import pickle
import encodings


def rootRecursion(rootAtts, recursedRoot, parentRoot):
    ###attributes are vites, heights, parentNames
    rootAtts[0] += str(recursedRoot.vite) + ","
    rootAtts[1] += str(recursedRoot.height) + ","
    rootAtts[2] += str(recursedRoot.name) + ","
    rootAtts[3] += str(parentRoot.name) + ","

    for c in recursedRoot.children:
        rootAtts = branchrecursion(rootAtts, c, recursedRoot)

    return rootAtts

def saveRoot(plant):

    rootSave = {'Vitalities': 0, 'Lengths': 0, 'Names': "", 'ParentNames':""}
    roots = plant.roots
    rootAtts= ["","","",""]

    for r in roots:
        rootAtts[0] += str(r.vite) + ","
        rootAtts[1] += str(r.length) + ","
        rootAtts[2] += str(r.name) + ","
        rootAtts[3] += str(r.name) + ","

    rootSave["Vitalities"] = rootAtts[0]
    rootSave["Lengths"] = rootAtts[1]
    rootSave["Names"] = rootAtts[2]
    rootSave["ParentNames"] = rootAtts[3]

    pickle_out = open("../SaveData/root.pickle","wb")
    pickle.dump(rootSave, pickle_out)
    pickle_out.close()

def saveStem(plant):
    stemSave = {'age':plant.age,'vite':plant.vite,'height':plant.height}
    pickle_out = open("../SaveData/stem.pickle", "wb")
    pickle.dump(stemSave, pickle_out)
    pickle_out.close()


def branchrecursion(branchatts, recursedbranch, parentbranch):
    ###attributes are vites, heights, parentNames
    branchatts[0] += str(recursedbranch.vite) + ","
    branchatts[1] += str(recursedbranch.height) + ","
    branchatts[2] += str(recursedbranch.name) + ","
    branchatts[3] += str(parentbranch) + ","
    for c in recursedbranch.branches:
        branchatts = branchrecursion(branchatts, c, recursedbranch.name)

    return branchatts

def saveBranches(plant):

    branchSave = {'Vitalities':0, 'Heights':0, 'Names':"",'ParentNames':""}
    branchAtts = ["","","",""]
    print(plant.branches)

    for b in plant.branches:
        print(b)
        branchAtts[0] += str(b.vite) + ","
        branchAtts[1] += str(b.height) + ","
        branchAtts[2] += str(b.name) + ","
        branchAtts[3] += str(b.name) + ","
        if len(b.branches)>0:
            for bb in b.branches:

                branchAtts = branchrecursion(branchAtts, bb, b.name)

    branchSave['Vitalities'] = branchAtts[0]
    branchSave['Heights'] = branchAtts[1]
    branchSave['Names'] = branchAtts[2]
    branchSave['ParentNames'] = branchAtts[3]

    pickle_out = open("../SaveData/branch.pickle","wb")
    pickle.dump(branchSave, pickle_out)
    pickle_out.close()

def save(plant):

    saveRoot(plant)  #saves roots and children of roots
    saveStem(plant)
    saveBranches(plant)

    ##save to files


    """
    currentData["roots"] = root
    currentData["rootchildren"] = child
    print(currentData)
    # SaveData.save_json(currentData, "save")
    """