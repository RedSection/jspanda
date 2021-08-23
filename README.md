# JSPanda

[![Panda](panda.gif)](https://www.youtube.com/watch?v=6At3qjurhOs)

JSpanda is client-side prototype pollution vulnerability scanner. It has two key features, scanning vulnerability the supplied URLs and analyzing the JavaScript libraries' source code. 

However, JSpanda cannot detect advanced prototype pollution vulnerabilities.

## **How JSPanda works?**

- Uses multiple payloads for prototype pollution vulnerability.
- Gathers all the links in the targets for scanning and add payloads to JSpanda-obtained URLs, navigates to each URL with headless Chromedriver.
- Scans all words in the source code of potentially vulnerable JavaScript library and it creates a simple JS PoC by finding the script gadget, helping you analyze the code manually.

## **Requirements**

- Download latest version of Google Chrome and Chromedriver
- Selenium

## **Usage**

Scan: python3.7 jspanda.py

- Add URLs to url.txt file, *for instance : example.com*

Basic Source Code Analysis : python3.7 analyze.py

- Add a JavaScript library's source code to analyze.js
- Generate PoC code using analyze.py
- Execute PoC code on Chrome's console. It pollutes all the words collected from the source code and show it on the screen. So it may generate false positive results. These outputs provide additional information to researchers, do not automate everything.

### Demonstration

[![asciicast](https://asciinema.org/a/BOazgAVyW6yHqhUE3fEYcCiML.svg)](https://asciinema.org/a/BOazgAVyW6yHqhUE3fEYcCiML)

### Source code analysis - Screenshot

![Untitled](https://github.com/RedSection/jspanda/blob/main/pollute.png?raw=true)

**Supporting Materials :** 

[https://twitter.com/har1sec/status/1314469278322655233](https://twitter.com/har1sec/status/1314469278322655233)


[https://github.com/BlackFan/client-side-prototype-pollution](https://github.com/BlackFan/client-side-prototype-pollution)


[https://github.com/ThePacketBender/notes/blob/01c0b834f6e3ee4d934b087b2d92c9e484dc2a50/web/prototype_pollution.txt](https://github.com/ThePacketBender/notes/blob/01c0b834f6e3ee4d934b087b2d92c9e484dc2a50/web/prototype_pollution.txt)

[https://habr.com/ru/company/huawei/blog/547178/](https://habr.com/ru/company/huawei/blog/547178/)

[https://infosecwriteups.com/javascript-prototype-pollution-practice-of-finding-and-exploitation-f97284333b2](https://infosecwriteups.com/javascript-prototype-pollution-practice-of-finding-and-exploitation-f97284333b2)

[https://github.com/securitum/research/tree/master/r2020_prototype-pollution](https://github.com/securitum/research/tree/master/r2020_prototype-pollution)


[Learn Prototype Pollution in Series - Part 2](https://attacker-codeninja.github.io/2021-07-05-Learn-Prototype-Pollution-Part-2/)

[dwisiswant0/ppfuzz](https://github.com/dwisiswant0/ppfuzz)

[GitHub - raverrr/plution: Prototype pollution scanner using headless chrome](https://github.com/raverrr/plution)

[JavaScript Prototype Poisoning Vulnerabilities in the Wild](https://medium.com/intrinsic-blog/javascript-prototype-poisoning-vulnerabilities-in-the-wild-7bc15347c96)

[The Complete Guide to Prototype Pollution Vulnerabilities](https://www.whitesourcesoftware.com/resources/blog/prototype-pollution-vulnerabilities/)
