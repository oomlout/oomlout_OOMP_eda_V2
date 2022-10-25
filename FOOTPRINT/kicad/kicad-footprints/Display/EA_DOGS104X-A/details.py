
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Display"
    oIndex = "EA_DOGS104X-A"
    hexID = "FZKDIEADOGS14XA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'EA_DOGS104X-A', 'description': 'LCD 4x10 character 3.3V VDD I2C or SPI http://www.lcd-module.com/fileadmin/eng/pdf/doma/dogs104e.pdf', 'tags': 'LCD 4x10 character 3.3V VDD I2C or SPI', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Display.3dshapes/EA_DOGS104X-A.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Display : EA_DOGS104X-A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

