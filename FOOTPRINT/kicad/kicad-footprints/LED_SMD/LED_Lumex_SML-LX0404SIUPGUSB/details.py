
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_Lumex_SML-LX0404SIUPGUSB"
    hexID = "FZKLSMLLUMEXSMLLX44SIUPGU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_Lumex_SML-LX0404SIUPGUSB', 'description': 'Lumex RGB LED, clear, SMD, https://www.lumex.com/spec/SML-LX0404SIUPGUSB.pdf', 'tags': 'LED RGB', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_Lumex_SML-LX0404SIUPGUSB.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('LED_SMD : LED_Lumex_SML-LX0404SIUPGUSB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

