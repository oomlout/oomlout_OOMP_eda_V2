
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "Osram_SFH2430"
    hexID = "FZKOPOSRAMSFH243"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Osram_SFH2430', 'description': 'PhotoDiode, plastic SMD DIL, 4.5x4mm, area: 2.65x2.65mm, https://dammedia.osram.info/media/resource/hires/osram-dam-5467144/SFH%202430_EN.pdf', 'tags': 'PhotoDiode plastic SMD DIL', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Osram_SFH2430.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('OptoDevice : Osram_SFH2430')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

