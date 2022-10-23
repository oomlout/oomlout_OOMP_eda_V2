
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Heatsink"
    oIndex = "Heatsink_35x26mm_1xFixation3mm_Fischer-SK486-35"
    hexID = "FZKHH35X261XFIXATION3FISCHERSK48635"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Heatsink_35x26mm_1xFixation3mm_Fischer-SK486-35', 'description': 'Heatsink, 35mm x 26mm, 1x Fixation 3mm, Fischer SK486-35', 'tags': 'heatsink', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Heatsink.3dshapes/Heatsink_35x26mm_1xFixation3mm_Fischer-SK486-35.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Heatsink : Heatsink_35x26mm_1xFixation3mm_Fischer-SK486-35')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

