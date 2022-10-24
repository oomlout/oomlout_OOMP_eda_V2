
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Mounting_Wuerth"
    oIndex = "Mounting_Wuerth_WA-SMSI-M3_H14mm_9774140360"
    hexID = "FZKMONMONWASMSIM3H1497741436"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mounting_Wuerth_WA-SMSI-M3_H14mm_9774140360', 'description': 'Mounting Hardware, inside through hole M3, height 14, Wuerth electronics 9774140360 (https://katalog.we-online.de/em/datasheet/9774140360.pdf), generated with kicad-footprint-generator', 'tags': 'Mounting M3 9774140360', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Mounting_Wuerth.3dshapes/Mounting_Wuerth_WA-SMSI-M3_H14mm_9774140360.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Mounting_Wuerth : Mounting_Wuerth_WA-SMSI-M3_H14mm_9774140360')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

