# Port_Scan 
  
A lot of times, a remote host, gets bound to a port and starts running a process on it. This is not only undesirable but also can be dangerous.
I made a set of two scripts, in order to solve the mess. One to check the currently active ports, another one to kill the process running on them.
  
## Setup instructions  
  
There are 2 scripts.  
- [ports_scan.py](./ports_scan.py)  
- [ports_kill.py](./ports_kill.py) 

1. Setup a Virtual Environment.
1. Install dependencies using `pip3 install -r requirements.txt`
1. Go through the comments and the interactive options. 
  
## Output  
  
Sample Outputs -   
  
- ports_scan.py.py  
  
![Result](img/cipher.PNG)  
  
- decipher.py  
>Enter the text to be decrypted: Rfshmjxyjw nx GQZJ  
>Enter the shift key: 5  
>Text before Decryption:  Rfshmjxyjw nx GQZJ  
>Shift Key:  5  
>Decrypted text:  Manchester is BLUE  
  
![Result](img/decipher.PNG)  
  
## Author(s)  
  
Made by [Vybhav Chaturvedi](https://www.linkedin.com/in/vybhav-chaturvedi-0ba82614a/)