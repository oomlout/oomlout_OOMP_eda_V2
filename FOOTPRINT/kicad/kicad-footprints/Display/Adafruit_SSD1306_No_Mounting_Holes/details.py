
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Display"
    oIndex = "Adafruit_SSD1306_No_Mounting_Holes"
    hexID = "FZKDIADASSD136NOMOUNTINGH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Adafruit_SSD1306_No_Mounting_Holes', 'description': 'Adafruit SSD1306 OLED 1.3 inch 128x64 I2C & SPI https://learn.adafruit.com/monochrome-oled-breakouts/downloads', 'tags': 'Adafruit SSD1306 OLED 1.3 inch 128x64 I2C & SPI ', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Display.3dshapes/Adafruit_SSD1306.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Display : Adafruit_SSD1306_No_Mounting_Holes')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

