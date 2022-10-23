
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "D_5KPW_P7.62mm_Vertical_AnodeUp"
    hexID = "FZKDD5KPWP762VERTICALANODEUP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_5KPW_P7.62mm_Vertical_AnodeUp', 'description': 'Diode, 5KPW series, Axial, Vertical, pin pitch=7.62mm, , length*diameter=9*8mm^2, , http://www.diodes.com/_files/packages/8686949.gif', 'tags': 'Diode 5KPW series Axial Vertical pin pitch 7.62mm  length 9mm diameter 8mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/D_5KPW_P7.62mm_Vertical_AnodeUp.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : D_5KPW_P7.62mm_Vertical_AnodeUp')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

