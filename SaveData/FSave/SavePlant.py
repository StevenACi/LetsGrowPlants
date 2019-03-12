import base64
import pickle
import encodings

def saveRoot(plant):

    rootSave = {'vites': 0, 'lengths': 0, 'numRoots': 0}
    rootchildrenSave = {'vites': "", 'lengths': "",'numChild': 0}

    roots = plant.roots
    children = plant.roots[0].children


    ## all the root stats, count the number of roots
    rootCounter = 0
    rootvites = ""
    rootlengths = ""

    for r in roots:
        rootCounter += 1
        rootvites += str(r.vite) + ","
        rootlengths += str(r.length) + ","

    rootSave['vite'] = rootvites
    rootSave['length'] = rootlengths

    ## encode all the child stats to base64 , count the number of children..
    childCounter = 0
    childvites = ""
    childlengths = ""

    for c in children:
        childCounter += 1
        childvites += str(c.vite) + ","
        childlengths += str(c.length) + ","

    rootchildrenSave["vites"] = childvites
    rootchildrenSave["lengths"] = childlengths

    ##save number of children
    rootchildrenSave['numChild'] = childCounter
    rootSave['numRoots'] = rootCounter

    rootSave = rootSave
    pickle_out = open("../SaveData/root.pickle","wb")
    pickle.dump(rootSave, pickle_out)
    pickle_out.close()

    pickle_out = open("../SaveData/rootchildren.pickle", "wb")
    pickle.dump(rootchildrenSave, pickle_out)
    pickle_out.close()

def saveStem(plant):
    stemSave = {'age':plant.age,'vite':plant.vite,'height':plant.height}
    pickle_out = open("../SaveData/stem.pickle", "wb")
    pickle.dump(stemSave, pickle_out)
    pickle_out.close()

def saveBranches(plant):

    branchSave = {'vites':0, 'heights':0, 'numBranch':0}
    branchchildrenSave = {'vites':0, 'heights':0, 'numChildren':0}
    branches = plant.branches

    ## all the branch stats, count the number of branches
    branchCounter = 0
    branchVites = ""
    branchHeights = ""
    childrenVites = ""
    childrenHeights = ""
    numChildren = ""

    for b in branches:

        branchCounter += 1
        branchVites += str(b.vite) + ","
        branchHeights += str(b.height) + ","

        childrenCounter = 0

        for bIndex, c in enumerate(b.branches):
            childrenVites += str(c.vite) + ","
            childrenHeights += str(c.height) + ","
            childrenCounter += 1

        numChildren += str(childrenCounter) + ","

    branchSave['vites'] = branchVites
    branchSave['heights'] = branchHeights
    branchSave['numBranch'] = branchCounter

    branchchildrenSave['vites'] = childrenVites
    branchchildrenSave['heights'] = childrenHeights
    branchchildrenSave['numChildren'] = numChildren

    pickle_out = open("../SaveData/branch.pickle","wb")
    pickle.dump(branchSave, pickle_out)
    pickle_out.close()

    pickle_out = open("../SaveData/branchchildren.pickle", "wb")
    pickle.dump(branchchildrenSave, pickle_out)
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