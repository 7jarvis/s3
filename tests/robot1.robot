*** Settings ***
Library    SeleniumLibrary
Library    D:/s3/utilites/file_upload_robot.py


*** Variables ***
${BROWSER}    Chrome
${URL}    http://the-internet.herokuapp.com/upload
${FILE_PATH}  C:/path/to/file.txt


*** Test Cases ***
Test File Upload
    Open Browser    ${URL}    ${BROWSER}
    Click On Upload Section    //*[@id='drag-drop-upload']
    Upload File    ${FILE_PATH}
    Page Should Contain    File uploaded successfully
    Close Browser



