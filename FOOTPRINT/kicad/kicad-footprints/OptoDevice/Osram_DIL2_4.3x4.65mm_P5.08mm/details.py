
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "Osram_DIL2_4.3x4.65mm_P5.08mm"
    hexID = "FZKOPOSRAMDIL243X465P58"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Osram_DIL2_4.3x4.65mm_P5.08mm', 'description': 'PhotoDiode, plastic DIL, 4.3x4.65mm², RM5.08', 'tags': 'PhotoDiode plastic DIL RM5.08', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Osram_DIL2_4.3x4.65mm_P5.08mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('OptoDevice : Osram_DIL2_4.3x4.65mm_P5.08mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

