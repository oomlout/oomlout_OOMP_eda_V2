
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "R_LDR_D20mm_P17.5mm_Vertical"
    hexID = "FZKOPRLDRD2P175VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_LDR_D20mm_P17.5mm_Vertical', 'description': 'Resistor, LDR 20mm diameter, pin pitch 17.5mm, see http://yourduino.com/docs/Photoresistor-5516-datasheet.pdf', 'tags': 'Resistor LDR', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/R_LDR_D20mm_P17.5mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('OptoDevice : R_LDR_D20mm_P17.5mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

