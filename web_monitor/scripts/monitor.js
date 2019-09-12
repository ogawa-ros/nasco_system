var ros = new ROSLIB.Ros({url : "ws://" + "172.20.0.237" + ":9000"});

ros.on("connection", function() {console.log("websocket: connected"); });
ros.on("error", function(error) {console.log("websocket error; ", error); });
ros.on("close", function() {console.log("websocket: closed");});

document.write("<script type='text/javascript' src='./monitor_lakeshore218.js'<>\/script>");
