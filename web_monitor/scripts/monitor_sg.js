var ros = new ROSLIB.Ros({url : "ws://" + IP_rxobs + ":9000"});

ros.on("connection", function() {console.log("websocket: connected"); });
ros.on("error", function(error) {console.log("websocket error; ", error); });
ros.on('close', function() {
    console.log('websocket: closed, and reconection...');
    var ros = new ROSLIB.Ros({url : 'ws://' + IP_rxobs + ':9000'});
    console.log('websocket: connected')
        });

/*-- e8257d --*/

var e8257d_freq = new ROSLIB.Topic({
    ros : ros,
    name : "/e8257d_freq",
    messageType : "std_msgs/Float64"
});
var e8257d_power = new ROSLIB.Topic({
    ros : ros,
    name : "/e8257d_power",
    messageType : "std_msgs/Float64"
});
var e8257d_onoff = new ROSLIB.Topic({
    ros : ros,
    name : "/e8257d_onoff",
    messageType : "std_msgs/Int32"
});


e8257d_freq.subscribe(function(message) {
    document.getElementById("e8257d_freq").innerHTML = (message.data);
});

e8257d_power.subscribe(function(message) {
    document.getElementById("e8257d_power").innerHTML = (message.data);
});

e8257d_onoff.subscribe(function(message) {
    document.getElementById("e8257d_onoff").innerHTML = (message.data);
});


/*-- mg3692c --*/

var mg3692c_freq = new ROSLIB.Topic({
    ros : ros,
    name : "/mg3692c_freq",
    messageType : "std_msgs/Float64"
});
var mg3692c_power = new ROSLIB.Topic({
    ros : ros,
    name : "/mg3692c_power",
    messageType : "std_msgs/Float64"
});
var mg3692c_onoff = new ROSLIB.Topic({
    ros : ros,
    name : "/mg3692c_onoff",
    messageType : "std_msgs/Int32"
});


mg3692c_freq.subscribe(function(message) {
    document.getElementById("mg3692c_freq").innerHTML = (message.data);
});

mg3692c_power.subscribe(function(message) {
    document.getElementById("mg3692c_power").innerHTML = (message.data);
});

mg3692c_onoff.subscribe(function(message) {
    document.getElementById("mg3692c_onoff").innerHTML = (message.data);
});

/*-- fsw0020 --*/

var fsw0020_freq = new ROSLIB.Topic({
    ros : ros,
    name : "/fsw0020_freq",
    messageType : "std_msgs/Float64"
});
var fsw0020_power = new ROSLIB.Topic({
    ros : ros,
    name : "/fsw0020_power",
    messageType : "std_msgs/Float64"
});
var fsw0020_onoff = new ROSLIB.Topic({
    ros : ros,
    name : "/fsw0020_onoff",
    messageType : "std_msgs/Int32"
});


fsw0020_freq.subscribe(function(message) {
    document.getElementById("fsw0020_freq").innerHTML = (message.data);
});

fsw0020_power.subscribe(function(message) {
    document.getElementById("fsw0020_power").innerHTML = (message.data);
});

fsw0020_onoff.subscribe(function(message) {
    document.getElementById("fsw0020_onoff").innerHTML = (message.data);
});
