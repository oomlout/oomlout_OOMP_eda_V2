
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "lsi-computer-systems"
    oIndex = "SOIC16LWB"
    hexID = "FZELSICOMPUTERSYSTEMSSOIC16LWB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('lsi-computer-systems : SOIC16LWB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

