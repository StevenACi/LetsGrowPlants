def branchrecursion(branchatts, recursedbranch, parentbranch):
    ###attributes are vites, heights, parentNames
    branchatts[0] += str(recursedbranch.vite) + ","
    branchatts[1] += str(recursedbranch.height) + ","
    branchatts[2] += str(recursedbranch.name) + ","
    branchatts[3] += str(parentbranch.name) + ","

    for c in recursedbranch.branches:
        branchatts = branchrecursion(branchatts, c, recursedbranch)

    return branchatts

def saveBranches(plant):

    branchSave = {'Vitalities':0, 'Heights':0, 'Names':"",'ParentNames':""}
    branches = plant.branches
    branchAtts = ["","","",""]
    for b in branches:
        branchAtts[0] += str(b.vite) + ","
        branchAtts[1] += str(b.height) + ","
        branchAtts[2] += str(b.name) + ","
        branchAtts[3] += str(b.name) + ","

        branchAtts = branchrecursion(branchAtts, b.branches, b)

    branchSave['Vitalities'] = branchAtts[0]
    branchSave['Heights'] = branchAtts[1]
    branchSave['Names'] = branchAtts[2]
    branchSave['ParentNames'] = branchAtts[3]

    pickle_out = open("../SaveData/branch.pickle","wb")
    pickle.dump(branchSave, pickle_out)
    pickle_out.close()
