
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Module"
    oIndex = "WEMOS_D1_mini_light"
    hexID = "FZKMOWEMOSD1MLIGHT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WEMOS_D1_mini_light', 'description': '16-pin module, column spacing 22.86 mm (900 mils), https://wiki.wemos.cc/products:d1:d1_mini, https://c1.staticflickr.com/1/734/31400410271_f278b087db_z.jpg', 'tags': 'ESP8266 WiFi microcontroller', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PinSocket_2.54mm.3dshapes/PinSocket_1x08_P2.54mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Module : WEMOS_D1_mini_light')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

