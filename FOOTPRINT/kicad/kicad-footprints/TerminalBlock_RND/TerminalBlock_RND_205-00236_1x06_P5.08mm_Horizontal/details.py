
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_RND"
    oIndex = "TerminalBlock_RND_205-00236_1x06_P5.08mm_Horizontal"
    hexID = "FZKTBRNDTBRND252361X6P58HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_RND_205-00236_1x06_P5.08mm_Horizontal', 'description': 'terminal block RND 205-00236, 6 pins, pitch 5.08mm, size 30.5x8.45mm^2, drill diamater 1.1mm, pad diameter 2.1mm, see http://cdn-reichelt.de/documents/datenblatt/C151/RND_205-00232_DB_EN.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_RND', 'tags': 'THT terminal block RND 205-00236 pitch 5.08mm size 30.5x8.45mm^2 drill 1.1mm pad 2.1mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_RND.3dshapes/TerminalBlock_RND_205-00236_1x06_P5.08mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_RND : TerminalBlock_RND_205-00236_1x06_P5.08mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

