
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "D_DO-201_P3.81mm_Vertical_KathodeUp"
    hexID = "FZKDDDO21P381VERTICALKATHODEUP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_DO-201_P3.81mm_Vertical_KathodeUp', 'description': 'Diode, DO-201 series, Axial, Vertical, pin pitch=3.81mm, , length*diameter=9.53*5.21mm^2, , http://www.diodes.com/_files/packages/DO-201.pdf', 'tags': 'Diode DO-201 series Axial Vertical pin pitch 3.81mm  length 9.53mm diameter 5.21mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/D_DO-201_P3.81mm_Vertical_KathodeUp.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : D_DO-201_P3.81mm_Vertical_KathodeUp')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

