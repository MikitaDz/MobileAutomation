# MobileAutomation
Mobile app automation project for Salut app

## How to run app tests on your local device (Linux)

## Before first run
1. Install Android SDK, Python, Appium, Appium python library, JDK, etc
2. Set environment variables which pointed to installed Android SDK 
export ANDROID_HOME=/home/mikitadz/Android/Sdk
export ANDROID_SDK_ROOT=/home/mikitadz/Android/Sdk
export PATH=${PATH}:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

## Run
1. Run Android studio by running `./studio.sh` from Android studio bin folder
2. Run Appium `appium -a 127.0.0.1` . Port is 4723 by default
3. From /Sdk/platform-tools run `adb devices` in order to look on the list of devices connected. Device should be connected via usb and Developer mode should be on
4. (Optional) Run `./uiautomatorviewer` from /Sdk/tools/bin in order to run uiautomatorviewer 
5. Set inside test config device id from step 3
6. Run tests from file or from IDE ()
