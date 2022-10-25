
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_DCDC"
    oIndex = "Converter_DCDC_XP_POWER-ISU02_SMD"
    hexID = "FZKCONCONXPPOWERISU2SM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_DCDC_XP_POWER-ISU02_SMD', 'description': 'DCDC-Converter, XP POWER, ISU02 Series, 2W Single and Dual Output, 1500VDC Isolation, 19.0x17.0x8.7mm https://www.xppower.com/Portals/0/pdfs/SF_ISU02.pdf', 'tags': 'DCDC SMD XP POWER ISU02', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_DCDC.3dshapes/Converter_DCDC_XP_POWER_ISU02-Series_SMD.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Converter_DCDC : Converter_DCDC_XP_POWER-ISU02_SMD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

