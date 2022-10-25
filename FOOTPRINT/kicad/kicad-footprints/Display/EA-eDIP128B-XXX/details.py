
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Display"
    oIndex = "EA-eDIP128B-XXX"
    hexID = "FZKDIEAEDIP128BXXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'EA-eDIP128B-XXX', 'description': 'LCD-graphical display with LED backlight 128x64 RS-232 I2C or SPI http://www.lcd-module.com/fileadmin/eng/pdf/grafik/edip128-6e.pdf', 'tags': 'LCD-graphical display with LED backlight 128x64 RS-232 I2C or SPI', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Display.3dshapes/EA-eDIP128B-XXX.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Display : EA-eDIP128B-XXX')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

