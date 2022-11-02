
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "johanson-technology"
    oIndex = "2450BM15A0002"
    hexID = "FZEJOHANSONTECHNOLOGY245BM15A2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('johanson-technology : 2450BM15A0002')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

