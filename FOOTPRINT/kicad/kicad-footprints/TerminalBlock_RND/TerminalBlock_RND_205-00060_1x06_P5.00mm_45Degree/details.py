
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_RND"
    oIndex = "TerminalBlock_RND_205-00060_1x06_P5.00mm_45Degree"
    hexID = "FZKTBRNDTBRND2561X6P545DEGREE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_RND_205-00060_1x06_P5.00mm_45Degree', 'description': 'terminal block RND 205-00060, 45Degree (cable under 45degree), 6 pins, pitch 5mm, size 30x12.6mm^2, drill diamater 1.3mm, pad diameter 2.5mm, see http://cdn-reichelt.de/documents/datenblatt/C151/RND_205-00056_DB_EN.pdf, script-generated with , script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_RND', 'tags': 'THT terminal block RND 205-00060 45Degree pitch 5mm size 30x12.6mm^2 drill 1.3mm pad 2.5mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_RND.3dshapes/TerminalBlock_RND_205-00060_1x06_P5.00mm_45Degree.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_RND : TerminalBlock_RND_205-00060_1x06_P5.00mm_45Degree')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

