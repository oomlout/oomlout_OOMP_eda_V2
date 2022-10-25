
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Heatsink"
    oIndex = "Heatsink_125x35x50mm_3xFixationM3"
    hexID = "FZKHH125X35X53XFIXATIONM3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Heatsink_125x35x50mm_3xFixationM3', 'description': 'Heatsink, 125x35x50mm, 3 fixation holes 3.2mm', 'tags': 'heatsink', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Heatsink.3dshapes/Heatsink_125x35x50mm_3xFixationM3.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Heatsink : Heatsink_125x35x50mm_3xFixationM3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

