// ==UserScript==
// @name         Decrypt_Blowfish_ECB
// @version      4.5
// @description  test of interoperability between python and javascript for Blowfish ECB algorithm
// @author       Daniela Moreno
// @require      https://gist.githubusercontent.com/aylarov/08eff1bfccb7e0e87a2fef0df766f01c/raw/9c6d8ed3dbb6bafc76fb3c5a6bc5722a41f1f497/ECB_Blowfish.js
// @downloadURL   https://github.com/dani0f/Tarea3-cripto/blob/main/Javascript/Decrypt_Blowfish_ECB.user.js
// @updateURL   https://github.com/dani0f/Tarea3-cripto/blob/main/Javascript/Decrypt_Blowfish_ECB.user.js
// @match        *://*/*
// @grant        none
// ==/UserScript==
var key = 'llave'
var div= document.getElementById("msg_encrypted")
var msgEncrypted=document.getElementsByClassName("algorithm text-danger")[0].id
alert(msgEncrypted)
var result = blowfish.decrypt(msgEncrypted, key, {cipherMode: 0, outputType: 0});
alert(result)
div.innerHTML = result






