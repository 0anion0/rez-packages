# -*- coding: utf-8 -*-

# Copyright (C) Fix Studio, and/or its licensors.
# All rights reserved.
#
# The coded instructions, statements, computer programs, and/or related
# material (collectively the "Data") in these files contain unpublished
# information proprietary to Fix Studio and/or its licensors.
#
# The Data may not be disclosed or distributed to third parties or be
# copied or duplicated, in whole or in part, without the prior written
# consent of Fix Studio.


from rez.utils.lint_helper import env, building


name = "maya"

version = "2016.0.6"  # from mayapy -c "import maya.standalone; maya.standalone.initialize(name='python'); print maya.cmds.about(api=True); maya.standalone.uninitialize()"

authors = ["Autodesk"]

description = "Autodesk maya 2016 Service Pack 6"

build_requires = []

variants = [["platform-linux", "arch-x86_64"]]

tools = ["maya", "mayapy"]

uuid = "repository.maya"

has_plugins = True


def commands():

    env.MAYA_LOCATION.set("{root}/maya")
    env.MAYA_VERSION = "2016"

    env.AUTODESK_ADLM_THINCLIENT_ENV.set("{root}/AdlmThinClientCustomEnv.xml")
    env.MAYA_COLOR_MANAGEMENT_POLICY_LOCK = 1
    env.MAYA_COLOR_MANAGEMENT_POLICY_FILE = "{root}/MayaNoColorManagement.xml"
    env.MAYA_VP2_USE_GPU_MAX_TARGET_SIZE = 1

    env.PATH.prepend("{root}/maya/bin")
