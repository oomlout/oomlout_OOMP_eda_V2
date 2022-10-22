
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "MCUU-DI14-84-ATTINY-01-MCAT84SC14"
    hexID = "FZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSMCUUDI1484ATTINY1MCAT84SC14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MCUU-DI14-84-ATTINY-01-MCAT84SC14', 'description': 'hexID: MCAT84SC14; 14-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils)', 'tags': 'THT DIP DIL PDIP 2.54mm 7.62mm 300mil', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-14_W7.62mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('oomlout_OOMP_parts : MCUU-DI14-84-ATTINY-01-MCAT84SC14')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

