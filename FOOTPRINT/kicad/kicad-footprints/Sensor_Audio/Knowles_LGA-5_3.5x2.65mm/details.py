
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Audio"
    oIndex = "Knowles_LGA-5_3.5x2.65mm"
    hexID = "FZKSENAUDIOKNOWLESLGA535X265"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Knowles_LGA-5_3.5x2.65mm', 'description': 'https://www.knowles.com/docs/default-source/model-downloads/sph0641lu4h-1-revb.pdf', 'tags': 'MEMS Microphone LGA', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Audio.3dshapes/Knowles_LGA-5_3.5x2.65mm.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Sensor_Audio : Knowles_LGA-5_3.5x2.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

