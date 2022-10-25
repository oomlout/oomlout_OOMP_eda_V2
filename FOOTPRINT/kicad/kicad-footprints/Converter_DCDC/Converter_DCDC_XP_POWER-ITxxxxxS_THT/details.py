
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_DCDC"
    oIndex = "Converter_DCDC_XP_POWER-ITxxxxxS_THT"
    hexID = "FZKCONCONXPPOWERITXXXXXSTHT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_DCDC_XP_POWER-ITxxxxxS_THT', 'description': 'XP_POWER  ITxxxxxS, SIP, (https://www.xppower.com/portals/0/pdfs/SF_ITX.pdf https://www.xppower.com/portals/0/pdfs/SF_ITQ.pdf), generated with kicad-footprint-generator', 'tags': 'XP_POWER  ITxxxxxS SIP DCDC-Converter', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_DCDC.3dshapes/Converter_DCDC_XP_POWER-ITxxxxxS_THT.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Converter_DCDC : Converter_DCDC_XP_POWER-ITxxxxxS_THT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

