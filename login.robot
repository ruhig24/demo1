*** Settings ***
Library  SeleniumLibrary

*** Variables ***


*** Test Cases ***
Login to Facebook
    Open Browser    https://www.facebook.com/   Chrome
    Input text      name=firstname    ruhi
    Input text      name=lastname  shri
    Input text      name=reg_email__    ruhishrivastava27@gmail.com
    Input text      name=reg_passwd__   abcdefgh

#    Select options  id=day  28



*** Keywords ***



