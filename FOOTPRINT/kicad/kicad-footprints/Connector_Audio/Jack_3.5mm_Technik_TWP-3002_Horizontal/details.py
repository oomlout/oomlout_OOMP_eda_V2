
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_3.5mm_Technik_TWP-3002_Horizontal"
    hexID = "FZKCNAUDIOJ35TECHNIKTWP32HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_3.5mm_Technik_TWP-3002_Horizontal', 'description': '3.5mm Horizontal Waterproof Stereo Headphones Jack, https://www.technik.com.hk/images/pdf_product/WP3002-PA66-A.pdf', 'tags': 'audio jack stereo horizontal waterproof', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_3.5mm_Technik_TWP-3002_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Audio : Jack_3.5mm_Technik_TWP-3002_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

