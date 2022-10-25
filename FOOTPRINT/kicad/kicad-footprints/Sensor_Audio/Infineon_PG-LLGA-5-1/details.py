
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Audio"
    oIndex = "Infineon_PG-LLGA-5-1"
    hexID = "FZKSENAUDIOINFINEONPGLLGA51"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Infineon_PG-LLGA-5-1', 'description': 'Infineon_PG-LLGA-5-1 StepUp generated footprint, https://www.infineon.com/cms/en/product/packages/PG-LLGA/PG-LLGA-5-1/', 'tags': 'infineon mems microphone', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Audio.3dshapes/Infineon_PG-LLGA-5-1.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Sensor_Audio : Infineon_PG-LLGA-5-1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

