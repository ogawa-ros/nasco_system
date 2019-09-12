var ros = new ROSLIB.Ros({url : "ws://" + IP_rxobs + ":9000"});

ros.on("connection", function() {console.log("websocket: connected"); });
ros.on("error", function(error) {console.log("websocket error; ", error); });
ros.on("close", function() {console.log("websocket: closed");});

var lakeshore_ch1 = new ROSLIB.Topic({
    ros : ros,
    name : "/lakeshore_ch1",
    messageType : "std_msgs/Float64"
});

var lakeshore_ch2 = new ROSLIB.Topic({
    ros : ros,
    name : "/lakeshore_ch2",
    messageType : "std_msgs/Float64"
});

var lakeshore_ch3 = new ROSLIB.Topic({
    ros : ros,
    name : "/lakeshore_ch3",
    messageType : "std_msgs/Float64"
});

var lakeshore_ch4 = new ROSLIB.Topic({
    ros : ros,
    name : "/lakeshore_ch4",
    messageType : "std_msgs/Float64"
});

var lakeshore_ch5 = new ROSLIB.Topic({
    ros : ros,
    name : "/lakeshore_ch5",
    messageType : "std_msgs/Float64"
});

var lakeshore_ch6 = new ROSLIB.Topic({
    ros : ros,
    name : "/lakeshore_ch6",
    messageType : "std_msgs/Float64"
});

var lakeshore_ch7 = new ROSLIB.Topic({
    ros : ros,
    name : "/lakeshore_ch7",
    messageType : "std_msgs/Float64"
});

var lakeshore_ch8 = new ROSLIB.Topic({
    ros : ros,
    name : "/lakeshore_ch8",
    messageType : "std_msgs/Float64"
});


lakeshore_ch1.subscribe(function(message) {
    document.getElementById("lakeshore_ch1").innerHTML = (message.data);
});

lakeshore_ch2.subscribe(function(message) {
    document.getElementById("lakeshore_ch2").innerHTML = (message.data);
});

lakeshore_ch3.subscribe(function(message) {
    document.getElementById("lakeshore_ch3").innerHTML = (message.data);
});

lakeshore_ch4.subscribe(function(message) {
    document.getElementById("lakeshore_ch4").innerHTML = (message.data);
});

lakeshore_ch5.subscribe(function(message) {
    document.getElementById("lakeshore_ch5").innerHTML = (message.data);
});

lakeshore_ch6.subscribe(function(message) {
    document.getElementById("lakeshore_ch6").innerHTML = (message.data);
});

lakeshore_ch7.subscribe(function(message) {
    document.getElementById("lakeshore_ch7").innerHTML = (message.data);
});

lakeshore_ch8.subscribe(function(message) {
    document.getElementById("lakeshore_ch8").innerHTML = (message.data);
});
