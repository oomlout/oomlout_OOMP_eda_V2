
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_RND"
    oIndex = "TerminalBlock_RND_205-00281_1x07_P5.00mm_Vertical"
    hexID = "FZKTBRNDTBRND252811X7P5VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_RND_205-00281_1x07_P5.00mm_Vertical', 'description': 'terminal block RND 205-00083, vertical (cable from top), 7 pins, pitch 5mm, size 35x10mm^2, drill diamater 1.3mm, pad diameter 2.5mm, see http://cdn-reichelt.de/documents/datenblatt/C151/RND_205-00276_DB_EN.pdf, script-generated with , script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_RND', 'tags': 'THT terminal block RND 205-00083 vertical pitch 5mm size 35x10mm^2 drill 1.3mm pad 2.5mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_RND.3dshapes/TerminalBlock_RND_205-00281_1x07_P5.00mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_RND : TerminalBlock_RND_205-00281_1x07_P5.00mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

