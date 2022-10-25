
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "Osram_BP104-SMD"
    hexID = "FZKOPOSRAMBP14SM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Osram_BP104-SMD', 'description': 'PhotoDiode, plastic SMD DIL, 4.5x4mm, area: 2.2x2.2mm, https://dammedia.osram.info/media/resource/hires/osram-dam-5989350/BP%20104%20FAS_EN.pdf', 'tags': 'PhotoDiode plastic SMD DIL', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Osram_BP104-SMD.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('OptoDevice : Osram_BP104-SMD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

