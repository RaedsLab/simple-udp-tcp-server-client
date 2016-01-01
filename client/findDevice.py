import bluetooth

# client src: https://people.csail.mit.edu/albert/bluez-intro/x232.html

target_name = "nexus"  # TODO : chnage device name to other PC name
target_address = None


def say_Hello(bd_addr):
    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))
    sock.send("hello!!")

    sock.close()


# MAIN
print "Scanning for devices..."
nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    print "- ", bluetooth.lookup_name(bdaddr), " : ", bdaddr

    if target_name == bluetooth.lookup_name(bdaddr):
        target_address = bdaddr
        break

if target_address is not None:
    print "Found target bluetooth device with address ", target_address
    say_Hello(str(target_address))
else:
    print "Could not find target bluetooth device nearby"
