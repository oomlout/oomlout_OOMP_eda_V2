
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Display_7Segment"
    oIndex = "SA15-11xxx"
    hexID = "FZKDI7SSA1511XXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SA15-11xxx', 'description': 'http://www.kingbrightusa.com/images/catalog/SPEC/SA15-11SRWA.pdf', 'tags': 'SA15-11xxx single digit 7 segment display 38.1mm 1.5inch', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Display_7Segment.3dshapes/SA15-11xxx.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Display_7Segment : SA15-11xxx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

