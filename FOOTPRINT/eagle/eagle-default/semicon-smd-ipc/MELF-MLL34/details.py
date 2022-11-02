
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "semicon-smd-ipc"
    oIndex = "MELF-MLL34"
    hexID = "FZESEMICONSMIPCMELFMLL34"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('semicon-smd-ipc : MELF-MLL34')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

