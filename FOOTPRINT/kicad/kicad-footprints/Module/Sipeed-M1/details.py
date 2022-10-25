
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Module"
    oIndex = "Sipeed-M1"
    hexID = "FZKMOSIPEEDM1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Sipeed-M1', 'description': 'AI accelerated MCU with optional wifi, https://dl.sipeed.com/MAIX/HDK/Sipeed-M1&M1W/Specifications', 'tags': 'AI Kendryte K210 RISC-V', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Module.3dshapes/Sipeed-M1.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Module : Sipeed-M1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

