<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>472</width>
    <height>501</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QTabWidget" name="mainTabContainer">
      <property name="currentIndex">
       <number>0</number>
      </property>
      <widget class="QWidget" name="gestureTab">
       <attribute name="title">
        <string>Gesture Mode</string>
       </attribute>
       <layout class="QHBoxLayout" name="horizontalLayout">
        <item>
         <widget class="KWebView" name="boneWebV">
          <property name="url">
           <url>
            <string>file:///home/srinivas/Perlich-Bones.html</string>
           </url>
          </property>
         </widget>
        </item>
        <item>
         <spacer name="horizontalSpacer">
          <property name="orientation">
           <enum>Qt::Horizontal</enum>
          </property>
          <property name="sizeHint" stdset="0">
           <size>
            <width>40</width>
            <height>20</height>
           </size>
          </property>
         </spacer>
        </item>
        <item>
         <widget class="QLabel" name="predLabel">
          <property name="minimumSize">
           <size>
            <width>100</width>
            <height>0</height>
           </size>
          </property>
          <property name="text">
           <string>Prediction</string>
          </property>
          <property name="alignment">
           <set>Qt::AlignCenter</set>
          </property>
         </widget>
        </item>
       </layout>
      </widget>
      <widget class="QWidget" name="gameTab">
       <attribute name="title">
        <string>Profile Settings</string>
       </attribute>
      </widget>
      <widget class="QWidget" name="profileTab">
       <attribute name="title">
        <string>Game Mode</string>
       </attribute>
      </widget>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>472</width>
     <height>25</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <customwidgets>
  <customwidget>
   <class>KWebView</class>
   <extends>QWidget</extends>
   <header>kwebview.h</header>
  </customwidget>
 </customwidgets>
 <resources/>
 <connections/>
</ui>
