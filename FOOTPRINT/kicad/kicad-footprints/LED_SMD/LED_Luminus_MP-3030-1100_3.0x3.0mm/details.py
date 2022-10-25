
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_Luminus_MP-3030-1100_3.0x3.0mm"
    hexID = "FZKLSMLLUMINUSMP33113X3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_Luminus_MP-3030-1100_3.0x3.0mm', 'description': 'Mid Power LED, Luminus MP-3030-1100, 3.0x3.0mm, 816mW, https://download.luminus.com/datasheets/Luminus_MP3030_1100_Datasheet.pdf', 'tags': 'LED Luminus MP-3030-1100', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_Luminus_MP-3030-1100_3.0x3.0mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('LED_SMD : LED_Luminus_MP-3030-1100_3.0x3.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

