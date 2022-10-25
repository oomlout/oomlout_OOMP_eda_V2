
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Display"
    oIndex = "CR2013-MI2120"
    hexID = "FZKDICR213MI212"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CR2013-MI2120', 'description': 'CR2013-MI2120 ILI9341 LCD Breakout http://pan.baidu.com/s/11Y990', 'tags': 'CR2013-MI2120 ILI9341 LCD Breakout', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Display.3dshapes/CR2013-MI2120.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Display : CR2013-MI2120')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

