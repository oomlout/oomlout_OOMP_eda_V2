
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Display"
    oIndex = "EA_eDIP160-XXX"
    hexID = "FZKDIEAEDIP16XXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'EA_eDIP160-XXX', 'description': 'LCD-graphical display with LED backlight 160x104 RS-232 I2C or SPI http://www.lcd-module.com/fileadmin/eng/pdf/grafik/edip160-7e.pdf', 'tags': 'LCD-graphical display with LED backlight 160x104 RS-232 I2C or SPI', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Display.3dshapes/EA_eDIP160-XXX.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Display : EA_eDIP160-XXX')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

