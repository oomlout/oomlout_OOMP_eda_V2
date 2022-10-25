
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Display"
    oIndex = "EA_eDIP320X-XXX"
    hexID = "FZKDIEAEDIP32XXXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'EA_eDIP320X-XXX', 'description': 'LCD display 320x340 RS-232 I2C or SPI http://www.lcd-module.com/fileadmin/eng/pdf/grafik/edip320-8e.pdf', 'tags': 'LCD display 320x340 RS-232 I2C or SPI', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Display.3dshapes/EA_eDIP320X-XXX.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Display : EA_eDIP320X-XXX')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

