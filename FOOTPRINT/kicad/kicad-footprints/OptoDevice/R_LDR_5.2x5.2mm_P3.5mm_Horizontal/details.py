
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "R_LDR_5.2x5.2mm_P3.5mm_Horizontal"
    hexID = "FZKOPRLDR52X52P35HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_LDR_5.2x5.2mm_P3.5mm_Horizontal', 'description': 'Resistor, LDR 5.2x5.2, upright, see http://cdn-reichelt.de/documents/datenblatt/A500/M996011A.pdf', 'tags': 'Resistor LDR5.2x5.2 ', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/R_LDR_5.2x5.2mm_P3.5mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('OptoDevice : R_LDR_5.2x5.2mm_P3.5mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

