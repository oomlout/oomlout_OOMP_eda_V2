
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Display"
    oIndex = "EA_eDIPTFT43-XXX"
    hexID = "FZKDIEAEDIPTFT43XXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'EA_eDIPTFT43-XXX', 'description': 'TFT graphical display 480x272 16-bit colour with LED backlight http://www.lcd-module.com/fileadmin/eng/pdf/grafik/ediptft43-ae.pdf', 'tags': 'TFT graphical display 480x272 16-bit colour with LED backlight', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Display.3dshapes/EA_eDIPTFT43-XXX.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Display : EA_eDIPTFT43-XXX')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

