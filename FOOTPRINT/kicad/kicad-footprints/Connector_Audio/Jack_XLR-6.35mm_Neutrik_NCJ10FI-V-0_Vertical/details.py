
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_XLR-6.35mm_Neutrik_NCJ10FI-V-0_Vertical"
    hexID = "FZKCNAUDIOJXLR635NEUTRIKNCJ1FIVVERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_XLR-6.35mm_Neutrik_NCJ10FI-V-0_Vertical', 'description': 'Combo I series, 3 pole XLR female receptacle with 6.35mm (1/4in) switching stereo jack and switching ground contact, vertical PCB mount, https://www.neutrik.com/en/product/ncj10fi-v-0', 'tags': 'neutrik jack combo i', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_XLR-6.35mm_Neutrik_NCJ10FI-V-0_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Audio : Jack_XLR-6.35mm_Neutrik_NCJ10FI-V-0_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

