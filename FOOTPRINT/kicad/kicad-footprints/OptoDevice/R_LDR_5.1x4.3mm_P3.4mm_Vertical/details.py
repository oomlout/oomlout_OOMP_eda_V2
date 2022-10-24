
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "R_LDR_5.1x4.3mm_P3.4mm_Vertical"
    hexID = "FZKOPRLDR51X43P34VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_LDR_5.1x4.3mm_P3.4mm_Vertical', 'description': 'Resistor, LDR 5.1x3.4mm, see http://yourduino.com/docs/Photoresistor-5516-datasheet.pdf', 'tags': 'Resistor LDR5.1x3.4mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/R_LDR_5.1x4.3mm_P3.4mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('OptoDevice : R_LDR_5.1x4.3mm_P3.4mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

