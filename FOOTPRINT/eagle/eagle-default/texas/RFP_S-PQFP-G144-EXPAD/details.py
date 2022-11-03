
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "texas"
    oIndex = "RFP_S-PQFP-G144-EXPAD"
    hexID = "FZETEXASRFPSPQFPG144EXPAD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('texas : RFP_S-PQFP-G144-EXPAD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

