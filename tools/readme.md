# Config
en/disable USB HID

Rpi4 USB_HID_permission
- ```sudo nano /etc/udev/rules.d/99-com.rules```
- insert/remove this line into 99-com.rules:

  ```
  SUBSYSTEMS=="usb", DRIVERS=="usbhid", ACTION=="add", ATTR{authorized}="0"
  ```

- save the file and update the rule:

  ```
  sudo udevadm trigger
  ```

- try to plugging any USB HID device, it will not be registered!
- note: don't unplug your current kb cable/dongle if you are not connected via ssh!

Autorun: ```sudo nano ~/.bashrc```, insert:
- ```python3 /home/rpi/ - path - /server.py &```
- ```echo Server has been started!```

Transfer file:
- ```scp rpi@192.168.1.xx:/home/rpi/-path-/-fname-.py C:/Users/-user-/Downloads```
- ```scp C:/Users/-user-/Downloads rpi@192.168.1.xx:/home/rpi/-path-/-fname-.py```
