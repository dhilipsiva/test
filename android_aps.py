#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: android_aps.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-08-22
"""

apps = "com.android.providers.telephony,com.motorola.pgmsystem2,eu.chainfire.adbd,com.motorola.ccc.sso.app,com.motorola.demomode,com.google.android.backuptransport,com.motorola.emaraphoneextns,com.android.exchange,com.google.android.marvin.talkback,com.motorola.ccc.main,com.android.phone,com.motorola.camera,com.motorola.bodyguard,com.motorola.bach.modemstats,in.swiggy.android,com.android.proxyhandler,com.android.providers.downloads,com.android.providers.media,com.android.inputdevices,com.android.keychain,com.quickoffice.android,com.motorola.aonlt.env,com.google.android.gms,com.motorola.motosignature.app,com.android.providers.settings,com.android.wallpaper.livepicker,com.motorola.ccc.notification,com.android.certinstaller,com.google.android.apps.uploader,com.qualcomm.services.location,com.motorola.wappushsi,com.google.android.feedback,com.motorola.aonlt,com.android.mms,com.google.android.onetimeinitializer,com.motorola.fmplayer,com.android.browser.provider,com.motorola.msimsettings,com.motorola.programmenu,com.android.providers.calendar,com.google.android.music,com.motorola.ccc.cce,com.google.android.inputmethod.pinyin,org.codeaurora.bluetooth,com.android.contacts,com.android.sharedstoragebackup,com.android.vpndialogs,com.motorola.contextual.fw,com.android.shell,com.google.android.inputmethod.latin,com.google.android.googlequicksearchbox,com.google.android.syncadapters.calendar,com.google.android.apps.docs,com.android.location.fused,com.android.stk,com.motorola.bug2go,com.android.documentsui,com.motorola.android.providers.settings,com.motorola.mesh,com.android.cellbroadcastreceiver,com.motorola.ccc.devicemanagement,com.android.calendar,com.google.android.partnersetup,com.google.android.talk,com.qualcomm.atfwd,com.motorola.android.settings.diag_mdlog,eu.chainfire.supersu,com.google.android.youtube,com.google.android.setupwizard,com.android.pacprocessor,com.android.providers.userdictionary,com.google.android.apps.maps,com.google.android.apps.books,com.google.android.gsf,com.android.deskclock,com.qualcomm.timeservice,com.google.android.videos,com.google.android.street,com.qualcomm.qualcommsettings,com.android.settings,com.motorola.setup,com.motorola.contextual.smartrules2,com.motorola.fmrecording,com.motorola.migrate,com.android.htmlviewer,com.motorola.audioeffects,com.google.android.configupdater,com.google.android.apps.cloudprint,com.motorola.android.providers.userpreferredsim,com.motorola.android.provisioning,com.motorola.motocare.internal,com.motorola.android.nativedropboxagent,com.android.packageinstaller,com.android.bluetooth,com.android.launcher,com.qualcomm.qcom_qmi,com.android.dreams.phototable,com.motorola.deviceauthenticator,com.motorola.context,com.motorola.motocit,com.android.email,com.android.backupconfirm,android,com.motorola.motocare,com.motorola.ccc.ota,com.android.chrome,com.motorola.android.fmradio,com.google.android.apps.magazines,com.hp.android.printservice,com.qualcomm.location,com.lmi.motorola.rescuesecurity,com.motorola.moodles,com.motorola.android.dm.service,com.android.systemui,com.qualcomm.interfacepermissions,com.android.vending,com.android.dialer,com.google.android.syncadapters.contacts,com.motorola.contacts.preloadcontacts,com.android.providers.partnerbookmarks,com.android.providers.contacts,com.motorola.authentication,com.android.soundrecorder,com.motorola.genie,com.google.android.tts,com.android.defcontainer,com.android.keyguard,com.android.wallpapercropper,com.android.providers.downloads.ui,com.google.android.play.games,com.motorola.MotGallery2,com.google.android.apps.plus,com.google.android.gm,com.qualcomm.qcrilmsgtunnel,com.motorola.ccc.checkin,com.android.externalstorage,com.motorola.so,com.android.dreams.basic,com.motorola.motgeofencesvc,com.google.android.gsf.login,com.android.printspooler,com.android.calculator2"  # NOQA

apps = apps.split(',')

builtin_namepaces = [
    'com.google', 'com.android', 'com.motorola', 'com.qualcomm', 'android',
    'eu.chainfire', 'com.quickoffice.android', 'org.codeaurora.bluetooth',
    'com.lmi.motorola.rescuesecurity', 'com.hp.android.printservice']
for app in apps:
    for builtin_namepace in builtin_namepaces:
        if app.startswith(builtin_namepace):
            break
    else:
        print(app)
