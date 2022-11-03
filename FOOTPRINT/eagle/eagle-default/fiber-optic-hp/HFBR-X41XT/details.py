
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "fiber-optic-hp"
    oIndex = "HFBR-X41XT"
    hexID = "FZEFIBEROPTICHPHFBRX41XT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('fiber-optic-hp : HFBR-X41XT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

