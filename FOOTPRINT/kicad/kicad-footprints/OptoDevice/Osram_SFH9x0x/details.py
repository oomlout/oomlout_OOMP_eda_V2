
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "Osram_SFH9x0x"
    hexID = "FZKOPOSRAMSFH9XX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Osram_SFH9x0x', 'description': 'package for Osram SFH9x0x series of reflective photo interrupters/couplers, see http://www.osram-os.com/Graphics/XPic6/00200860_0.pdf', 'tags': 'reflective photo interrupter SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Osram_SFH9x0x.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('OptoDevice : Osram_SFH9x0x')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

