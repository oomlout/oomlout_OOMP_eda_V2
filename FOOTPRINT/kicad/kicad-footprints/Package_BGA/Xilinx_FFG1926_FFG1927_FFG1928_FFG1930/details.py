
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Xilinx_FFG1926_FFG1927_FFG1928_FFG1930"
    hexID = "FZKBGAXILINXFFG1926FFG1927FFG1928FFG193"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Xilinx_FFG1926_FFG1927_FFG1928_FFG1930', 'description': 'Virtex-7 BGA, 44x44 grid, 45x45mm package, 1mm pitch; https://www.xilinx.com/support/documentation/user_guides/ug475_7Series_Pkg_Pinout.pdf#page=303, NSMD pad definition Appendix A', 'tags': 'BGA 1924 1 FF1926 FFG1926 FF1927 FFG1927 FFV1927 FF1928 FFG1928 FF1930 FFG1930', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Xilinx_FFG1926_FFG1927_FFG1928_FFG1930.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : Xilinx_FFG1926_FFG1927_FFG1928_FFG1930')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

