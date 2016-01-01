#!/usr/bin/env python

import cgi
import cgitb;

DATA_FILE_NAME = ""

cgitb.enable()  # for troubleshooting

print "Content-type: text/html"
print

print """
<html>

<head><title>Dynamic Web Page</title></head>

<body>

  <h3>The last message was:</h3>
"""
with open('/home/r3d/Code/pythonBluetooth/web/data.txt', 'r') as f:
    first_line = f.readline()
    print "<pre>", first_line, "</pre>"
    print """

    <script>
    function refresh() {
             window.location.reload(true);
     }

    setTimeout(refresh, 1000);
</script>

</body>

</html>
"""
