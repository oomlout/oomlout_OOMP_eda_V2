
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "D_5KP_P7.62mm_Vertical_KathodeUp"
    hexID = "FZKDD5KPP762VERTICALKATHODEUP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_5KP_P7.62mm_Vertical_KathodeUp', 'description': 'Diode, 5KP series, Axial, Vertical, pin pitch=7.62mm, , length*diameter=7.62*9.53mm^2, , http://www.diodes.com/_files/packages/8686949.gif', 'tags': 'Diode 5KP series Axial Vertical pin pitch 7.62mm  length 7.62mm diameter 9.53mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/D_5KP_P7.62mm_Vertical_KathodeUp.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : D_5KP_P7.62mm_Vertical_KathodeUp')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

