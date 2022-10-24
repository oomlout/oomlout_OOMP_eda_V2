
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "WLCSP-4-X1-WLB0909-4_0.89x0.89mm_P0.5mm"
    hexID = "FZKCSPWLCSP4X1WLB99489X89P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WLCSP-4-X1-WLB0909-4_0.89x0.89mm_P0.5mm', 'description': 'X1-WLB0909, 0.89x0.89mm, 4 Ball, 2x2 Layout, 0.5mm Pitch, https://www.diodes.com/assets/Datasheets/AP22913.pdf', 'tags': 'CSP 4 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/WLCSP-4-X1-WLB0909-4_0.89x0.89mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_CSP : WLCSP-4-X1-WLB0909-4_0.89x0.89mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

