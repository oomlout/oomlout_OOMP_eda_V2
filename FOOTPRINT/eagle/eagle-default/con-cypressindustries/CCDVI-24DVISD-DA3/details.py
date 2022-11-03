
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "con-cypressindustries"
    oIndex = "CCDVI-24DVISD-DA3"
    hexID = "FZECONCYPRESSINDUSTRIESCCDVI24DVISDDA3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('con-cypressindustries : CCDVI-24DVISD-DA3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

