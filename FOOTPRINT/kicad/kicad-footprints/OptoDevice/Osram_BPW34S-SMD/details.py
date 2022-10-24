
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "Osram_BPW34S-SMD"
    hexID = "FZKOPOSRAMBPW34SSM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Osram_BPW34S-SMD', 'description': 'PhotoDiode, plastic SMD DIL, 4.5x4mm, area: 2.65x2.65mm, https://dammedia.osram.info/media/resource/hires/osram-dam-5488319/BPW%2034%20S_EN.pdf', 'tags': 'PhotoDiode plastic SMD DIL', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Osram_BPW34S-SMD.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('OptoDevice : Osram_BPW34S-SMD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

