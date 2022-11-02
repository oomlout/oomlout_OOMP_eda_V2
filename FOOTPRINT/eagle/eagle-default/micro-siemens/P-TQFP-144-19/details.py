
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "micro-siemens"
    oIndex = "P-TQFP-144-19"
    hexID = "FZEMSIEMENSPTQFP14419"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('micro-siemens : P-TQFP-144-19')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

