<h1>CodeHS</h1>
<h3>Lets you encrypt messages in a CodeHS python turtle sandbox. CodeHS doesn't allow you to use bytes(), import base64, .encode() or anything that could've made this easier so thats annoying. This can let you encrypt a message and decrypt it using a <a href="https://en.wikipedia.org/wiki/XOR_cipher" target="_blank">XOR cipher</a> with a key.</h3>

<h1>Usage</h1>
<ul>
  <li>Must be ran in a <a href="https://codehs.com/" target="_blank">CodeHS</a> sandbox</li>
  <li>Once logged into Codehs, click "Sandbox" in the navigation bar</li>
  <li>Click "Create Program" then select "Python (turtle)" and create program</li>
  <li>Copy and paste the code from the main.py file and paste it into your sandbox</li>
  <li>Run the program.</li>
</ul>

<h1>Example Usage</h1>
```
[Jicrypt]: Encrypt or decrypt? (1 or 2): 1
[Jicrypt]: Enter the text you want to encrypt: my secret message
[Jicrypt]: Enter a key (as an integer): 123
Enable bloat? This can enhance security by obsecuring the length of your message. (Y or N): y
Encrypted message:ùí´çñ÷æñà´ùñççõóñ~oAaET(P]D5']\r\x0bXqnQK#pJN}8RAFS>
[Jicrypt]: Generated bloat (Remember this): 17
[Jicrypt]: Run again (1) or exit (2): 1


[Jicrypt]: Encrypt or decrypt? (1 or 2): 2
Enter encrypted text: ùí´çñ÷æñà´ùñççõóñ~oAaET(P]D5']\r\x0bXqnQK#pJN}8RAFS>
Enter the key to decrypt the message: 123
Bloat (0 if none): 17
Decrypted message: my secret message
```
