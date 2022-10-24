
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "R_LDR_5.0x4.1mm_P3mm_Vertical"
    hexID = "FZKOPRLDR5X41P3VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_LDR_5.0x4.1mm_P3mm_Vertical', 'description': 'Resistor, LDR 5x4.1mm, see http://cdn-reichelt.de/documents/datenblatt/A500/A90xxxx%23PE.pdf', 'tags': 'Resistor LDR5x4.1mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/R_LDR_5.0x4.1mm_P3mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('OptoDevice : R_LDR_5.0x4.1mm_P3mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

