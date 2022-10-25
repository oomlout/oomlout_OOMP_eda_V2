
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor"
    oIndex = "Winson_GM-402B_5x5mm_P1.27mm"
    hexID = "FZKSENWINSONGM42B5X5P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Winson_GM-402B_5x5mm_P1.27mm', 'description': 'Winson GM-402B, 8 Pin (https://www.winsen-sensor.com/d/files/me2/mems--gm-402b--manual-v1_1.pdf)', 'tags': 'Winson', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor.3dshapes/Winson_GM-402B_5x5mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Sensor : Winson_GM-402B_5x5mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

